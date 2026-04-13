from app.api_client.client import AuthenticatedClient, Client
from app.api_client.api.consumers import login, request_new_registration, verify_email, get_currently_logged_consumer, update_credentials
from app.api_client.models import BodyLogin, RegistrationDTO, TokenResponse, ConsumerDTO, UpdateCredentialsDTO
from typing import Optional
from app.utils.errors import catch_api_errors
from models import APIError


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

        catch_api_errors(response)

        try:
            return response.parsed
        except KeyError:
            return None

    def request_new_registration(self, registration: RegistrationDTO):
        response = request_new_registration.sync_detailed(
            client=self.client,
            body=registration
        )

        catch_api_errors(response)

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

        catch_api_errors(response)

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

        catch_api_errors(response)

        try:
            return response.parsed.consumers[0]
        except IndexError:
            raise APIError(f"API succeeded but did not return a user for get_current_user.")

    def update_credentials(self, credentials: UpdateCredentialsDTO):
        if not isinstance(self.client, AuthenticatedClient):
            raise Exception('This method can be called only with authenticated client.')

        response = update_credentials.sync_detailed(
            client=self.client,
            body=credentials
        )

        catch_api_errors(response)

        try:
            return response.parsed
        except KeyError:
            return None

