from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...models.response_dt_obool import ResponseDTObool
from ...types import UNSET, Response


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
) -> HTTPValidationError | ResponseDTObool | None:
    if response.status_code == 200:
        response_200 = ResponseDTObool.from_dict(response.json())

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
) -> Response[HTTPValidationError | ResponseDTObool]:
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
) -> Response[HTTPValidationError | ResponseDTObool]:
    """Like Article

    Args:
        article_uuid (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | ResponseDTObool]
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
) -> HTTPValidationError | ResponseDTObool | None:
    """Like Article

    Args:
        article_uuid (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | ResponseDTObool
    """

    return sync_detailed(
        client=client,
        article_uuid=article_uuid,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    article_uuid: str,
) -> Response[HTTPValidationError | ResponseDTObool]:
    """Like Article

    Args:
        article_uuid (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | ResponseDTObool]
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
) -> HTTPValidationError | ResponseDTObool | None:
    """Like Article

    Args:
        article_uuid (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | ResponseDTObool
    """

    return (
        await asyncio_detailed(
            client=client,
            article_uuid=article_uuid,
        )
    ).parsed
