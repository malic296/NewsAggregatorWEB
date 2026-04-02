from app.api_client.client import AuthenticatedClient
from app.api_client.models import ChannelDTO
from app.api_client.api.channels import read_channels


class ChannelsService:
    def __init__(self, client: AuthenticatedClient):
        self.client = client

    def get_all_channels(self) -> list[ChannelDTO]:
        response = read_channels.sync_detailed(
            client=self.client
        )

        return response.parsed.channels