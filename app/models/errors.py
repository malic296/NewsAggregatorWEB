class APIError(Exception):
    def __init__(self, message: str, status_code: int = 500):
        self.status_code = status_code
        self.message = message

class UnauthorizedError(APIError):
    pass

class RateLimitError(APIError):
    pass