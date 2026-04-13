from app.api_client.client import AuthenticatedClient
from app.api_client.api.articles import read_articles, read_article
from app.api_client.models import ArticleDTO
from typing import Optional
from app.utils.errors import catch_api_errors

class ArticlesService:
    def __init__(self, client: AuthenticatedClient):
        self.client = client

    def read_articles(self, hours: Optional[int] = None) -> list[ArticleDTO]:
        response = read_articles.sync_detailed(
            client=self.client,
            hours=hours if hours else 1
        )

        catch_api_errors(response)

        return response.parsed.articles

    def read_article(self, uuid: str) -> Optional[ArticleDTO]:
        response = read_article.sync_detailed(
            client=self.client,
            uuid=uuid,
        )

        catch_api_errors(response)

        return response.parsed.article