from flask import Flask
from config import configs

def create_app(config_key):
    app = Flask(__name__)
    app.config.from_object(configs[config_key])

    from app.blueprints import main
    from app.blueprints import auth
    from app.blueprints import user

    app.register_blueprint(main)
    app.register_blueprint(auth)
    app.register_blueprint(user)

    return app