from app.api_client.client import AuthenticatedClient, Client
from app.api_client.api.consumers import login_latest_consumers_login_post, request_new_registration_latest_consumers_register_request_new_registration_post, verify_email_latest_consumers_register_verify_email_post
from app.api_client.models import BodyLoginLatestConsumersLoginPost, RegistrationDTO, ResponseDTONoneType
from .base import handle_api_errors
from typing import Optional
from app.models import AccessToken

class ConsumersService:
    def __init__(self, client: AuthenticatedClient | Client):
        self.client = client

    def login_user(self, credential: str, password: str) -> Optional[AccessToken]:
        form_data = BodyLoginLatestConsumersLoginPost(
            username=credential,
            password=password
        )

        response = login_latest_consumers_login_post.sync_detailed(
            client=self.client,
            body=form_data
        )

        try:
            return AccessToken(**response.parsed)
        except KeyError:
            return None

    def request_new_registration(self, registration: RegistrationDTO):
        result = request_new_registration_latest_consumers_register_request_new_registration_post.sync_detailed(
            client=self.client,
            body=registration
        )

        if result.parsed is not None:
            if result.parsed.status_code != 200:
                return False

            return True
        else:
            return False

    def verify_email(self, email: str, code: int) -> Optional[AccessToken]:
        response = verify_email_latest_consumers_register_verify_email_post.sync_detailed(
            client=self.client,
            email=email,
            code=code
        )

        try:
            return AccessToken(**response.parsed)
        except KeyError:
            return None


