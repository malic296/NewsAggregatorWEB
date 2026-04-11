from flask import Blueprint

logged = Blueprint("logged", __name__, template_folder="templates")

from . import routes