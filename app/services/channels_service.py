from app.api_client.client import AuthenticatedClient
from app.api_client.models import ChannelDTO
from app.api_client.api.channels import get_available_channels_latest_channels_get


class ChannelsService:
    def __init__(self, client: AuthenticatedClient):
        self.client = client

    def get_all_channels(self) -> list[ChannelDTO]:
        response = get_available_channels_latest_channels_get.sync_detailed(
            client=self.client
        )

        return response.parsed.data