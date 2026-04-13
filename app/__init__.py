from flask import Flask
from config import configs
from app.utils.errors import register_error_handlers

def create_app(config_key):
    app = Flask(__name__)
    app.config.from_object(configs[config_key])

    from app.blueprints import main, auth, user

    app.register_blueprint(main)
    app.register_blueprint(auth)
    app.register_blueprint(user)

    register_error_handlers(app)

    return app