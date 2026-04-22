from app.api_client.client import AuthenticatedClient, Client
from app.api_client.api.consumers import login, register, verification, me, credentials
from app.api_client.models import BodyLogin, RegistrationDTO, TokenResponse, ConsumerDTO, UpdateCredentialsDTO
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
            raise RateLimitError("Příliš mnoho pokusů. Zkuste to prosím později.")

        if response.status_code == 401:
            raise ExternalServiceError("Neplatné přihlašovací údaje.", status_code=401)

        if response.status_code >= 500:
            raise ExternalServiceError("Služba je dočasně nedostupná.", status_code=response.status_code)

        if response.status_code != 200:
            raise ExternalServiceError(f"API failed with: {response.status_code}")

        try:
            return response.parsed
        except KeyError:
            return None

    def request_new_registration(self, registration: RegistrationDTO):
        response = register.sync_detailed(
            client=self.client,
            body=registration
        )

        if response.status_code == 429:
            raise RateLimitError("Příliš mnoho pokusů. Zkuste to prosím později.")

        if response.status_code == 401:
            raise ExternalServiceError("Neplatné přihlašovací údaje.", status_code=401)

        if response.status_code >= 500:
            raise ExternalServiceError("Služba je dočasně nedostupná.", status_code=response.status_code)

        if response.status_code != 200:
            raise ExternalServiceError(f"API failed with: {response.status_code}")

        if response.parsed is not None:
            return True
        else:
            return False

    def verify_email(self, email: str, code: int) -> Optional[TokenResponse]:
        response = verification.sync_detailed(
            client=self.client,
            email=email,
            code=code
        )

        if response.status_code == 429:
            raise RateLimitError("Příliš mnoho pokusů. Zkuste to prosím později.")

        if response.status_code == 401:
            raise ExternalServiceError("Neplatné přihlašovací údaje.", status_code=401)

        if response.status_code >= 500:
            raise ExternalServiceError("Služba je dočasně nedostupná.", status_code=response.status_code)

        if response.status_code != 200:
            raise ExternalServiceError(f"API failed with: {response.status_code}")

        try:
            return response.parsed
        except KeyError:
            return None

    def get_current_user(self) -> ConsumerDTO:
        if not isinstance(self.client, AuthenticatedClient):
            raise Exception('This method can be called only with authenticated client.')

        response = me.sync_detailed(
            client=self.client
        )

        if response.status_code == 429:
            raise RateLimitError("API rate limit exceeded")

        if response.status_code != 200:
            raise ExternalServiceError(f"API failed with: {response.status_code}")

        try:
            return response.parsed.consumer
        except IndexError:
            raise ExternalServiceError(f"API succeeded but did not return a user for get_current_user.")

    def update_credentials(self, new_credentials: UpdateCredentialsDTO):
        if not isinstance(self.client, AuthenticatedClient):
            raise Exception('This method can be called only with authenticated client.')

        response = credentials.sync_detailed(
            client=self.client,
            body=new_credentials
        )

        if response.status_code == 429:
            raise RateLimitError("Příliš mnoho pokusů. Zkuste to prosím později.")

        if response.status_code == 401:
            raise ExternalServiceError("Neplatné přihlašovací údaje.", status_code=401)

        if response.status_code >= 500:
            raise ExternalServiceError("Služba je dočasně nedostupná.", status_code=response.status_code)

        if response.status_code != 200:
            raise ExternalServiceError(f"API failed with: {response.status_code}")

        try:
            return response.parsed
        except KeyError:
            return None

