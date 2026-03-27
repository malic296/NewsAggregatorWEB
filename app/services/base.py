from functools import wraps
from flask import redirect, url_for, flash

from app.models import AccessToken


def handle_api_errors(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        response = func(*args, **kwargs)

        if response.status_code == 401:
            return redirect((url_for("auth.login")))

        if response.status_code == 500:
            return redirect((url_for("auth.login")))

        return response
    return wrapper