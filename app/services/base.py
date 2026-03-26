from functools import wraps
from flask import redirect, url_for, flash

def handle_api_errors(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        response = func(*args, **kwargs)
        if response.status_code == 401:
            return redirect((url_for("auth.login")))

        if hasattr(response, "parsed") and response.parsed:
            if not response.parsed.success:
                flash(response.parsed.message, "danger")

        return response
    return wrapper