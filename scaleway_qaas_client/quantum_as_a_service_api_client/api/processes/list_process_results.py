from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.list_process_results_order_by import ListProcessResultsOrderBy
from ...models.scaleway_qaas_v1_alpha_1_list_process_results_response import (
    ScalewayQaasV1Alpha1ListProcessResultsResponse,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    process_id: str,
    *,
    page: Union[Unset, int] = UNSET,
    page_size: Union[Unset, int] = UNSET,
    order_by: Union[
        Unset, ListProcessResultsOrderBy
    ] = ListProcessResultsOrderBy.CREATED_AT_DESC,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["page"] = page

    params["page_size"] = page_size

    json_order_by: Union[Unset, str] = UNSET
    if not isinstance(order_by, Unset):
        json_order_by = order_by.value

    params["order_by"] = json_order_by

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/qaas/v1alpha1/processes/{process_id}/results",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[ScalewayQaasV1Alpha1ListProcessResultsResponse]:
    if response.status_code == 200:
        response_200 = ScalewayQaasV1Alpha1ListProcessResultsResponse.from_dict(
            response.json()
        )

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[ScalewayQaasV1Alpha1ListProcessResultsResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    process_id: str,
    *,
    client: AuthenticatedClient,
    page: Union[Unset, int] = UNSET,
    page_size: Union[Unset, int] = UNSET,
    order_by: Union[
        Unset, ListProcessResultsOrderBy
    ] = ListProcessResultsOrderBy.CREATED_AT_DESC,
) -> Response[ScalewayQaasV1Alpha1ListProcessResultsResponse]:
    """List all results of a process

     Retrieve all intermediate and final result of a process.

    Args:
        process_id (str): ID of the process.
        page (Union[Unset, int]): Page number.
        page_size (Union[Unset, int]): Maximum number of results to return per page.
        order_by (Union[Unset, ListProcessResultsOrderBy]): Sort order of the returned results.
            Default: ListProcessResultsOrderBy.CREATED_AT_DESC.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ScalewayQaasV1Alpha1ListProcessResultsResponse]
    """

    kwargs = _get_kwargs(
        process_id=process_id,
        page=page,
        page_size=page_size,
        order_by=order_by,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    process_id: str,
    *,
    client: AuthenticatedClient,
    page: Union[Unset, int] = UNSET,
    page_size: Union[Unset, int] = UNSET,
    order_by: Union[
        Unset, ListProcessResultsOrderBy
    ] = ListProcessResultsOrderBy.CREATED_AT_DESC,
) -> Optional[ScalewayQaasV1Alpha1ListProcessResultsResponse]:
    """List all results of a process

     Retrieve all intermediate and final result of a process.

    Args:
        process_id (str): ID of the process.
        page (Union[Unset, int]): Page number.
        page_size (Union[Unset, int]): Maximum number of results to return per page.
        order_by (Union[Unset, ListProcessResultsOrderBy]): Sort order of the returned results.
            Default: ListProcessResultsOrderBy.CREATED_AT_DESC.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ScalewayQaasV1Alpha1ListProcessResultsResponse
    """

    return sync_detailed(
        process_id=process_id,
        client=client,
        page=page,
        page_size=page_size,
        order_by=order_by,
    ).parsed


async def asyncio_detailed(
    process_id: str,
    *,
    client: AuthenticatedClient,
    page: Union[Unset, int] = UNSET,
    page_size: Union[Unset, int] = UNSET,
    order_by: Union[
        Unset, ListProcessResultsOrderBy
    ] = ListProcessResultsOrderBy.CREATED_AT_DESC,
) -> Response[ScalewayQaasV1Alpha1ListProcessResultsResponse]:
    """List all results of a process

     Retrieve all intermediate and final result of a process.

    Args:
        process_id (str): ID of the process.
        page (Union[Unset, int]): Page number.
        page_size (Union[Unset, int]): Maximum number of results to return per page.
        order_by (Union[Unset, ListProcessResultsOrderBy]): Sort order of the returned results.
            Default: ListProcessResultsOrderBy.CREATED_AT_DESC.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ScalewayQaasV1Alpha1ListProcessResultsResponse]
    """

    kwargs = _get_kwargs(
        process_id=process_id,
        page=page,
        page_size=page_size,
        order_by=order_by,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    process_id: str,
    *,
    client: AuthenticatedClient,
    page: Union[Unset, int] = UNSET,
    page_size: Union[Unset, int] = UNSET,
    order_by: Union[
        Unset, ListProcessResultsOrderBy
    ] = ListProcessResultsOrderBy.CREATED_AT_DESC,
) -> Optional[ScalewayQaasV1Alpha1ListProcessResultsResponse]:
    """List all results of a process

     Retrieve all intermediate and final result of a process.

    Args:
        process_id (str): ID of the process.
        page (Union[Unset, int]): Page number.
        page_size (Union[Unset, int]): Maximum number of results to return per page.
        order_by (Union[Unset, ListProcessResultsOrderBy]): Sort order of the returned results.
            Default: ListProcessResultsOrderBy.CREATED_AT_DESC.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ScalewayQaasV1Alpha1ListProcessResultsResponse
    """

    return (
        await asyncio_detailed(
            process_id=process_id,
            client=client,
            page=page,
            page_size=page_size,
            order_by=order_by,
        )
    ).parsed
