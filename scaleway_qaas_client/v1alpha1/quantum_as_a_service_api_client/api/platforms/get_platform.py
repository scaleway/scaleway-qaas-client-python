from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.scaleway_qaas_v1_alpha_1_platform import ScalewayQaasV1Alpha1Platform
from ...types import Response


def _get_kwargs(
    platform_id: str,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/qaas/v1alpha1/platforms/{platform_id}",
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[ScalewayQaasV1Alpha1Platform]:
    if response.status_code == 200:
        response_200 = ScalewayQaasV1Alpha1Platform.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[ScalewayQaasV1Alpha1Platform]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    platform_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[ScalewayQaasV1Alpha1Platform]:
    """Get platform information

     Retrieve information about the provided **platform ID**, such as provider name, technology, and
    type.

    Args:
        platform_id (str): Unique ID of the platform.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ScalewayQaasV1Alpha1Platform]
    """

    kwargs = _get_kwargs(
        platform_id=platform_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    platform_id: str,
    *,
    client: AuthenticatedClient,
) -> Optional[ScalewayQaasV1Alpha1Platform]:
    """Get platform information

     Retrieve information about the provided **platform ID**, such as provider name, technology, and
    type.

    Args:
        platform_id (str): Unique ID of the platform.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ScalewayQaasV1Alpha1Platform
    """

    return sync_detailed(
        platform_id=platform_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    platform_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[ScalewayQaasV1Alpha1Platform]:
    """Get platform information

     Retrieve information about the provided **platform ID**, such as provider name, technology, and
    type.

    Args:
        platform_id (str): Unique ID of the platform.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ScalewayQaasV1Alpha1Platform]
    """

    kwargs = _get_kwargs(
        platform_id=platform_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    platform_id: str,
    *,
    client: AuthenticatedClient,
) -> Optional[ScalewayQaasV1Alpha1Platform]:
    """Get platform information

     Retrieve information about the provided **platform ID**, such as provider name, technology, and
    type.

    Args:
        platform_id (str): Unique ID of the platform.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ScalewayQaasV1Alpha1Platform
    """

    return (
        await asyncio_detailed(
            platform_id=platform_id,
            client=client,
        )
    ).parsed
