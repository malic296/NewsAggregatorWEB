from app.api_client.client import AuthenticatedClient
from app.api_client.models import ChannelDTO
from app.api_client.api.channels import read_channels, set_disabled_channels
from app.models.errors import ExternalServiceError, RateLimitError


class ChannelsService:
    def __init__(self, client: AuthenticatedClient):
        self.client = client

    def get_all_channels(self) -> list[ChannelDTO]:
        response = read_channels.sync_detailed(
            client=self.client
        )

        if response.parsed.status_code == 429:
            raise RateLimitError("API rate limit exceeded")

        if response.parsed.status_code != 200:
            raise ExternalServiceError(f"API failed with: {response.status_code}")

        return response.parsed.channels

    def set_disabled_channels(self, channels_to_disable: list[ChannelDTO]) -> None:
        response = set_disabled_channels.sync_detailed(
            client=self.client,
            body=channels_to_disable
        )

        if response.parsed.status_code == 429:
            raise RateLimitError("API rate limit exceeded")

        if response.parsed.status_code != 200:
            raise ExternalServiceError(f"API failed with: {response.parsed.status_code}")

