from app.api_client.client import AuthenticatedClient
from app.api_client.api.articles import read_articles
from app.api_client.models import ArticleDTO
from typing import Optional

class ArticlesService:
    def __init__(self, client: AuthenticatedClient):
        self.client = client

    def read_articles(self, hours: Optional[int] = None) -> list[ArticleDTO]:
        result = read_articles.sync_detailed(
            client=self.client,
            hours=hours if hours else 1
        )

        return result.parsed.articles