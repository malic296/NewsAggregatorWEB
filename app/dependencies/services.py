from app.models import ServiceContainer
from app.services import ArticlesService, ChannelsService, LikesService, ConsumersService
from flask import g, request
from app.api_client.client import AuthenticatedClient, Client

def get_service_container() -> ServiceContainer:
    if "services" not in g:
        token= request.cookies.get("access_token")

        if token:
            client = AuthenticatedClient(
                base_url="http://localhost:8000",
                token=token,
                prefix="Bearer"
            )
        else:
            client = Client(
                base_url="http://localhost:8000",
            )

        g.services = ServiceContainer(
            articles=ArticlesService(client),
            channels=ChannelsService(client),
            likes=LikesService(client),
            consumers=ConsumersService(client)
        )

    return g.services