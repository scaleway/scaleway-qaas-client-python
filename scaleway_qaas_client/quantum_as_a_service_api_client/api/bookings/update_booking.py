from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.scaleway_qaas_v1_alpha_1_booking import ScalewayQaasV1Alpha1Booking
from ...models.update_booking_body import UpdateBookingBody
from ...types import Response


def _get_kwargs(
    booking_id: str,
    *,
    body: UpdateBookingBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": f"/qaas/v1alpha1/bookings/{booking_id}",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[ScalewayQaasV1Alpha1Booking]:
    if response.status_code == 200:
        response_200 = ScalewayQaasV1Alpha1Booking.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[ScalewayQaasV1Alpha1Booking]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    booking_id: str,
    *,
    client: AuthenticatedClient,
    body: UpdateBookingBody,
) -> Response[ScalewayQaasV1Alpha1Booking]:
    """Update booking information

     Update booking information of the provided **booking ID**.

    Args:
        booking_id (str): Unique ID of the booking.
        body (UpdateBookingBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ScalewayQaasV1Alpha1Booking]
    """

    kwargs = _get_kwargs(
        booking_id=booking_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    booking_id: str,
    *,
    client: AuthenticatedClient,
    body: UpdateBookingBody,
) -> Optional[ScalewayQaasV1Alpha1Booking]:
    """Update booking information

     Update booking information of the provided **booking ID**.

    Args:
        booking_id (str): Unique ID of the booking.
        body (UpdateBookingBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ScalewayQaasV1Alpha1Booking
    """

    return sync_detailed(
        booking_id=booking_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    booking_id: str,
    *,
    client: AuthenticatedClient,
    body: UpdateBookingBody,
) -> Response[ScalewayQaasV1Alpha1Booking]:
    """Update booking information

     Update booking information of the provided **booking ID**.

    Args:
        booking_id (str): Unique ID of the booking.
        body (UpdateBookingBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ScalewayQaasV1Alpha1Booking]
    """

    kwargs = _get_kwargs(
        booking_id=booking_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    booking_id: str,
    *,
    client: AuthenticatedClient,
    body: UpdateBookingBody,
) -> Optional[ScalewayQaasV1Alpha1Booking]:
    """Update booking information

     Update booking information of the provided **booking ID**.

    Args:
        booking_id (str): Unique ID of the booking.
        body (UpdateBookingBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ScalewayQaasV1Alpha1Booking
    """

    return (
        await asyncio_detailed(
            booking_id=booking_id,
            client=client,
            body=body,
        )
    ).parsed
