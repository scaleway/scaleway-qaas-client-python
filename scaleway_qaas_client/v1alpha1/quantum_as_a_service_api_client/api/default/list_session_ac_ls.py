from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.scaleway_qaas_v1_alpha_1_list_session_ac_ls_request_order_by import (
    ScalewayQaasV1Alpha1ListSessionACLsRequestOrderBy,
)
from ...models.scaleway_qaas_v1_alpha_1_list_session_ac_ls_response import (
    ScalewayQaasV1Alpha1ListSessionACLsResponse,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    session_id: str,
    *,
    page: Union[None, Unset, int] = UNSET,
    page_size: Union[Unset, int] = UNSET,
    order_by: Union[Unset, ScalewayQaasV1Alpha1ListSessionACLsRequestOrderBy] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    json_page: Union[None, Unset, int]
    if isinstance(page, Unset):
        json_page = UNSET
    else:
        json_page = page
    params["page"] = json_page

    params["page_size"] = page_size

    json_order_by: Union[Unset, str] = UNSET
    if not isinstance(order_by, Unset):
        json_order_by = order_by.value

    params["order_by"] = json_order_by

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/qaas/v1alpha1/sessions/{session_id}/acls",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[ScalewayQaasV1Alpha1ListSessionACLsResponse]:
    if response.status_code == 200:
        response_200 = ScalewayQaasV1Alpha1ListSessionACLsResponse.from_dict(
            response.json()
        )

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[ScalewayQaasV1Alpha1ListSessionACLsResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    session_id: str,
    *,
    client: AuthenticatedClient,
    page: Union[None, Unset, int] = UNSET,
    page_size: Union[Unset, int] = UNSET,
    order_by: Union[Unset, ScalewayQaasV1Alpha1ListSessionACLsRequestOrderBy] = UNSET,
) -> Response[ScalewayQaasV1Alpha1ListSessionACLsResponse]:
    """
    Args:
        session_id (str):
        page (Union[None, Unset, int]):
        page_size (Union[Unset, int]):
        order_by (Union[Unset, ScalewayQaasV1Alpha1ListSessionACLsRequestOrderBy]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ScalewayQaasV1Alpha1ListSessionACLsResponse]
    """

    kwargs = _get_kwargs(
        session_id=session_id,
        page=page,
        page_size=page_size,
        order_by=order_by,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    session_id: str,
    *,
    client: AuthenticatedClient,
    page: Union[None, Unset, int] = UNSET,
    page_size: Union[Unset, int] = UNSET,
    order_by: Union[Unset, ScalewayQaasV1Alpha1ListSessionACLsRequestOrderBy] = UNSET,
) -> Optional[ScalewayQaasV1Alpha1ListSessionACLsResponse]:
    """
    Args:
        session_id (str):
        page (Union[None, Unset, int]):
        page_size (Union[Unset, int]):
        order_by (Union[Unset, ScalewayQaasV1Alpha1ListSessionACLsRequestOrderBy]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ScalewayQaasV1Alpha1ListSessionACLsResponse
    """

    return sync_detailed(
        session_id=session_id,
        client=client,
        page=page,
        page_size=page_size,
        order_by=order_by,
    ).parsed


async def asyncio_detailed(
    session_id: str,
    *,
    client: AuthenticatedClient,
    page: Union[None, Unset, int] = UNSET,
    page_size: Union[Unset, int] = UNSET,
    order_by: Union[Unset, ScalewayQaasV1Alpha1ListSessionACLsRequestOrderBy] = UNSET,
) -> Response[ScalewayQaasV1Alpha1ListSessionACLsResponse]:
    """
    Args:
        session_id (str):
        page (Union[None, Unset, int]):
        page_size (Union[Unset, int]):
        order_by (Union[Unset, ScalewayQaasV1Alpha1ListSessionACLsRequestOrderBy]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ScalewayQaasV1Alpha1ListSessionACLsResponse]
    """

    kwargs = _get_kwargs(
        session_id=session_id,
        page=page,
        page_size=page_size,
        order_by=order_by,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    session_id: str,
    *,
    client: AuthenticatedClient,
    page: Union[None, Unset, int] = UNSET,
    page_size: Union[Unset, int] = UNSET,
    order_by: Union[Unset, ScalewayQaasV1Alpha1ListSessionACLsRequestOrderBy] = UNSET,
) -> Optional[ScalewayQaasV1Alpha1ListSessionACLsResponse]:
    """
    Args:
        session_id (str):
        page (Union[None, Unset, int]):
        page_size (Union[Unset, int]):
        order_by (Union[Unset, ScalewayQaasV1Alpha1ListSessionACLsRequestOrderBy]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ScalewayQaasV1Alpha1ListSessionACLsResponse
    """

    return (
        await asyncio_detailed(
            session_id=session_id,
            client=client,
            page=page,
            page_size=page_size,
            order_by=order_by,
        )
    ).parsed
