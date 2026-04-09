from http import HTTPStatus
from typing import Any

import httpx

from app.api_client import errors
from app.api_client.client import AuthenticatedClient, Client
from app.api_client.models import HTTPValidationError
from app.api_client.models.like_response import LikeResponse
from app.api_client.types import UNSET, Response


def _get_kwargs(
    *,
    article_uuid: str,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["article_uuid"] = article_uuid

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/latest/likes/like_article",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> HTTPValidationError | LikeResponse | None:
    if response.status_code == 200:
        response_200 = LikeResponse.from_dict(response.json())

        return response_200

    if response.status_code == 422:
        response_422 = HTTPValidationError.from_dict(response.json())

        return response_422

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[HTTPValidationError | LikeResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    article_uuid: str,
) -> Response[HTTPValidationError | LikeResponse]:
    """Like Article

    Args:
        article_uuid (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | LikeResponse]
    """

    kwargs = _get_kwargs(
        article_uuid=article_uuid,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    article_uuid: str,
) -> HTTPValidationError | LikeResponse | None:
    """Like Article

    Args:
        article_uuid (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | LikeResponse
    """

    return sync_detailed(
        client=client,
        article_uuid=article_uuid,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    article_uuid: str,
) -> Response[HTTPValidationError | LikeResponse]:
    """Like Article

    Args:
        article_uuid (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | LikeResponse]
    """

    kwargs = _get_kwargs(
        article_uuid=article_uuid,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    article_uuid: str,
) -> HTTPValidationError | LikeResponse | None:
    """Like Article

    Args:
        article_uuid (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | LikeResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            article_uuid=article_uuid,
        )
    ).parsed
