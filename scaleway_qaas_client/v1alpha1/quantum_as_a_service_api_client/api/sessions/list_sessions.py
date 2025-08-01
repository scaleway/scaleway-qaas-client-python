from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.list_sessions_order_by import ListSessionsOrderBy
from ...models.scaleway_qaas_v1_alpha_1_list_sessions_response import (
    ScalewayQaasV1Alpha1ListSessionsResponse,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    platform_id: Union[Unset, str] = UNSET,
    tags: Union[Unset, list[str]] = UNSET,
    page: Union[Unset, int] = UNSET,
    page_size: Union[Unset, int] = UNSET,
    order_by: Union[Unset, ListSessionsOrderBy] = ListSessionsOrderBy.NAME_ASC,
    project_id: str,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["platform_id"] = platform_id

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
        "url": "/qaas/v1alpha1/sessions",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[ScalewayQaasV1Alpha1ListSessionsResponse]:
    if response.status_code == 200:
        response_200 = ScalewayQaasV1Alpha1ListSessionsResponse.from_dict(
            response.json()
        )

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[ScalewayQaasV1Alpha1ListSessionsResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    platform_id: Union[Unset, str] = UNSET,
    tags: Union[Unset, list[str]] = UNSET,
    page: Union[Unset, int] = UNSET,
    page_size: Union[Unset, int] = UNSET,
    order_by: Union[Unset, ListSessionsOrderBy] = ListSessionsOrderBy.NAME_ASC,
    project_id: str,
) -> Response[ScalewayQaasV1Alpha1ListSessionsResponse]:
    """List all sessions

     Retrieve information about all sessions.

    Args:
        platform_id (Union[Unset, str]): List sessions that have been created for this platform.
        tags (Union[Unset, list[str]]): List sessions with these tags.
        page (Union[Unset, int]): Page number.
        page_size (Union[Unset, int]): Maximum number of sessions to return per page.
        order_by (Union[Unset, ListSessionsOrderBy]): Sort order of the returned sessions.
            Default: ListSessionsOrderBy.NAME_ASC.
        project_id (str): List sessions belonging to this project ID. (UUID format) Example:
            6170692e-7363-616c-6577-61792e636f6d.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ScalewayQaasV1Alpha1ListSessionsResponse]
    """

    kwargs = _get_kwargs(
        platform_id=platform_id,
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
    platform_id: Union[Unset, str] = UNSET,
    tags: Union[Unset, list[str]] = UNSET,
    page: Union[Unset, int] = UNSET,
    page_size: Union[Unset, int] = UNSET,
    order_by: Union[Unset, ListSessionsOrderBy] = ListSessionsOrderBy.NAME_ASC,
    project_id: str,
) -> Optional[ScalewayQaasV1Alpha1ListSessionsResponse]:
    """List all sessions

     Retrieve information about all sessions.

    Args:
        platform_id (Union[Unset, str]): List sessions that have been created for this platform.
        tags (Union[Unset, list[str]]): List sessions with these tags.
        page (Union[Unset, int]): Page number.
        page_size (Union[Unset, int]): Maximum number of sessions to return per page.
        order_by (Union[Unset, ListSessionsOrderBy]): Sort order of the returned sessions.
            Default: ListSessionsOrderBy.NAME_ASC.
        project_id (str): List sessions belonging to this project ID. (UUID format) Example:
            6170692e-7363-616c-6577-61792e636f6d.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ScalewayQaasV1Alpha1ListSessionsResponse
    """

    return sync_detailed(
        client=client,
        platform_id=platform_id,
        tags=tags,
        page=page,
        page_size=page_size,
        order_by=order_by,
        project_id=project_id,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    platform_id: Union[Unset, str] = UNSET,
    tags: Union[Unset, list[str]] = UNSET,
    page: Union[Unset, int] = UNSET,
    page_size: Union[Unset, int] = UNSET,
    order_by: Union[Unset, ListSessionsOrderBy] = ListSessionsOrderBy.NAME_ASC,
    project_id: str,
) -> Response[ScalewayQaasV1Alpha1ListSessionsResponse]:
    """List all sessions

     Retrieve information about all sessions.

    Args:
        platform_id (Union[Unset, str]): List sessions that have been created for this platform.
        tags (Union[Unset, list[str]]): List sessions with these tags.
        page (Union[Unset, int]): Page number.
        page_size (Union[Unset, int]): Maximum number of sessions to return per page.
        order_by (Union[Unset, ListSessionsOrderBy]): Sort order of the returned sessions.
            Default: ListSessionsOrderBy.NAME_ASC.
        project_id (str): List sessions belonging to this project ID. (UUID format) Example:
            6170692e-7363-616c-6577-61792e636f6d.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ScalewayQaasV1Alpha1ListSessionsResponse]
    """

    kwargs = _get_kwargs(
        platform_id=platform_id,
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
    platform_id: Union[Unset, str] = UNSET,
    tags: Union[Unset, list[str]] = UNSET,
    page: Union[Unset, int] = UNSET,
    page_size: Union[Unset, int] = UNSET,
    order_by: Union[Unset, ListSessionsOrderBy] = ListSessionsOrderBy.NAME_ASC,
    project_id: str,
) -> Optional[ScalewayQaasV1Alpha1ListSessionsResponse]:
    """List all sessions

     Retrieve information about all sessions.

    Args:
        platform_id (Union[Unset, str]): List sessions that have been created for this platform.
        tags (Union[Unset, list[str]]): List sessions with these tags.
        page (Union[Unset, int]): Page number.
        page_size (Union[Unset, int]): Maximum number of sessions to return per page.
        order_by (Union[Unset, ListSessionsOrderBy]): Sort order of the returned sessions.
            Default: ListSessionsOrderBy.NAME_ASC.
        project_id (str): List sessions belonging to this project ID. (UUID format) Example:
            6170692e-7363-616c-6577-61792e636f6d.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ScalewayQaasV1Alpha1ListSessionsResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            platform_id=platform_id,
            tags=tags,
            page=page,
            page_size=page_size,
            order_by=order_by,
            project_id=project_id,
        )
    ).parsed
