from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.list_bookings_order_by import ListBookingsOrderBy
from ...models.scaleway_qaas_v1_alpha_1_list_bookings_response import (
    ScalewayQaasV1Alpha1ListBookingsResponse,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    project_id: Union[Unset, str] = UNSET,
    platform_id: Union[Unset, str] = UNSET,
    page: Union[Unset, int] = UNSET,
    page_size: Union[Unset, int] = UNSET,
    order_by: Union[Unset, ListBookingsOrderBy] = ListBookingsOrderBy.CREATED_AT_DESC,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["project_id"] = project_id

    params["platform_id"] = platform_id

    params["page"] = page

    params["page_size"] = page_size

    json_order_by: Union[Unset, str] = UNSET
    if not isinstance(order_by, Unset):
        json_order_by = order_by.value

    params["order_by"] = json_order_by

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/qaas/v1alpha1/bookings",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[ScalewayQaasV1Alpha1ListBookingsResponse]:
    if response.status_code == 200:
        response_200 = ScalewayQaasV1Alpha1ListBookingsResponse.from_dict(
            response.json()
        )

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[ScalewayQaasV1Alpha1ListBookingsResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    project_id: Union[Unset, str] = UNSET,
    platform_id: Union[Unset, str] = UNSET,
    page: Union[Unset, int] = UNSET,
    page_size: Union[Unset, int] = UNSET,
    order_by: Union[Unset, ListBookingsOrderBy] = ListBookingsOrderBy.CREATED_AT_DESC,
) -> Response[ScalewayQaasV1Alpha1ListBookingsResponse]:
    """List all bookings according the filter

     Retrieve information about all bookings of the provided **project ID** or ** platform ID**.

    Args:
        project_id (Union[Unset, str]): List bookings belonging to this project ID. (UUID format)
            Example: 6170692e-7363-616c-6577-61792e636f6d.
        platform_id (Union[Unset, str]): List bookings attached to this platform ID.
        page (Union[Unset, int]): Page number.
        page_size (Union[Unset, int]): Maximum number of results to return per page.
        order_by (Union[Unset, ListBookingsOrderBy]): Sort order of the returned results. Default:
            ListBookingsOrderBy.CREATED_AT_DESC.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ScalewayQaasV1Alpha1ListBookingsResponse]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        platform_id=platform_id,
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
    project_id: Union[Unset, str] = UNSET,
    platform_id: Union[Unset, str] = UNSET,
    page: Union[Unset, int] = UNSET,
    page_size: Union[Unset, int] = UNSET,
    order_by: Union[Unset, ListBookingsOrderBy] = ListBookingsOrderBy.CREATED_AT_DESC,
) -> Optional[ScalewayQaasV1Alpha1ListBookingsResponse]:
    """List all bookings according the filter

     Retrieve information about all bookings of the provided **project ID** or ** platform ID**.

    Args:
        project_id (Union[Unset, str]): List bookings belonging to this project ID. (UUID format)
            Example: 6170692e-7363-616c-6577-61792e636f6d.
        platform_id (Union[Unset, str]): List bookings attached to this platform ID.
        page (Union[Unset, int]): Page number.
        page_size (Union[Unset, int]): Maximum number of results to return per page.
        order_by (Union[Unset, ListBookingsOrderBy]): Sort order of the returned results. Default:
            ListBookingsOrderBy.CREATED_AT_DESC.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ScalewayQaasV1Alpha1ListBookingsResponse
    """

    return sync_detailed(
        client=client,
        project_id=project_id,
        platform_id=platform_id,
        page=page,
        page_size=page_size,
        order_by=order_by,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    project_id: Union[Unset, str] = UNSET,
    platform_id: Union[Unset, str] = UNSET,
    page: Union[Unset, int] = UNSET,
    page_size: Union[Unset, int] = UNSET,
    order_by: Union[Unset, ListBookingsOrderBy] = ListBookingsOrderBy.CREATED_AT_DESC,
) -> Response[ScalewayQaasV1Alpha1ListBookingsResponse]:
    """List all bookings according the filter

     Retrieve information about all bookings of the provided **project ID** or ** platform ID**.

    Args:
        project_id (Union[Unset, str]): List bookings belonging to this project ID. (UUID format)
            Example: 6170692e-7363-616c-6577-61792e636f6d.
        platform_id (Union[Unset, str]): List bookings attached to this platform ID.
        page (Union[Unset, int]): Page number.
        page_size (Union[Unset, int]): Maximum number of results to return per page.
        order_by (Union[Unset, ListBookingsOrderBy]): Sort order of the returned results. Default:
            ListBookingsOrderBy.CREATED_AT_DESC.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ScalewayQaasV1Alpha1ListBookingsResponse]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        platform_id=platform_id,
        page=page,
        page_size=page_size,
        order_by=order_by,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    project_id: Union[Unset, str] = UNSET,
    platform_id: Union[Unset, str] = UNSET,
    page: Union[Unset, int] = UNSET,
    page_size: Union[Unset, int] = UNSET,
    order_by: Union[Unset, ListBookingsOrderBy] = ListBookingsOrderBy.CREATED_AT_DESC,
) -> Optional[ScalewayQaasV1Alpha1ListBookingsResponse]:
    """List all bookings according the filter

     Retrieve information about all bookings of the provided **project ID** or ** platform ID**.

    Args:
        project_id (Union[Unset, str]): List bookings belonging to this project ID. (UUID format)
            Example: 6170692e-7363-616c-6577-61792e636f6d.
        platform_id (Union[Unset, str]): List bookings attached to this platform ID.
        page (Union[Unset, int]): Page number.
        page_size (Union[Unset, int]): Maximum number of results to return per page.
        order_by (Union[Unset, ListBookingsOrderBy]): Sort order of the returned results. Default:
            ListBookingsOrderBy.CREATED_AT_DESC.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ScalewayQaasV1Alpha1ListBookingsResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            project_id=project_id,
            platform_id=platform_id,
            page=page,
            page_size=page_size,
            order_by=order_by,
        )
    ).parsed
