from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...models.response_dt_olist_article_dto import ResponseDTOlistArticleDTO
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    hours: int | Unset = 1,
    channel_ids: list[int] | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["hours"] = hours

    json_channel_ids: list[int] | Unset = UNSET
    if not isinstance(channel_ids, Unset):
        json_channel_ids = channel_ids

    params["channel_ids"] = json_channel_ids

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/latest/articles/",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> HTTPValidationError | ResponseDTOlistArticleDTO | None:
    if response.status_code == 200:
        response_200 = ResponseDTOlistArticleDTO.from_dict(response.json())

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
) -> Response[HTTPValidationError | ResponseDTOlistArticleDTO]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    hours: int | Unset = 1,
    channel_ids: list[int] | Unset = UNSET,
) -> Response[HTTPValidationError | ResponseDTOlistArticleDTO]:
    """Get Articles

    Args:
        hours (int | Unset):  Default: 1.
        channel_ids (list[int] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | ResponseDTOlistArticleDTO]
    """

    kwargs = _get_kwargs(
        hours=hours,
        channel_ids=channel_ids,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    hours: int | Unset = 1,
    channel_ids: list[int] | Unset = UNSET,
) -> HTTPValidationError | ResponseDTOlistArticleDTO | None:
    """Get Articles

    Args:
        hours (int | Unset):  Default: 1.
        channel_ids (list[int] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | ResponseDTOlistArticleDTO
    """

    return sync_detailed(
        client=client,
        hours=hours,
        channel_ids=channel_ids,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    hours: int | Unset = 1,
    channel_ids: list[int] | Unset = UNSET,
) -> Response[HTTPValidationError | ResponseDTOlistArticleDTO]:
    """Get Articles

    Args:
        hours (int | Unset):  Default: 1.
        channel_ids (list[int] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | ResponseDTOlistArticleDTO]
    """

    kwargs = _get_kwargs(
        hours=hours,
        channel_ids=channel_ids,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    hours: int | Unset = 1,
    channel_ids: list[int] | Unset = UNSET,
) -> HTTPValidationError | ResponseDTOlistArticleDTO | None:
    """Get Articles

    Args:
        hours (int | Unset):  Default: 1.
        channel_ids (list[int] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | ResponseDTOlistArticleDTO
    """

    return (
        await asyncio_detailed(
            client=client,
            hours=hours,
            channel_ids=channel_ids,
        )
    ).parsed
