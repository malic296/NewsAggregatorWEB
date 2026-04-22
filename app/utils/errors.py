from flask import render_template, flash, redirect, url_for
from app.models.errors import RateLimitError, UnauthorizedError

def register_error_handlers(app):
    @app.errorhandler(RateLimitError)
    def rate_limit_error(error):
        flash("Zpomal! příliš mnoho aktivit.", "warning")
        return redirect(url_for("main.index"))

    @app.errorhandler(UnauthorizedError)
    def unauthorized_error(error):
        flash("Unauthorized. Please log in first.", "warning")
        return redirect(url_for("auth.login"))

    @app.errorhandler(404)
    def not_found_error(error):
        return render_template("error.html", message="404. Page does not exist.")

    @app.errorhandler(Exception)
    def handle_default_exception(error):
        return render_template("error.html", message="Unexpected error. Please reload the page and try again.")


def catch_api_errors(response):
    if response.status_code != 200:
        raise APIError(f"HTTP Error: {response.status_code}")

    parsed = getattr(response, 'parsed', None)

    inner_status = None
    if parsed:
        if isinstance(parsed, dict):
            inner_status = parsed.get('status_code')
        else:
            inner_status = getattr(parsed, 'status_code', None)

    if inner_status is not None and inner_status != 200:
        if inner_status == 401:
            raise UnauthorizedError("Unauthorized. Please log in first.")
        elif inner_status == 429:
            raise RateLimitError("Too many requests. Try again later.")
        else:
            raise APIError(f"API Internal Error: {inner_status}")