from app.api_client.client import AuthenticatedClient
from app.api_client.models import ChannelDTO
from app.api_client.api.channels import channels, disabled
from app.models.errors import ExternalServiceError, RateLimitError


class ChannelsService:
    def __init__(self, client: AuthenticatedClient):
        self.client = client

    def get_all_channels(self) -> list[ChannelDTO]:
        response = channels.sync_detailed(
            client=self.client
        )

        if response.status_code == 429:
            raise RateLimitError("Příliš mnoho pokusů. Zkuste to prosím později.")

        if response.status_code == 401:
            raise ExternalServiceError("Neplatné přihlašovací údaje.", status_code=401)

        if response.status_code >= 500:
            raise ExternalServiceError("Služba je dočasně nedostupná.", status_code=response.status_code)

        if response.status_code != 200:
            raise ExternalServiceError(f"API failed with: {response.status_code}")

        return response.parsed.channels

    def set_disabled_channels(self, channels_to_disable: list[ChannelDTO]) -> None:
        response = disabled.sync_detailed(
            client=self.client,
            body=channels_to_disable
        )

        if response.status_code == 429:
            raise RateLimitError("Příliš mnoho pokusů. Zkuste to prosím později.")

        if response.status_code == 401:
            raise ExternalServiceError("Neplatné přihlašovací údaje.", status_code=401)

        if response.status_code >= 500:
            raise ExternalServiceError("Služba je dočasně nedostupná.", status_code=response.status_code)

        if response.status_code != 200:
            raise ExternalServiceError(f"API failed with: {response.status_code}")

