from flask import render_template, Blueprint, g, request, redirect, url_for, flash

from app.api_client.models import UpdateCredentialsDTO, TokenResponse
from app.decorators import authorized
from app.forms import FilterForm, ChannelFilterForm, CredentialsForm

logged = Blueprint("logged", __name__, template_folder="templates")

@logged.route("/profile", methods=["GET", "POST"])
@authorized
def profile():
    form = CredentialsForm()

    if form.validate_on_submit():
        req = UpdateCredentialsDTO(old_password=form.old_password.data)
        if form.new_username.data:
            req.new_username = form.new_username.data

        if form.new_password.data:
            req.new_password = form.new_password.data

        token: TokenResponse = g.services.consumers.update_credentials(req)

        if token:
            resp = redirect(url_for("logged.profile"))
            resp.delete_cookie(
                'access_token',
                httponly=True,
                secure=False,
                samesite='Lax'
            )

            resp.set_cookie(
                "access_token",
                token.access_token,
                httponly=True,
                secure=False,
                samesite='Lax',
                max_age=1800
            )

            return resp

    user = g.services.consumers.get_current_user()
    return render_template("logged/profile.html", user=user, form=form)

@logged.route("/logout", methods=["GET", "POST"])
@authorized
def logout():
    resp = redirect(url_for("auth.index"))
    resp.delete_cookie(
        'access_token',
        httponly=True,
        secure=False,
        samesite='Lax'
    )
    return resp

@logged.route("/articles", methods=["GET", "POST"])
@authorized
def articles():
    filter_form = FilterForm()
    hours = 1

    if filter_form.validate_on_submit():
        try:
            hours = int(filter_form.hours.data)
        except Exception:
            flash("Hours must be in integer format", "error")
            hours = 1
        if not hours or int(hours) < 1:
            filter_form.hours.errors.append("Hours must be set to 1 or greater.")
            articles = g.services.articles.read_articles()

        else:
            articles = g.services.articles.read_articles(hours=int(hours))
    else:
        articles = g.services.articles.read_articles(hours=hours)

    articles.sort(key=lambda x: x.likes, reverse=True)
    return render_template("logged/articles.html", articles=articles, filter_form=filter_form, current_hours = hours)

@logged.route("/like_article/<uuid>", methods=["POST"])
@authorized
def like_article(uuid):
    liked = g.services.likes.like_article(uuid)
    return {"liked": liked}

@logged.route("/channels", methods=["GET", "POST"])
@authorized
def channels():
    all_channels = g.services.channels.get_all_channels()
    form = ChannelFilterForm()

    if form.validate_on_submit():
        disabled_uuids = request.form.getlist("disabled")
        disabled_channels = [channel for channel in all_channels if channel.uuid in disabled_uuids]
        g.services.channels.set_disabled_channels(disabled_channels)

        updated_channels = g.services.channels.get_all_channels()
        return redirect(url_for('logged.channels'))

    return render_template("logged/channels.html", channels=all_channels, form=form)