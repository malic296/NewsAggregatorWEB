from app.api_client.client import AuthenticatedClient
from app.api_client.api.likes import like_article

class LikesService:
    def __init__(self, client: AuthenticatedClient):
        self.client = client

    def like_articles(self, uuid: str) -> bool:
        response = like_article.sync_detailed(
            client=self.client,
            article_uuid=uuid
        )

        if not response.parsed.success:
            raise Exception("Liking article failed.")

        return response.parsed.liked