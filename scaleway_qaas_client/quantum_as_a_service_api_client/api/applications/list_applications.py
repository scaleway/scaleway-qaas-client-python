from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.list_applications_application_type import ListApplicationsApplicationType
from ...models.list_applications_order_by import ListApplicationsOrderBy
from ...models.scaleway_qaas_v1_alpha_1_list_applications_response import (
    ScalewayQaasV1Alpha1ListApplicationsResponse,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    name: Union[Unset, str] = UNSET,
    application_type: Union[
        Unset, ListApplicationsApplicationType
    ] = ListApplicationsApplicationType.UNKNOWN_TYPE,
    page: Union[Unset, int] = UNSET,
    page_size: Union[Unset, int] = UNSET,
    order_by: Union[Unset, ListApplicationsOrderBy] = ListApplicationsOrderBy.NAME_ASC,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["name"] = name

    json_application_type: Union[Unset, str] = UNSET
    if not isinstance(application_type, Unset):
        json_application_type = application_type.value

    params["application_type"] = json_application_type

    params["page"] = page

    params["page_size"] = page_size

    json_order_by: Union[Unset, str] = UNSET
    if not isinstance(order_by, Unset):
        json_order_by = order_by.value

    params["order_by"] = json_order_by

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/qaas/v1alpha1/applications",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[ScalewayQaasV1Alpha1ListApplicationsResponse]:
    if response.status_code == 200:
        response_200 = ScalewayQaasV1Alpha1ListApplicationsResponse.from_dict(
            response.json()
        )

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[ScalewayQaasV1Alpha1ListApplicationsResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    name: Union[Unset, str] = UNSET,
    application_type: Union[
        Unset, ListApplicationsApplicationType
    ] = ListApplicationsApplicationType.UNKNOWN_TYPE,
    page: Union[Unset, int] = UNSET,
    page_size: Union[Unset, int] = UNSET,
    order_by: Union[Unset, ListApplicationsOrderBy] = ListApplicationsOrderBy.NAME_ASC,
) -> Response[ScalewayQaasV1Alpha1ListApplicationsResponse]:
    """List all available applications

     Retrieve information about all applications.

    Args:
        name (Union[Unset, str]): List applications with this name.
        application_type (Union[Unset, ListApplicationsApplicationType]): List applications with
            this type. Default: ListApplicationsApplicationType.UNKNOWN_TYPE.
        page (Union[Unset, int]): Page number.
        page_size (Union[Unset, int]): Maximum number of applications a to return per page.
        order_by (Union[Unset, ListApplicationsOrderBy]): Sort order of the returned applications.
            Default: ListApplicationsOrderBy.NAME_ASC.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ScalewayQaasV1Alpha1ListApplicationsResponse]
    """

    kwargs = _get_kwargs(
        name=name,
        application_type=application_type,
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
    name: Union[Unset, str] = UNSET,
    application_type: Union[
        Unset, ListApplicationsApplicationType
    ] = ListApplicationsApplicationType.UNKNOWN_TYPE,
    page: Union[Unset, int] = UNSET,
    page_size: Union[Unset, int] = UNSET,
    order_by: Union[Unset, ListApplicationsOrderBy] = ListApplicationsOrderBy.NAME_ASC,
) -> Optional[ScalewayQaasV1Alpha1ListApplicationsResponse]:
    """List all available applications

     Retrieve information about all applications.

    Args:
        name (Union[Unset, str]): List applications with this name.
        application_type (Union[Unset, ListApplicationsApplicationType]): List applications with
            this type. Default: ListApplicationsApplicationType.UNKNOWN_TYPE.
        page (Union[Unset, int]): Page number.
        page_size (Union[Unset, int]): Maximum number of applications a to return per page.
        order_by (Union[Unset, ListApplicationsOrderBy]): Sort order of the returned applications.
            Default: ListApplicationsOrderBy.NAME_ASC.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ScalewayQaasV1Alpha1ListApplicationsResponse
    """

    return sync_detailed(
        client=client,
        name=name,
        application_type=application_type,
        page=page,
        page_size=page_size,
        order_by=order_by,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    name: Union[Unset, str] = UNSET,
    application_type: Union[
        Unset, ListApplicationsApplicationType
    ] = ListApplicationsApplicationType.UNKNOWN_TYPE,
    page: Union[Unset, int] = UNSET,
    page_size: Union[Unset, int] = UNSET,
    order_by: Union[Unset, ListApplicationsOrderBy] = ListApplicationsOrderBy.NAME_ASC,
) -> Response[ScalewayQaasV1Alpha1ListApplicationsResponse]:
    """List all available applications

     Retrieve information about all applications.

    Args:
        name (Union[Unset, str]): List applications with this name.
        application_type (Union[Unset, ListApplicationsApplicationType]): List applications with
            this type. Default: ListApplicationsApplicationType.UNKNOWN_TYPE.
        page (Union[Unset, int]): Page number.
        page_size (Union[Unset, int]): Maximum number of applications a to return per page.
        order_by (Union[Unset, ListApplicationsOrderBy]): Sort order of the returned applications.
            Default: ListApplicationsOrderBy.NAME_ASC.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ScalewayQaasV1Alpha1ListApplicationsResponse]
    """

    kwargs = _get_kwargs(
        name=name,
        application_type=application_type,
        page=page,
        page_size=page_size,
        order_by=order_by,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    name: Union[Unset, str] = UNSET,
    application_type: Union[
        Unset, ListApplicationsApplicationType
    ] = ListApplicationsApplicationType.UNKNOWN_TYPE,
    page: Union[Unset, int] = UNSET,
    page_size: Union[Unset, int] = UNSET,
    order_by: Union[Unset, ListApplicationsOrderBy] = ListApplicationsOrderBy.NAME_ASC,
) -> Optional[ScalewayQaasV1Alpha1ListApplicationsResponse]:
    """List all available applications

     Retrieve information about all applications.

    Args:
        name (Union[Unset, str]): List applications with this name.
        application_type (Union[Unset, ListApplicationsApplicationType]): List applications with
            this type. Default: ListApplicationsApplicationType.UNKNOWN_TYPE.
        page (Union[Unset, int]): Page number.
        page_size (Union[Unset, int]): Maximum number of applications a to return per page.
        order_by (Union[Unset, ListApplicationsOrderBy]): Sort order of the returned applications.
            Default: ListApplicationsOrderBy.NAME_ASC.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ScalewayQaasV1Alpha1ListApplicationsResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            name=name,
            application_type=application_type,
            page=page,
            page_size=page_size,
            order_by=order_by,
        )
    ).parsed
