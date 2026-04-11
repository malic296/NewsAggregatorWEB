from flask import Flask
from config import configs

def create_app(config_key):
    app = Flask(__name__)
    app.config.from_object(configs[config_key])

    from app.blueprints import logged
    from app.blueprints import auth

    app.register_blueprint(logged)
    app.register_blueprint(auth)

    return app