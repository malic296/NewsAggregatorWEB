from app.api_client.client import AuthenticatedClient
from app.api_client.api.likes import like_article
from app.utils.errors import catch_api_errors

class LikesService:
    def __init__(self, client: AuthenticatedClient):
        self.client = client

    def like_article(self, uuid: str) -> bool:
        response = like_article.sync_detailed(
            client=self.client,
            article_uuid=uuid
        )

        catch_api_errors(response)

        return response.parsed.liked