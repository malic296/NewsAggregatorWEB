from app.api_client.client import AuthenticatedClient, Client
from app.api_client.api.consumers import login, request_new_registration, verify_email
from app.api_client.models import BodyLogin, RegistrationDTO, TokenResponse
from typing import Optional
from app.models import AccessToken

class ConsumersService:
    def __init__(self, client: AuthenticatedClient | Client):
        self.client = client

    def login_user(self, credential: str, password: str) -> Optional[TokenResponse]:
        form_data = BodyLogin(
            username=credential,
            password=password
        )

        response = login.sync_detailed(
            client=self.client,
            body=form_data
        )

        try:
            return response.parsed
        except KeyError:
            return None

    def request_new_registration(self, registration: RegistrationDTO):
        result = request_new_registration.sync_detailed(
            client=self.client,
            body=registration
        )

        if result.parsed is not None:
            if result.parsed.status_code != 200:
                return False

            return True
        else:
            return False

    def verify_email(self, email: str, code: int) -> Optional[TokenResponse]:
        response = verify_email.sync_detailed(
            client=self.client,
            email=email,
            code=code
        )

        try:
            return response.parsed
        except KeyError:
            return None


