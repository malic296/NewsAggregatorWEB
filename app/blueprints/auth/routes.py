from flask import redirect, render_template, url_for, flash, session
from app.api_client.models import RegistrationDTO, TokenResponse
from dependencies.services import get_services
from .forms import LoginForm, RegistrationForm, VerifyForm
from . import auth

@auth.route('/')
def index():
    return render_template('auth/welcome.html')


@auth.route("/login", methods=["GET", "POST"])
def login():
    services = get_services()
    form = LoginForm()
    if form.validate_on_submit():
        token: TokenResponse = services.consumers.login_user(form.credential.data, form.password.data)

        if token:
            resp = redirect(url_for('logged.articles'))
            resp.set_cookie(
                'access_token',
                token.access_token,
                httponly=True,
                secure=False,
                samesite='Lax',
                max_age=1800
            )
            return resp

        flash("Login failed. Please check your credentials.", "danger")

    return render_template("auth/login.html", form = form)

@auth.route("/register", methods=["GET", "POST"])
def register():
    services = get_services()
    form = RegistrationForm()
    if form.validate_on_submit():
        email_sent = services.consumers.request_new_registration(RegistrationDTO(form.username.data, form.email.data, form.password.data))
        if email_sent:
            session["pending_email"] = form.email.data
            return redirect(url_for('auth.verify'))

    return render_template("auth/register.html", form = form)

@auth.route("/verify", methods=["GET", "POST"])
def verify():
    services = get_services()
    form = VerifyForm()
    email = session.get("pending_email")
    if not email:
        return redirect(url_for('auth.register'))
    if form.validate_on_submit():
        token = services.consumers.verify_email(email=email, code=int(form.code.data))
        if token:
            session.pop("pending_email", None)

            resp = redirect(url_for('logged.articles'))
            resp.set_cookie(
                'access_token',
                token.access_token,
                httponly=True,
                secure=False,
                samesite='Lax',
                max_age=1800
            )
            return resp

        flash("Login failed. Please check your credentials.", "danger")

    return render_template("auth/verify.html", form = form)
