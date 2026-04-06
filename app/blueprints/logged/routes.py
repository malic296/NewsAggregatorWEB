from flask import render_template, Blueprint, g, request, redirect, url_for
from app.decorators import authorized
from app.forms import FilterForm, ChannelFilterForm

logged = Blueprint("logged", __name__, template_folder="templates")

@logged.route("/profile", methods=["GET", "POST"])
@authorized
def profile():
    return render_template("logged/profile.html")

@logged.route("/logout", methods=["GET", "POST"])
@authorized
def logout():
    return render_template("auth/welcome.html")

@logged.route("/articles", methods=["GET", "POST"])
@authorized
def articles():
    filter_form = FilterForm()
    hours = 1

    if filter_form.validate_on_submit():
        hours = filter_form.hours.data
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