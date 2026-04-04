from flask import Flask, render_template, g
from app.blueprints import logged, auth
from app.dependencies.services import get_service_container
from app.dependencies import register_error_handlers

def create_app():
    app = Flask(__name__)

    app.config['SECRET_KEY'] = 'dev-secret-key-change-in-prod'
    app.config['API_URL'] = 'http://localhost:8000'

    app.register_blueprint(logged)
    app.register_blueprint(auth)
    register_error_handlers(app)


    @app.before_request
    def services_injection():
        if "services" not in g:
            g.services = get_service_container()

    @app.route('/')
    def index():
        return render_template('auth/welcome.html')

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
