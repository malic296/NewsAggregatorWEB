class NewsAggregatorError(Exception):
    def __init__(self, message, status_code=500):
        super().__init__(message)
        self.message = message
        self.status_code = status_code

class ExternalServiceError(NewsAggregatorError):
    pass

class RateLimitError(NewsAggregatorError):
    def __init__(self, message="Too many requests"):
        super().__init__(message, status_code=429)