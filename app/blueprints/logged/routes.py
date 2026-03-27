from flask import render_template, Blueprint, g
from app.decorators import authorized
from app.api_client.api.channels import get_available_channels_latest_channels_get

logged = Blueprint("logged", __name__, template_folder="templates")

@logged.route("/news", methods=["GET", "POST"])
@authorized
def news():
    return render_template("logged/news.html")

@logged.route("/channels", methods=["GET"])
@authorized
def channels():
    channels = g.services.channels.get_all_channels()
    return render_template("logged/channels.html", channels=channels)