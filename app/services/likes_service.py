from app.api_client.client import AuthenticatedClient

class LikesService:
    def __init__(self, client: AuthenticatedClient):
        self.client = client