from app.api_client.client import AuthenticatedClient
from.base import handle_api_errors

class ArticlesService:
    def __init__(self, client: AuthenticatedClient):
        self.client = client