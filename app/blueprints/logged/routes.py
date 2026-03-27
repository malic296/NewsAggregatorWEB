from flask import render_template
from flask import Blueprint
from app.decorators import authorized

logged = Blueprint("logged", __name__, template_folder="templates")

@logged.route("/index")
@authorized
def index():
    return render_template("logged/index.html")