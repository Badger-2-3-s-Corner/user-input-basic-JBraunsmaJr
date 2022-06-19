from flask import Blueprint

my_app = Blueprint("blueprints", __name__, template_folder="templates")

from . import routes