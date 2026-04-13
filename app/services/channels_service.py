from app.api_client.client import AuthenticatedClient
from app.api_client.models import ChannelDTO
from app.api_client.api.channels import read_channels, set_disabled_channels
from app.utils.errors import catch_api_errors


class ChannelsService:
    def __init__(self, client: AuthenticatedClient):
        self.client = client

    def get_all_channels(self) -> list[ChannelDTO]:
        response = read_channels.sync_detailed(
            client=self.client
        )

        catch_api_errors(response)

        return response.parsed.channels

    def set_disabled_channels(self, channels_to_disable: list[ChannelDTO]) -> None:
        response = set_disabled_channels.sync_detailed(
            client=self.client,
            body=channels_to_disable
        )

        catch_api_errors(response)

