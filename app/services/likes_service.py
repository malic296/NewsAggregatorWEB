from app.api_client.client import AuthenticatedClient
from app.api_client.api.likes import like_article
from app.models.errors import RateLimitError, ExternalServiceError

class LikesService:
    def __init__(self, client: AuthenticatedClient):
        self.client = client

    def like_article(self, uuid: str) -> bool:
        response = like_article.sync_detailed(
            client=self.client,
            article_uuid=uuid
        )

        if response.parsed.status_code == 429:
            raise RateLimitError("API rate limit exceeded")

        if response.parsed.status_code != 200:
            raise ExternalServiceError(f"API failed with: {response.parsed.status_code}")

        return response.parsed.liked