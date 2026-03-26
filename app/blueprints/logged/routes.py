from flask import render_template
from flask import Blueprint

logged = Blueprint("logged", __name__, template_folder="templates")

@logged.route("/index")
def index():
    return render_template("logged/index.html")