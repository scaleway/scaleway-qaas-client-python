from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.list_platforms_order_by import ListPlatformsOrderBy
from ...models.list_platforms_platform_technology import ListPlatformsPlatformTechnology
from ...models.list_platforms_platform_type import ListPlatformsPlatformType
from ...models.scaleway_qaas_v1_alpha_1_list_platforms_response import (
    ScalewayQaasV1Alpha1ListPlatformsResponse,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    provider_name: Union[Unset, str] = UNSET,
    backend_name: Union[Unset, str] = UNSET,
    name: Union[Unset, str] = UNSET,
    platform_type: Union[
        Unset, ListPlatformsPlatformType
    ] = ListPlatformsPlatformType.UNKNOWN_TYPE,
    platform_technology: Union[
        Unset, ListPlatformsPlatformTechnology
    ] = ListPlatformsPlatformTechnology.UNKNOWN_TECHNOLOGY,
    page: Union[Unset, int] = UNSET,
    page_size: Union[Unset, int] = UNSET,
    order_by: Union[Unset, ListPlatformsOrderBy] = ListPlatformsOrderBy.NAME_ASC,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["provider_name"] = provider_name

    params["backend_name"] = backend_name

    params["name"] = name

    json_platform_type: Union[Unset, str] = UNSET
    if not isinstance(platform_type, Unset):
        json_platform_type = platform_type.value

    params["platform_type"] = json_platform_type

    json_platform_technology: Union[Unset, str] = UNSET
    if not isinstance(platform_technology, Unset):
        json_platform_technology = platform_technology.value

    params["platform_technology"] = json_platform_technology

    params["page"] = page

    params["page_size"] = page_size

    json_order_by: Union[Unset, str] = UNSET
    if not isinstance(order_by, Unset):
        json_order_by = order_by.value

    params["order_by"] = json_order_by

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/qaas/v1alpha1/platforms",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[ScalewayQaasV1Alpha1ListPlatformsResponse]:
    if response.status_code == 200:
        response_200 = ScalewayQaasV1Alpha1ListPlatformsResponse.from_dict(
            response.json()
        )

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[ScalewayQaasV1Alpha1ListPlatformsResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    provider_name: Union[Unset, str] = UNSET,
    backend_name: Union[Unset, str] = UNSET,
    name: Union[Unset, str] = UNSET,
    platform_type: Union[
        Unset, ListPlatformsPlatformType
    ] = ListPlatformsPlatformType.UNKNOWN_TYPE,
    platform_technology: Union[
        Unset, ListPlatformsPlatformTechnology
    ] = ListPlatformsPlatformTechnology.UNKNOWN_TECHNOLOGY,
    page: Union[Unset, int] = UNSET,
    page_size: Union[Unset, int] = UNSET,
    order_by: Union[Unset, ListPlatformsOrderBy] = ListPlatformsOrderBy.NAME_ASC,
) -> Response[ScalewayQaasV1Alpha1ListPlatformsResponse]:
    """List all available platforms

     Retrieve information about all platforms.

    Args:
        provider_name (Union[Unset, str]): List platforms with this provider name.
        backend_name (Union[Unset, str]): List platforms with this backend name.
        name (Union[Unset, str]): List platforms with this name.
        platform_type (Union[Unset, ListPlatformsPlatformType]): List platforms with this type.
            Default: ListPlatformsPlatformType.UNKNOWN_TYPE.
        platform_technology (Union[Unset, ListPlatformsPlatformTechnology]): List platforms with
            this technology. Default: ListPlatformsPlatformTechnology.UNKNOWN_TECHNOLOGY.
        page (Union[Unset, int]): Page number.
        page_size (Union[Unset, int]): Maximum number of platforms to return per page.
        order_by (Union[Unset, ListPlatformsOrderBy]): Sort order of the returned platforms.
            Default: ListPlatformsOrderBy.NAME_ASC.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ScalewayQaasV1Alpha1ListPlatformsResponse]
    """

    kwargs = _get_kwargs(
        provider_name=provider_name,
        backend_name=backend_name,
        name=name,
        platform_type=platform_type,
        platform_technology=platform_technology,
        page=page,
        page_size=page_size,
        order_by=order_by,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    provider_name: Union[Unset, str] = UNSET,
    backend_name: Union[Unset, str] = UNSET,
    name: Union[Unset, str] = UNSET,
    platform_type: Union[
        Unset, ListPlatformsPlatformType
    ] = ListPlatformsPlatformType.UNKNOWN_TYPE,
    platform_technology: Union[
        Unset, ListPlatformsPlatformTechnology
    ] = ListPlatformsPlatformTechnology.UNKNOWN_TECHNOLOGY,
    page: Union[Unset, int] = UNSET,
    page_size: Union[Unset, int] = UNSET,
    order_by: Union[Unset, ListPlatformsOrderBy] = ListPlatformsOrderBy.NAME_ASC,
) -> Optional[ScalewayQaasV1Alpha1ListPlatformsResponse]:
    """List all available platforms

     Retrieve information about all platforms.

    Args:
        provider_name (Union[Unset, str]): List platforms with this provider name.
        backend_name (Union[Unset, str]): List platforms with this backend name.
        name (Union[Unset, str]): List platforms with this name.
        platform_type (Union[Unset, ListPlatformsPlatformType]): List platforms with this type.
            Default: ListPlatformsPlatformType.UNKNOWN_TYPE.
        platform_technology (Union[Unset, ListPlatformsPlatformTechnology]): List platforms with
            this technology. Default: ListPlatformsPlatformTechnology.UNKNOWN_TECHNOLOGY.
        page (Union[Unset, int]): Page number.
        page_size (Union[Unset, int]): Maximum number of platforms to return per page.
        order_by (Union[Unset, ListPlatformsOrderBy]): Sort order of the returned platforms.
            Default: ListPlatformsOrderBy.NAME_ASC.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ScalewayQaasV1Alpha1ListPlatformsResponse
    """

    return sync_detailed(
        client=client,
        provider_name=provider_name,
        backend_name=backend_name,
        name=name,
        platform_type=platform_type,
        platform_technology=platform_technology,
        page=page,
        page_size=page_size,
        order_by=order_by,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    provider_name: Union[Unset, str] = UNSET,
    backend_name: Union[Unset, str] = UNSET,
    name: Union[Unset, str] = UNSET,
    platform_type: Union[
        Unset, ListPlatformsPlatformType
    ] = ListPlatformsPlatformType.UNKNOWN_TYPE,
    platform_technology: Union[
        Unset, ListPlatformsPlatformTechnology
    ] = ListPlatformsPlatformTechnology.UNKNOWN_TECHNOLOGY,
    page: Union[Unset, int] = UNSET,
    page_size: Union[Unset, int] = UNSET,
    order_by: Union[Unset, ListPlatformsOrderBy] = ListPlatformsOrderBy.NAME_ASC,
) -> Response[ScalewayQaasV1Alpha1ListPlatformsResponse]:
    """List all available platforms

     Retrieve information about all platforms.

    Args:
        provider_name (Union[Unset, str]): List platforms with this provider name.
        backend_name (Union[Unset, str]): List platforms with this backend name.
        name (Union[Unset, str]): List platforms with this name.
        platform_type (Union[Unset, ListPlatformsPlatformType]): List platforms with this type.
            Default: ListPlatformsPlatformType.UNKNOWN_TYPE.
        platform_technology (Union[Unset, ListPlatformsPlatformTechnology]): List platforms with
            this technology. Default: ListPlatformsPlatformTechnology.UNKNOWN_TECHNOLOGY.
        page (Union[Unset, int]): Page number.
        page_size (Union[Unset, int]): Maximum number of platforms to return per page.
        order_by (Union[Unset, ListPlatformsOrderBy]): Sort order of the returned platforms.
            Default: ListPlatformsOrderBy.NAME_ASC.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ScalewayQaasV1Alpha1ListPlatformsResponse]
    """

    kwargs = _get_kwargs(
        provider_name=provider_name,
        backend_name=backend_name,
        name=name,
        platform_type=platform_type,
        platform_technology=platform_technology,
        page=page,
        page_size=page_size,
        order_by=order_by,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    provider_name: Union[Unset, str] = UNSET,
    backend_name: Union[Unset, str] = UNSET,
    name: Union[Unset, str] = UNSET,
    platform_type: Union[
        Unset, ListPlatformsPlatformType
    ] = ListPlatformsPlatformType.UNKNOWN_TYPE,
    platform_technology: Union[
        Unset, ListPlatformsPlatformTechnology
    ] = ListPlatformsPlatformTechnology.UNKNOWN_TECHNOLOGY,
    page: Union[Unset, int] = UNSET,
    page_size: Union[Unset, int] = UNSET,
    order_by: Union[Unset, ListPlatformsOrderBy] = ListPlatformsOrderBy.NAME_ASC,
) -> Optional[ScalewayQaasV1Alpha1ListPlatformsResponse]:
    """List all available platforms

     Retrieve information about all platforms.

    Args:
        provider_name (Union[Unset, str]): List platforms with this provider name.
        backend_name (Union[Unset, str]): List platforms with this backend name.
        name (Union[Unset, str]): List platforms with this name.
        platform_type (Union[Unset, ListPlatformsPlatformType]): List platforms with this type.
            Default: ListPlatformsPlatformType.UNKNOWN_TYPE.
        platform_technology (Union[Unset, ListPlatformsPlatformTechnology]): List platforms with
            this technology. Default: ListPlatformsPlatformTechnology.UNKNOWN_TECHNOLOGY.
        page (Union[Unset, int]): Page number.
        page_size (Union[Unset, int]): Maximum number of platforms to return per page.
        order_by (Union[Unset, ListPlatformsOrderBy]): Sort order of the returned platforms.
            Default: ListPlatformsOrderBy.NAME_ASC.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ScalewayQaasV1Alpha1ListPlatformsResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            provider_name=provider_name,
            backend_name=backend_name,
            name=name,
            platform_type=platform_type,
            platform_technology=platform_technology,
            page=page,
            page_size=page_size,
            order_by=order_by,
        )
    ).parsed
