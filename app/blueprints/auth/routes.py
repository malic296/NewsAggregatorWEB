from flask import request, redirect, render_template, url_for, flash
from app.dependencies.services import get_service_container
from app.forms import LoginForm, RegistrationForm
from flask import Blueprint

auth = Blueprint("auth", __name__, template_folder="templates")


@auth.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():

        services = get_service_container()
        api_response = services.consumers.login_user(form.credential.data, form.password.data)

        if api_response.status_code == 200:
            token = api_response.parsed.access_token

            resp = redirect(url_for('logged.index'))
            resp.set_cookie(
                'access_token',
                token,
                httponly=True,
                secure=False,
                samesite='Lax'
            )
            return resp

        flash("Login failed. Please check your credentials.", "danger")

    return render_template("auth/login.html", form = form)

@auth.route("/register", methods=["GET", "POST"])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        return render_template("welcome.html", form = form)
        services = get_service_container()
        api_response = services.consumers.login_user(form.username.data, form.email.data, form.password.data)

        if api_response.status_code == 200:
            token = api_response.parsed.access_token

            resp = redirect(url_for('logged.index'))
            resp.set_cookie(
                'access_token',
                token,
                httponly=True,
                secure=False,
                samesite='Lax'
            )
            return resp

        flash("Login failed. Please check your credentials.", "danger")

    return render_template("auth/register.html", form = form)