# Copyright 2025 Scaleway
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
import json
from typing import Dict, List, Optional, Union

import randomname
from pytimeparse.timeparse import timeparse

from scaleway_qaas_client.quantum_as_a_service_api_client.api.jobs.cancel_job import (
    sync_detailed as _cancel_job_sync,
)
from scaleway_qaas_client.quantum_as_a_service_api_client.api.jobs.create_job import (
    sync_detailed as _create_job_sync,
)
from scaleway_qaas_client.quantum_as_a_service_api_client.api.jobs.get_job import (
    sync_detailed as _get_job_sync,
)
from scaleway_qaas_client.quantum_as_a_service_api_client.api.jobs.list_job_results import (
    sync_detailed as _list_job_result_sync,
)
from scaleway_qaas_client.quantum_as_a_service_api_client.api.platforms.get_platform import (
    sync_detailed as _get_platform_sync,
)
from scaleway_qaas_client.quantum_as_a_service_api_client.api.platforms.list_platforms import (
    sync_detailed as _list_platforms_sync,
)
from scaleway_qaas_client.quantum_as_a_service_api_client.api.sessions.create_session import (
    sync_detailed as _create_session_sync,
)
from scaleway_qaas_client.quantum_as_a_service_api_client.api.sessions.delete_session import (
    sync_detailed as _delete_session_sync,
)
from scaleway_qaas_client.quantum_as_a_service_api_client.api.sessions.get_session import (
    sync_detailed as _get_session_sync,
)
from scaleway_qaas_client.quantum_as_a_service_api_client.api.sessions.list_sessions import (
    sync_detailed as _list_sessions_sync,
)
from scaleway_qaas_client.quantum_as_a_service_api_client.api.sessions.terminate_session import (
    sync_detailed as _terminate_session_sync,
)
from scaleway_qaas_client.quantum_as_a_service_api_client.client import (
    AuthenticatedClient,
)
from scaleway_qaas_client.quantum_as_a_service_api_client.models import (
    CancelJobBody,
    CreateJobBody,
    CreateJobBodyCircuit,
    CreateSessionBody,
    ScalewayQaasV1Alpha1Job,
    ScalewayQaasV1Alpha1JobResult,
    ScalewayQaasV1Alpha1Platform,
    ScalewayQaasV1Alpha1Session,
    TerminateSessionBody,
)
from scaleway_qaas_client.quantum_as_a_service_api_client.types import Response

_DEFAULT_URL = "https://api.scaleway.com"


def _raise_on_error(response: Response):
    if not response:
        raise Exception("error: None response")

    if response.status_code.is_server_error or response.status_code.is_client_error:
        raise Exception(
            f"error {response.status_code}: {response.content.decode('utf-8')}"
        )


class QaaSClient:
    def __init__(self, project_id: str, secret_key: str, url: str = _DEFAULT_URL):
        if not project_id:
            raise Exception("QaasClient: project_id cannot be None")

        if not secret_key:
            raise Exception("QaasClient: secret_key cannot be None")

        self.__project_id = project_id

        self.__client = AuthenticatedClient(
            base_url=url,
            timeout=10.0,
            verify_ssl="https" in url,
            token=secret_key,
            prefix=None,
            auth_header_name="X-Auth-Token",
        )

    def __repr__(self) -> str:
        return f"<QaaSClient(url={self.__client._base_url},project_id={self.__project_id})>"

    """Get platform information

     Retrieve information about the provided **platform ID**, such as provider name, technology, and
    type.

    Args:
        platform_id (str): Unique ID of the platform.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ScalewayQaasV1Alpha1Platform
    """

    def get_platform(self, platform_id: str) -> ScalewayQaasV1Alpha1Platform:
        if not platform_id:
            raise Exception("get_platform: platform_id cannot be None")

        response = _get_platform_sync(client=self.__client, platform_id=platform_id)

        _raise_on_error(response)

        return response.parsed

    """List all available platforms

     Retrieve information about all platforms.

    Args:
        name (Union[Unset, str]): List platforms with this name.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        List[ScalewayQaasV1Alpha1ListPlatforms]
    """

    def list_platforms(
        self, name: Optional[str] = None
    ) -> List[ScalewayQaasV1Alpha1Platform]:
        response = _list_platforms_sync(client=self.__client, name=name)

        _raise_on_error(response)

        return response.parsed.platforms

    """Create a session

     Create a dedicated session for the specified platform.

    Args:
        body (CreateSessionBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ScalewayQaasV1Alpha1Session
    """

    def create_session(
        self,
        platform_id: str,
        max_duration: Union[str, int],
        max_idle_duration: Union[str, int],
        deduplication_id: Optional[str] = None,
        name: Optional[str] = None,
    ) -> ScalewayQaasV1Alpha1Session:
        if not platform_id:
            raise Exception("create_session: platform_id cannot be None")

        name = name if name else f"qs-{randomname.get_name()}"

        if isinstance(max_duration, str):
            max_duration = f"{timeparse(max_duration)}s"

        if isinstance(max_idle_duration, str):
            max_idle_duration = f"{timeparse(max_idle_duration)}s"

        response = _create_session_sync(
            client=self.__client,
            body=CreateSessionBody(
                project_id=self.__project_id,
                name=name,
                platform_id=platform_id,
                deduplication_id=deduplication_id,
                max_duration=max_duration,
                max_idle_duration=max_idle_duration,
            ),
        )

        _raise_on_error(response)

        return response.parsed

    """Get session information

     Retrieve information about the provided **session ID**, such as name, status, and number of executed
    jobs.

    Args:
        session_id (str): Unique ID of the session.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ScalewayQaasV1Alpha1Session
    """

    def get_session(self, session_id: str) -> ScalewayQaasV1Alpha1Session:
        if not session_id:
            raise Exception("get_session: session_id cannot be None")

        response = _get_session_sync(client=self.__client, session_id=session_id)

        _raise_on_error(response)

        return response.parsed

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
        List[ScalewayQaasV1Alpha1ListSessionsResponse]
    """

    def list_sessions(
        self, platform_id: Optional[str] = None
    ) -> List[ScalewayQaasV1Alpha1Session]:
        if not platform_id:
            raise Exception("list_session: platform_id cannot be None")

        response = _list_sessions_sync(
            client=self.__client, project_id=self.__project_id, platform_id=platform_id
        )

        _raise_on_error(response)

        return response.parsed.sessions

    """Terminate an existing session

     Terminate a session by its unique ID and cancel all its attached jobs and booking.

    Args:
        session_id (str): Unique ID of the session.
        body (TerminateSessionBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ScalewayQaasV1Alpha1Session
    """

    def terminate_session(self, session_id: str) -> ScalewayQaasV1Alpha1Session:
        if not session_id:
            raise Exception("terminate_session: session_id cannot be None")

        response = _terminate_session_sync(
            client=self.__client,
            session_id=session_id,
            body=TerminateSessionBody(),
        )

        _raise_on_error(response)

        return response.parsed

    """Delete an existing session

     Delete a session by its unique ID and delete all its attached job and booking.

    Args:
        session_id (str): Unique ID of the session.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.
    """

    def delete_session(self, session_id: str):
        if not session_id:
            raise Exception("delete_session: session_id cannot be None")

        _delete_session_sync(client=self.__client, session_id=session_id)

    """Create a job

     Create a job to be executed inside a session.

    Args:
        body (CreateJobBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ScalewayQaasV1Alpha1Job
    """

    def create_job(
        self,
        session_id: str,
        payload: Union[Dict, List, str],
        name: Optional[str] = None,
    ) -> ScalewayQaasV1Alpha1Job:
        if not session_id:
            raise Exception("create_job: session_id cannot be None")

        if not payload:
            raise Exception("create_job: payload cannot be None")

        payload = payload if isinstance(payload, str) else json.dumps(payload)
        name = name if name else f"qj-{randomname.get_name()}"

        response = _create_job_sync(
            client=self.__client,
            body=CreateJobBody(
                name=name,
                session_id=session_id,
                circuit=CreateJobBodyCircuit(qiskit_circuit=payload),
            ),
        )

        _raise_on_error(response)

        return response.parsed

    """Get job information

     Retrieve information about the provided **job ID**, such as status, payload, and result.

    Args:
        job_id (str): Unique ID of the job you want to get.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ScalewayQaasV1Alpha1Job
    """

    def get_job(self, job_id: str) -> ScalewayQaasV1Alpha1Job:
        if not job_id:
            raise Exception("get_job: job_id cannot be None")

        response = _get_job_sync(client=self.__client, job_id=job_id)

        _raise_on_error(response)

        return response.parsed

    """List all results of a job

     Retrieve all intermediate and final results of a job.

    Args:
        job_id (str): ID of the job.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        List[ScalewayQaasV1Alpha1ListJobResultsResponse]
    """

    def list_job_results(self, job_id: str) -> List[ScalewayQaasV1Alpha1JobResult]:
        if not job_id:
            raise Exception("list_job_results: job_id cannot be None")

        response = _list_job_result_sync(client=self.__client, job_id=job_id)

        _raise_on_error(response)

        return response.parsed.job_results

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

    def cancel_job(self, job_id: str) -> ScalewayQaasV1Alpha1Job:
        if not job_id:
            raise Exception("cancel_job: job_id cannot be None")

        response = _cancel_job_sync(
            client=self.__client,
            job_id=job_id,
            body=CancelJobBody(),
        )

        _raise_on_error(response)

        return response.parsed
