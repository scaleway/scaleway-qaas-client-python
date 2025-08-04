from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.list_processes_order_by import ListProcessesOrderBy
from ...models.scaleway_qaas_v1_alpha_1_list_processes_response import (
    ScalewayQaasV1Alpha1ListProcessesResponse,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    application_id: Union[Unset, str] = UNSET,
    tags: Union[Unset, list[str]] = UNSET,
    page: Union[Unset, int] = UNSET,
    page_size: Union[Unset, int] = UNSET,
    order_by: Union[Unset, ListProcessesOrderBy] = ListProcessesOrderBy.CREATED_AT_DESC,
    project_id: str,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["application_id"] = application_id

    json_tags: Union[Unset, list[str]] = UNSET
    if not isinstance(tags, Unset):
        json_tags = tags

    params["tags"] = json_tags

    params["page"] = page

    params["page_size"] = page_size

    json_order_by: Union[Unset, str] = UNSET
    if not isinstance(order_by, Unset):
        json_order_by = order_by.value

    params["order_by"] = json_order_by

    params["project_id"] = project_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/qaas/v1alpha1/processes",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[ScalewayQaasV1Alpha1ListProcessesResponse]:
    if response.status_code == 200:
        response_200 = ScalewayQaasV1Alpha1ListProcessesResponse.from_dict(
            response.json()
        )

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[ScalewayQaasV1Alpha1ListProcessesResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    application_id: Union[Unset, str] = UNSET,
    tags: Union[Unset, list[str]] = UNSET,
    page: Union[Unset, int] = UNSET,
    page_size: Union[Unset, int] = UNSET,
    order_by: Union[Unset, ListProcessesOrderBy] = ListProcessesOrderBy.CREATED_AT_DESC,
    project_id: str,
) -> Response[ScalewayQaasV1Alpha1ListProcessesResponse]:
    """List all processes

     Retrieve information about all processes.

    Args:
        application_id (Union[Unset, str]): List processes that have been created for this
            application.
        tags (Union[Unset, list[str]]): List processes with these tags.
        page (Union[Unset, int]): Page number.
        page_size (Union[Unset, int]): Maximum number of processes to return per page.
        order_by (Union[Unset, ListProcessesOrderBy]): Sort order of the returned processes.
            Default: ListProcessesOrderBy.CREATED_AT_DESC.
        project_id (str): List processes belonging to this project ID. (UUID format) Example:
            6170692e-7363-616c-6577-61792e636f6d.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ScalewayQaasV1Alpha1ListProcessesResponse]
    """

    kwargs = _get_kwargs(
        application_id=application_id,
        tags=tags,
        page=page,
        page_size=page_size,
        order_by=order_by,
        project_id=project_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    application_id: Union[Unset, str] = UNSET,
    tags: Union[Unset, list[str]] = UNSET,
    page: Union[Unset, int] = UNSET,
    page_size: Union[Unset, int] = UNSET,
    order_by: Union[Unset, ListProcessesOrderBy] = ListProcessesOrderBy.CREATED_AT_DESC,
    project_id: str,
) -> Optional[ScalewayQaasV1Alpha1ListProcessesResponse]:
    """List all processes

     Retrieve information about all processes.

    Args:
        application_id (Union[Unset, str]): List processes that have been created for this
            application.
        tags (Union[Unset, list[str]]): List processes with these tags.
        page (Union[Unset, int]): Page number.
        page_size (Union[Unset, int]): Maximum number of processes to return per page.
        order_by (Union[Unset, ListProcessesOrderBy]): Sort order of the returned processes.
            Default: ListProcessesOrderBy.CREATED_AT_DESC.
        project_id (str): List processes belonging to this project ID. (UUID format) Example:
            6170692e-7363-616c-6577-61792e636f6d.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ScalewayQaasV1Alpha1ListProcessesResponse
    """

    return sync_detailed(
        client=client,
        application_id=application_id,
        tags=tags,
        page=page,
        page_size=page_size,
        order_by=order_by,
        project_id=project_id,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    application_id: Union[Unset, str] = UNSET,
    tags: Union[Unset, list[str]] = UNSET,
    page: Union[Unset, int] = UNSET,
    page_size: Union[Unset, int] = UNSET,
    order_by: Union[Unset, ListProcessesOrderBy] = ListProcessesOrderBy.CREATED_AT_DESC,
    project_id: str,
) -> Response[ScalewayQaasV1Alpha1ListProcessesResponse]:
    """List all processes

     Retrieve information about all processes.

    Args:
        application_id (Union[Unset, str]): List processes that have been created for this
            application.
        tags (Union[Unset, list[str]]): List processes with these tags.
        page (Union[Unset, int]): Page number.
        page_size (Union[Unset, int]): Maximum number of processes to return per page.
        order_by (Union[Unset, ListProcessesOrderBy]): Sort order of the returned processes.
            Default: ListProcessesOrderBy.CREATED_AT_DESC.
        project_id (str): List processes belonging to this project ID. (UUID format) Example:
            6170692e-7363-616c-6577-61792e636f6d.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ScalewayQaasV1Alpha1ListProcessesResponse]
    """

    kwargs = _get_kwargs(
        application_id=application_id,
        tags=tags,
        page=page,
        page_size=page_size,
        order_by=order_by,
        project_id=project_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    application_id: Union[Unset, str] = UNSET,
    tags: Union[Unset, list[str]] = UNSET,
    page: Union[Unset, int] = UNSET,
    page_size: Union[Unset, int] = UNSET,
    order_by: Union[Unset, ListProcessesOrderBy] = ListProcessesOrderBy.CREATED_AT_DESC,
    project_id: str,
) -> Optional[ScalewayQaasV1Alpha1ListProcessesResponse]:
    """List all processes

     Retrieve information about all processes.

    Args:
        application_id (Union[Unset, str]): List processes that have been created for this
            application.
        tags (Union[Unset, list[str]]): List processes with these tags.
        page (Union[Unset, int]): Page number.
        page_size (Union[Unset, int]): Maximum number of processes to return per page.
        order_by (Union[Unset, ListProcessesOrderBy]): Sort order of the returned processes.
            Default: ListProcessesOrderBy.CREATED_AT_DESC.
        project_id (str): List processes belonging to this project ID. (UUID format) Example:
            6170692e-7363-616c-6577-61792e636f6d.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ScalewayQaasV1Alpha1ListProcessesResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            application_id=application_id,
            tags=tags,
            page=page,
            page_size=page_size,
            order_by=order_by,
            project_id=project_id,
        )
    ).parsed
