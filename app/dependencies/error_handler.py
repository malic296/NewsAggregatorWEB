from flask import render_template, flash, redirect, url_for
from app.models.errors import ExternalServiceError, RateLimitError

def register_error_handlers(app):
    @app.errorhandler(ExternalServiceError)
    def external_service_error(error):
        return render_template("auth/error.html", message= "External service error. Please try again later.")

    @app.errorhandler(Exception)
    def handle_default_exception(error):
        return render_template("auth/error.html", message= "Unexpected error.")

    @app.errorhandler(RateLimitError)
    def handle_rate_limit(error):
        flash("Slow down! Too many requests. Please try again in a moment.", "warning")
        return redirect(url_for("index"))

    @app.errorhandler(404)
    def not_found_error(error):
        return render_template("auth/error.html", message= "404. Page does not exist.")