from flask import redirect, render_template, url_for, flash, session, g
from app.api_client.models import RegistrationDTO
from app.dependencies.services import get_service_container
from app.forms import LoginForm, RegistrationForm, VerifyForm
from flask import Blueprint

auth = Blueprint("auth", __name__, template_folder="templates")

@auth.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        token = g.services.consumers.login_user(form.credential.data, form.password.data)

        if token:
            resp = redirect(url_for('logged.index'))
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
    form = RegistrationForm()
    if form.validate_on_submit():
        email_sent = g.services.consumers.request_new_registration(RegistrationDTO(form.username.data, form.email.data, form.password.data))
        if email_sent:
            session["pending_email"] = form.email.data
            return redirect(url_for('auth.verify'))

    return render_template("auth/register.html", form = form)

@auth.route("/verify", methods=["GET", "POST"])
def verify():
    form = VerifyForm()
    email = session.get("pending_email")
    if not email:
        return redirect(url_for('auth.register'))
    if form.validate_on_submit():
        token = g.services.consumers.verify_email(email=email, code=int(form.code.data))
        if token:
            session.pop("pending_email", None)

            resp = redirect(url_for('logged.index'))
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