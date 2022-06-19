from flask import Flask, Blueprint


def create_app(config_filename=None):
    flaskapp = Flask(__name__, instance_relative_config=True)

    if config_filename is not None:
        flaskapp.config.from_pyfile(config_filename)

    app_blueprint = Blueprint('flaskProject', __name__, template_folder='templates')
    register_blueprints(flaskapp)
    return flaskapp, app_blueprint


def register_blueprints(app):
    from project.blueprints import my_app
    app.register_blueprint(my_app)