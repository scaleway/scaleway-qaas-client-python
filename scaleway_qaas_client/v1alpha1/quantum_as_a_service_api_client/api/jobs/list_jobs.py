from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.list_jobs_order_by import ListJobsOrderBy
from ...models.scaleway_qaas_v1_alpha_1_list_jobs_response import (
    ScalewayQaasV1Alpha1ListJobsResponse,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    tags: Union[Unset, list[str]] = UNSET,
    page: Union[Unset, int] = UNSET,
    page_size: Union[Unset, int] = UNSET,
    order_by: Union[Unset, ListJobsOrderBy] = ListJobsOrderBy.CREATED_AT_DESC,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

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

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/qaas/v1alpha1/jobs",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[ScalewayQaasV1Alpha1ListJobsResponse]:
    if response.status_code == 200:
        response_200 = ScalewayQaasV1Alpha1ListJobsResponse.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[ScalewayQaasV1Alpha1ListJobsResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    tags: Union[Unset, list[str]] = UNSET,
    page: Union[Unset, int] = UNSET,
    page_size: Union[Unset, int] = UNSET,
    order_by: Union[Unset, ListJobsOrderBy] = ListJobsOrderBy.CREATED_AT_DESC,
) -> Response[ScalewayQaasV1Alpha1ListJobsResponse]:
    """List all jobs within a project or session

     Retrieve information about all jobs within a given project or session.

    Args:
        tags (Union[Unset, list[str]]): List jobs with these tags.
        page (Union[Unset, int]): Page number.
        page_size (Union[Unset, int]): Maximum number of jobs to return per page.
        order_by (Union[Unset, ListJobsOrderBy]): Sort order of the returned jobs. Default:
            ListJobsOrderBy.CREATED_AT_DESC.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ScalewayQaasV1Alpha1ListJobsResponse]
    """

    kwargs = _get_kwargs(
        tags=tags,
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
    tags: Union[Unset, list[str]] = UNSET,
    page: Union[Unset, int] = UNSET,
    page_size: Union[Unset, int] = UNSET,
    order_by: Union[Unset, ListJobsOrderBy] = ListJobsOrderBy.CREATED_AT_DESC,
) -> Optional[ScalewayQaasV1Alpha1ListJobsResponse]:
    """List all jobs within a project or session

     Retrieve information about all jobs within a given project or session.

    Args:
        tags (Union[Unset, list[str]]): List jobs with these tags.
        page (Union[Unset, int]): Page number.
        page_size (Union[Unset, int]): Maximum number of jobs to return per page.
        order_by (Union[Unset, ListJobsOrderBy]): Sort order of the returned jobs. Default:
            ListJobsOrderBy.CREATED_AT_DESC.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ScalewayQaasV1Alpha1ListJobsResponse
    """

    return sync_detailed(
        client=client,
        tags=tags,
        page=page,
        page_size=page_size,
        order_by=order_by,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    tags: Union[Unset, list[str]] = UNSET,
    page: Union[Unset, int] = UNSET,
    page_size: Union[Unset, int] = UNSET,
    order_by: Union[Unset, ListJobsOrderBy] = ListJobsOrderBy.CREATED_AT_DESC,
) -> Response[ScalewayQaasV1Alpha1ListJobsResponse]:
    """List all jobs within a project or session

     Retrieve information about all jobs within a given project or session.

    Args:
        tags (Union[Unset, list[str]]): List jobs with these tags.
        page (Union[Unset, int]): Page number.
        page_size (Union[Unset, int]): Maximum number of jobs to return per page.
        order_by (Union[Unset, ListJobsOrderBy]): Sort order of the returned jobs. Default:
            ListJobsOrderBy.CREATED_AT_DESC.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ScalewayQaasV1Alpha1ListJobsResponse]
    """

    kwargs = _get_kwargs(
        tags=tags,
        page=page,
        page_size=page_size,
        order_by=order_by,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    tags: Union[Unset, list[str]] = UNSET,
    page: Union[Unset, int] = UNSET,
    page_size: Union[Unset, int] = UNSET,
    order_by: Union[Unset, ListJobsOrderBy] = ListJobsOrderBy.CREATED_AT_DESC,
) -> Optional[ScalewayQaasV1Alpha1ListJobsResponse]:
    """List all jobs within a project or session

     Retrieve information about all jobs within a given project or session.

    Args:
        tags (Union[Unset, list[str]]): List jobs with these tags.
        page (Union[Unset, int]): Page number.
        page_size (Union[Unset, int]): Maximum number of jobs to return per page.
        order_by (Union[Unset, ListJobsOrderBy]): Sort order of the returned jobs. Default:
            ListJobsOrderBy.CREATED_AT_DESC.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ScalewayQaasV1Alpha1ListJobsResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            tags=tags,
            page=page,
            page_size=page_size,
            order_by=order_by,
        )
    ).parsed
