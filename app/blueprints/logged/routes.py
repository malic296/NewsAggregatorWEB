from flask import render_template, Blueprint, g
from app.decorators import authorized

logged = Blueprint("logged", __name__, template_folder="templates")

@logged.route("/news", methods=["GET", "POST"])
@authorized
def news():
    #news = g.services.articles.read_articles()
    return render_template("logged/news.html")

@logged.route("/channels", methods=["GET"])
@authorized
def channels():
    channels = g.services.channels.get_all_channels()
    return render_template("logged/channels.html", channels=channels)