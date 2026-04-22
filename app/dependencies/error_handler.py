from flask import render_template, flash, redirect, url_for
from app.models.errors import ExternalServiceError, RateLimitError
from flask import render_template, flash, redirect, request, url_for
from app.models.errors import NewsAggregatorError, RateLimitError
from werkzeug.exceptions import HTTPException

def register_error_handlers(app):
    @app.errorhandler(NewsAggregatorError)
    def handle_custom_errors(error):
        if isinstance(error, RateLimitError):
            return render_template("error.html", message=error.message), 429

        if 400 <= error.status_code < 500:
            flash(error.message, "danger")
            target = request.referrer or url_for('auth.index')
            return redirect(target)

        return render_template("error.html", message=error.message), error.status_code

    @app.errorhandler(404)
    def not_found_error(error):
        return render_template("error.html", message="Stránka nenalezena (404)"), 404

    @app.errorhandler(Exception)
    def handle_unexpected_error(error):
        return render_template("error.html", message="Došlo k neočekávané chybě na serveru."), 500