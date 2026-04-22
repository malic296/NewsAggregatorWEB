from app.api_client.client import AuthenticatedClient
from app.api_client.api.articles import articles, article, like
from app.api_client.models import ArticleDTO
from typing import Optional
from app.models.errors import ExternalServiceError, RateLimitError

class ArticlesService:
    def __init__(self, client: AuthenticatedClient):
        self.client = client

    def read_articles(self, hours: Optional[int] = None) -> list[ArticleDTO]:
        response = articles.sync_detailed(
            client=self.client,
            hours=hours if hours else 1
        )

        if response.status_code == 429:
            raise RateLimitError("Příliš mnoho pokusů. Zkuste to prosím později.")

        if response.status_code == 401:
            raise ExternalServiceError("Neplatné přihlašovací údaje.", status_code=401)

        if response.status_code >= 500:
            raise ExternalServiceError("Služba je dočasně nedostupná.", status_code=response.status_code)

        if response.status_code != 200:
            raise ExternalServiceError(f"API failed with: {response.status_code}")

        return response.parsed.articles

    def read_article(self, uuid: str) -> Optional[ArticleDTO]:
        response = article.sync_detailed(
            client=self.client,
            uuid=uuid,
        )

        if response.status_code == 429:
            raise RateLimitError("Příliš mnoho pokusů. Zkuste to prosím později.")

        if response.status_code == 401:
            raise ExternalServiceError("Neplatné přihlašovací údaje.", status_code=401)

        if response.status_code >= 500:
            raise ExternalServiceError("Služba je dočasně nedostupná.", status_code=response.status_code)

        if response.status_code != 200:
            raise ExternalServiceError(f"API failed with: {response.status_code}")

        return response.parsed.article

    def like_article(self, uuid: str) -> bool:
        response = like.sync_detailed(
            client=self.client,
            article_uuid=uuid
        )

        if response.status_code == 429:
            raise RateLimitError("Příliš mnoho pokusů. Zkuste to prosím později.")

        if response.status_code == 401:
            raise ExternalServiceError("Neplatné přihlašovací údaje.", status_code=401)

        if response.status_code >= 500:
            raise ExternalServiceError("Služba je dočasně nedostupná.", status_code=response.status_code)

        if response.status_code != 200:
            raise ExternalServiceError(f"API failed with: {response.status_code}")

        return response.parsed.liked