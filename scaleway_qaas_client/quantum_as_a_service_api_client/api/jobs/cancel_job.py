from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.cancel_job_body import CancelJobBody
from ...models.scaleway_qaas_v1_alpha_1_job import ScalewayQaasV1Alpha1Job
from ...types import Response


def _get_kwargs(
    job_id: str,
    *,
    body: CancelJobBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": f"/qaas/v1alpha1/jobs/{job_id}/cancel",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[ScalewayQaasV1Alpha1Job]:
    if response.status_code == 200:
        response_200 = ScalewayQaasV1Alpha1Job.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[ScalewayQaasV1Alpha1Job]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    job_id: str,
    *,
    client: AuthenticatedClient,
    body: CancelJobBody,
) -> Response[ScalewayQaasV1Alpha1Job]:
    """Cancel a job

     Cancel the job corresponding to the provided **job ID**.

    Args:
        job_id (str): Unique ID of the job.
        body (CancelJobBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ScalewayQaasV1Alpha1Job]
    """

    kwargs = _get_kwargs(
        job_id=job_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    job_id: str,
    *,
    client: AuthenticatedClient,
    body: CancelJobBody,
) -> Optional[ScalewayQaasV1Alpha1Job]:
    """Cancel a job

     Cancel the job corresponding to the provided **job ID**.

    Args:
        job_id (str): Unique ID of the job.
        body (CancelJobBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ScalewayQaasV1Alpha1Job
    """

    return sync_detailed(
        job_id=job_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    job_id: str,
    *,
    client: AuthenticatedClient,
    body: CancelJobBody,
) -> Response[ScalewayQaasV1Alpha1Job]:
    """Cancel a job

     Cancel the job corresponding to the provided **job ID**.

    Args:
        job_id (str): Unique ID of the job.
        body (CancelJobBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ScalewayQaasV1Alpha1Job]
    """

    kwargs = _get_kwargs(
        job_id=job_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    job_id: str,
    *,
    client: AuthenticatedClient,
    body: CancelJobBody,
) -> Optional[ScalewayQaasV1Alpha1Job]:
    """Cancel a job

     Cancel the job corresponding to the provided **job ID**.

    Args:
        job_id (str): Unique ID of the job.
        body (CancelJobBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ScalewayQaasV1Alpha1Job
    """

    return (
        await asyncio_detailed(
            job_id=job_id,
            client=client,
            body=body,
        )
    ).parsed
