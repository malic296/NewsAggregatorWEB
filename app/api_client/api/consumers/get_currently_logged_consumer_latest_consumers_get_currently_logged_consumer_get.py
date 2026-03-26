from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.response_dto_consumer_dto import ResponseDTOConsumerDTO
from ...types import Response


def _get_kwargs() -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/latest/consumers/get_currently_logged_consumer",
    }

    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> ResponseDTOConsumerDTO | None:
    if response.status_code == 200:
        response_200 = ResponseDTOConsumerDTO.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[ResponseDTOConsumerDTO]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
) -> Response[ResponseDTOConsumerDTO]:
    """Get Currently Logged Consumer

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ResponseDTOConsumerDTO]
    """

    kwargs = _get_kwargs()

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
) -> ResponseDTOConsumerDTO | None:
    """Get Currently Logged Consumer

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ResponseDTOConsumerDTO
    """

    return sync_detailed(
        client=client,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
) -> Response[ResponseDTOConsumerDTO]:
    """Get Currently Logged Consumer

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ResponseDTOConsumerDTO]
    """

    kwargs = _get_kwargs()

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
) -> ResponseDTOConsumerDTO | None:
    """Get Currently Logged Consumer

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ResponseDTOConsumerDTO
    """

    return (
        await asyncio_detailed(
            client=client,
        )
    ).parsed
