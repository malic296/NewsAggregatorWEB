from app.api_client.client import AuthenticatedClient, Client
from app.api_client.api.consumers import login_latest_consumers_login_post
from app.api_client.models import BodyLoginLatestConsumersLoginPost
from .base import handle_api_errors

class ConsumersService:
    def __init__(self, client: AuthenticatedClient | Client):
        self.client = client

    @handle_api_errors
    def login_user(self, credential: str, password: str):
        form_data = BodyLoginLatestConsumersLoginPost(
            username=credential,
            password=password
        )

        return login_latest_consumers_login_post.sync_detailed(
            client=self.client,
            body=form_data
        )
