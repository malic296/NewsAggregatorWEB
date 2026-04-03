from app.api_client.client import AuthenticatedClient
from app.api_client.models import ChannelDTO
from app.api_client.api.channels import read_channels, set_disabled_channels


class ChannelsService:
    def __init__(self, client: AuthenticatedClient):
        self.client = client

    def get_all_channels(self) -> list[ChannelDTO]:
        response = read_channels.sync_detailed(
            client=self.client
        )

        if not response.parsed.success:
            raise Exception("Failed getting all channels.")

        return response.parsed.channels

    def set_disabled_channels(self, channels_to_disable: list[ChannelDTO]) -> None:
        response = set_disabled_channels.sync_detailed(
            client=self.client,
            body=channels_to_disable
        )

        if not response.parsed.success:
            raise Exception("Failed setting disabled channels.")

