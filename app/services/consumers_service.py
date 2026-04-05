from app.api_client.client import AuthenticatedClient, Client
from app.api_client.api.consumers import login, request_new_registration, verify_email, get_currently_logged_consumer
from app.api_client.models import BodyLogin, RegistrationDTO, TokenResponse, ConsumerDTO
from typing import Optional
from app.models.errors import RateLimitError, ExternalServiceError

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

        if response.status_code == 429:
            raise RateLimitError("API rate limit exceeded")

        if response.status_code != 200:
            raise ExternalServiceError(f"API failed with: {response.status_code}")

        try:
            return response.parsed
        except KeyError:
            return None

    def request_new_registration(self, registration: RegistrationDTO):
        response = request_new_registration.sync_detailed(
            client=self.client,
            body=registration
        )

        if response.parsed.status_code == 429:
            raise RateLimitError("API rate limit exceeded")

        if response.parsed.status_code != 200:
            raise ExternalServiceError(f"API failed with: {response.parsed.status_code}")

        if response.parsed is not None:
            return True
        else:
            return False

    def verify_email(self, email: str, code: int) -> Optional[TokenResponse]:
        response = verify_email.sync_detailed(
            client=self.client,
            email=email,
            code=code
        )

        if response.status_code == 429:
            raise RateLimitError("API rate limit exceeded")

        if response.status_code != 200:
            raise ExternalServiceError(f"API failed with: {response.status_code}")

        try:
            return response.parsed
        except KeyError:
            return None

    def get_current_user(self) -> ConsumerDTO:
        if not isinstance(self.client, AuthenticatedClient):
            raise Exception('This method can be called only with authenticated client.')

        response = get_currently_logged_consumer.sync_detailed(
            client=self.client
        )

        if response.parsed.status_code == 429:
            raise RateLimitError("API rate limit exceeded")

        if response.parsed.status_code != 200:
            raise ExternalServiceError(f"API failed with: {response.parsed.status_code}")

        try:
            return response.parsed.consumers[0]
        except IndexError:
            raise ExternalServiceError(f"API succeeded but did not return a user for get_current_user.")

