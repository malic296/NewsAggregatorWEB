from app.api_client.client import AuthenticatedClient
from app.api_client.api.articles import read_articles
from app.api_client.models import ArticleDTO
from typing import Optional
from app.models.errors import ExternalServiceError, RateLimitError

class ArticlesService:
    def __init__(self, client: AuthenticatedClient):
        self.client = client

    def read_articles(self, hours: Optional[int] = None) -> list[ArticleDTO]:
        response = read_articles.sync_detailed(
            client=self.client,
            hours=hours if hours else 1
        )

        if response.parsed.status_code == 429:
            raise RateLimitError("API rate limit exceeded")

        if response.parsed.status_code != 200:
            raise ExternalServiceError(f"API failed with: {response.parsed.status_code}")

        return response.parsed.articles