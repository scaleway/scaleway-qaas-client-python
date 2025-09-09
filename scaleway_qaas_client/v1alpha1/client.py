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

from scaleway_qaas_client.v1alpha1.quantum_as_a_service_api_client.api.applications.get_application import (
    sync_detailed as _get_application_sync,
)
from scaleway_qaas_client.v1alpha1.quantum_as_a_service_api_client.api.applications.list_applications import (
    sync_detailed as _list_applications_sync,
)
from scaleway_qaas_client.v1alpha1.quantum_as_a_service_api_client.api.default.list_session_ac_ls import (
    sync_detailed as _list_session_acls_sync,
)
from scaleway_qaas_client.v1alpha1.quantum_as_a_service_api_client.api.jobs.cancel_job import (
    sync_detailed as _cancel_job_sync,
)
from scaleway_qaas_client.v1alpha1.quantum_as_a_service_api_client.api.jobs.create_job import (
    sync_detailed as _create_job_sync,
)
from scaleway_qaas_client.v1alpha1.quantum_as_a_service_api_client.api.jobs.get_job import (
    sync_detailed as _get_job_sync,
)
from scaleway_qaas_client.v1alpha1.quantum_as_a_service_api_client.api.jobs.list_job_results import (
    sync_detailed as _list_job_results_sync,
)
from scaleway_qaas_client.v1alpha1.quantum_as_a_service_api_client.api.jobs.list_jobs import (
    sync_detailed as _list_jobs_sync,
)
from scaleway_qaas_client.v1alpha1.quantum_as_a_service_api_client.api.models.create_model import (
    sync_detailed as _create_model_sync,
)
from scaleway_qaas_client.v1alpha1.quantum_as_a_service_api_client.api.models.get_model import (
    sync_detailed as _get_model_sync,
)
from scaleway_qaas_client.v1alpha1.quantum_as_a_service_api_client.api.models.list_models import (
    sync_detailed as _list_models_sync,
)
from scaleway_qaas_client.v1alpha1.quantum_as_a_service_api_client.api.platforms.get_platform import (
    sync_detailed as _get_platform_sync,
)
from scaleway_qaas_client.v1alpha1.quantum_as_a_service_api_client.api.platforms.list_platforms import (
    sync_detailed as _list_platforms_sync,
)
from scaleway_qaas_client.v1alpha1.quantum_as_a_service_api_client.api.processes.cancel_process import (
    sync_detailed as _cancel_process_sync,
)
from scaleway_qaas_client.v1alpha1.quantum_as_a_service_api_client.api.processes.create_process import (
    sync_detailed as _create_process_sync,
)
from scaleway_qaas_client.v1alpha1.quantum_as_a_service_api_client.api.processes.delete_process import (
    sync_detailed as _delete_process_sync,
)
from scaleway_qaas_client.v1alpha1.quantum_as_a_service_api_client.api.processes.get_process import (
    sync_detailed as _get_process_sync,
)
from scaleway_qaas_client.v1alpha1.quantum_as_a_service_api_client.api.processes.list_process_results import (
    sync_detailed as _list_process_results_sync,
)
from scaleway_qaas_client.v1alpha1.quantum_as_a_service_api_client.api.processes.list_processes import (
    sync_detailed as _list_processes_sync,
)
from scaleway_qaas_client.v1alpha1.quantum_as_a_service_api_client.api.sessions.create_session import (
    sync_detailed as _create_session_sync,
)
from scaleway_qaas_client.v1alpha1.quantum_as_a_service_api_client.api.sessions.delete_session import (
    sync_detailed as _delete_session_sync,
)
from scaleway_qaas_client.v1alpha1.quantum_as_a_service_api_client.api.sessions.get_session import (
    sync_detailed as _get_session_sync,
)
from scaleway_qaas_client.v1alpha1.quantum_as_a_service_api_client.api.sessions.list_sessions import (
    sync_detailed as _list_sessions_sync,
)
from scaleway_qaas_client.v1alpha1.quantum_as_a_service_api_client.api.sessions.terminate_session import (
    sync_detailed as _terminate_session_sync,
)
from scaleway_qaas_client.v1alpha1.quantum_as_a_service_api_client.client import (
    AuthenticatedClient,
)
from scaleway_qaas_client.v1alpha1.quantum_as_a_service_api_client.models import (
    CancelJobBody,
    CancelProcessBody,
    CreateJobBody,
    CreateJobBodyCircuit,
    CreateModelBody,
    CreateProcessBody,
    CreateSessionBody,
    ListPlatformsPlatformTechnology,
    ListPlatformsPlatformType,
    ScalewayQaasV1Alpha1Application,
    ScalewayQaasV1Alpha1Job,
    ScalewayQaasV1Alpha1JobResult,
    ScalewayQaasV1Alpha1Model,
    ScalewayQaasV1Alpha1Platform,
    ScalewayQaasV1Alpha1Process,
    ScalewayQaasV1Alpha1ProcessResult,
    ScalewayQaasV1Alpha1Session,
    ScalewayQaasV1Alpha1SessionAccess,
    TerminateSessionBody,
)
from scaleway_qaas_client.v1alpha1.quantum_as_a_service_api_client.types import (
    UNSET,
    Response,
)

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
        url = url or _DEFAULT_URL

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

    def get_platform(self, platform_id: str) -> ScalewayQaasV1Alpha1Platform:
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

        if not platform_id:
            raise Exception("get_platform: platform_id cannot be None")

        response = _get_platform_sync(client=self.__client, platform_id=platform_id)

        _raise_on_error(response)

        return response.parsed

    def list_platforms(
        self,
        name: Optional[str] = None,
        backend_name: Optional[str] = None,
        provider_name: Optional[str] = None,
        platform_type: Optional[str] = None,
        platform_technology: Optional[str] = None,
    ) -> List[ScalewayQaasV1Alpha1Platform]:
        """List all available platforms

        Retrieve information about all platforms.

        Args:
            provider_name (Union[Unset, str]): List platforms with this provider name.
            backend_name (Union[Unset, str]): List platforms with this backend name.
            name (Union[Unset, str]): List platforms with this name.
            platform_type (Union[Unset, ListPlatformsPlatformType]): List platforms with this type.
            platform_technology (Union[Unset, ListPlatformsPlatformTechnology]): List platforms with this technology.

        Raises:
            errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
            httpx.TimeoutException: If the request takes longer than Client.timeout.

        Returns:
            List[ScalewayQaasV1Alpha1ListPlatforms]
        """

        if isinstance(platform_technology, str):
            platform_technology = ListPlatformsPlatformTechnology[platform_technology]
        elif not platform_technology:
            platform_technology = UNSET

        if isinstance(platform_type, str):
            platform_type = ListPlatformsPlatformType[platform_type]
        elif not platform_type:
            platform_type = UNSET

        response = _list_platforms_sync(
            client=self.__client,
            name=name,
            provider_name=provider_name,
            backend_name=backend_name,
            platform_type=platform_type,
            platform_technology=platform_technology,
        )

        _raise_on_error(response)

        return response.parsed.platforms

    def create_session(
        self,
        platform_id: str,
        max_duration: Union[str, int] = "59m",
        max_idle_duration: Union[str, int] = "59m",
        deduplication_id: Optional[str] = None,
        name: Optional[str] = None,
        model_id: Optional[str] = None,
        parameters: Optional[Union[Dict, List, str]] = None,
    ) -> ScalewayQaasV1Alpha1Session:
        """Create a session

        Create a dedicated session for the specified platform.

        Args:
            platform_id (str): ID of the Platform for which the session was created.
            name (Union[None, Unset, str]): Name of the session.
            max_idle_duration (Union[None, Unset, str]): Maximum idle duration before the session ends. (in seconds)
                Example: 2.5s.
            max_duration (Union[None, Unset, str]): Maximum duration before the session ends. (in seconds) Example: 20m.
            deduplication_id (Union[None, Unset, str]): Deduplication ID of the session.
            model_id (Union[None, Unset, str]): Default computation model ID to be executed by job assigned to this session.

        Raises:
            errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
            httpx.TimeoutException: If the request takes longer than Client.timeout.

        Returns:
            ScalewayQaasV1Alpha1Session
        """

        if not platform_id:
            raise Exception("create_session: platform_id cannot be None")

        if parameters:
            parameters = (
                parameters if isinstance(parameters, str) else json.dumps(parameters)
            )

        name = name or f"qs-{randomname.get_name()}"

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
                model_id=model_id,
                parameters=parameters,
            ),
        )

        _raise_on_error(response)

        return response.parsed

    def get_session(self, session_id: str) -> ScalewayQaasV1Alpha1Session:
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

        if not session_id:
            raise Exception("get_session: session_id cannot be None")

        response = _get_session_sync(client=self.__client, session_id=session_id)

        _raise_on_error(response)

        return response.parsed

    def list_sessions(
        self, platform_id: Optional[str] = None
    ) -> List[ScalewayQaasV1Alpha1Session]:
        """List all sessions

        Retrieve information about all sessions.

        Args:
            platform_id (Union[Unset, str]): List sessions that have been created for this platform.

        Raises:
            errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
            httpx.TimeoutException: If the request takes longer than Client.timeout.

        Returns:
            List[ScalewayQaasV1Alpha1ListSessionsResponse]
        """

        response = _list_sessions_sync(
            client=self.__client, project_id=self.__project_id, platform_id=platform_id
        )

        _raise_on_error(response)

        return response.parsed.sessions

    def terminate_session(self, session_id: str) -> ScalewayQaasV1Alpha1Session:
        """Terminate an existing session

        Terminate a session by its unique ID and cancel all its attached jobs and booking.

        Args:
            session_id (str): Unique ID of the session.

        Raises:
            errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
            httpx.TimeoutException: If the request takes longer than Client.timeout.

        Returns:
            ScalewayQaasV1Alpha1Session
        """

        if not session_id:
            raise Exception("terminate_session: session_id cannot be None")

        response = _terminate_session_sync(
            client=self.__client,
            session_id=session_id,
            body=TerminateSessionBody(),
        )

        _raise_on_error(response)

        return response.parsed

    def delete_session(self, session_id: str):
        """Delete an existing session

        Delete a session by its unique ID and delete all its attached job and booking.

        Args:
            session_id (str): Unique ID of the session.

        Raises:
            errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
            httpx.TimeoutException: If the request takes longer than Client.timeout.
        """

        if not session_id:
            raise Exception("delete_session: session_id cannot be None")

        _delete_session_sync(client=self.__client, session_id=session_id)

    def list_session_acls(
        self, session_id: Optional[str] = None
    ) -> List[ScalewayQaasV1Alpha1SessionAccess]:
        """List session ACLs

        List the Access permission of the existing session.

        Args:
            session_id (str): Unique ID of the session.

        Raises:
            errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
            httpx.TimeoutException: If the request takes longer than Client.timeout.
        """

        if not session_id:
            raise Exception("list_session_acls: session_id cannot be None")

        response = _list_session_acls_sync(client=self.__client, session_id=session_id)

        _raise_on_error(response)

        return response.parsed.acls

    def create_job(
        self,
        session_id: str,
        model_id: Optional[str] = None,
        payload: Optional[
            Union[Dict, List, str]
        ] = None,  # Deprecated, use model_id from create_model(payload) instead
        name: Optional[str] = None,
        parameters: Optional[Union[Dict, List, str]] = None,
    ) -> ScalewayQaasV1Alpha1Job:
        """Create a job

        Create a job to be executed inside a session.

        Args:
            name (str): Name of the job.
            session_id (str): Session in which the job is executed.
            payload (str): DEPRECATED Quantum circuit that should be executed.
            model_id (Union[None, Unset, str]): Computation model ID to be executed by the job.
            parameters (Union[None, Unset, str]): Execution parameters for this job.

        Raises:
            errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
            httpx.TimeoutException: If the request takes longer than Client.timeout.

        Returns:
            ScalewayQaasV1Alpha1Job
        """

        if not session_id:
            raise Exception("create_job: session_id cannot be None")

        if payload:
            payload = payload if isinstance(payload, str) else json.dumps(payload)

        if parameters:
            parameters = (
                parameters if isinstance(parameters, str) else json.dumps(parameters)
            )

        name = name or f"qj-{randomname.get_name()}"

        response = _create_job_sync(
            client=self.__client,
            body=CreateJobBody(
                name=name,
                session_id=session_id,
                model_id=model_id,
                circuit=(CreateJobBodyCircuit(qiskit_circuit=payload)),
                parameters=parameters,
            ),
        )

        _raise_on_error(response)

        return response.parsed

    def get_job(self, job_id: str) -> ScalewayQaasV1Alpha1Job:
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

        if not job_id:
            raise Exception("get_job: job_id cannot be None")

        response = _get_job_sync(client=self.__client, job_id=job_id)

        _raise_on_error(response)

        return response.parsed

    def list_jobs(self, session_id: str) -> List[ScalewayQaasV1Alpha1Job]:
        """List all jobs within a project or session

        Retrieve information about all jobs within a given session.

        Args:
            session_id (str): Unique ID of the session you want to get jobs from.

        Raises:
            errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
            httpx.TimeoutException: If the request takes longer than Client.timeout.

        Returns:
            Response[ScalewayQaasV1Alpha1ListJobsResponse]
        """
        response = _list_jobs_sync(client=self.__client, session_id=session_id)

        _raise_on_error(response)

        return response.parsed.jobs

    def list_job_results(self, job_id: str) -> List[ScalewayQaasV1Alpha1JobResult]:
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

        if not job_id:
            raise Exception("list_job_results: job_id cannot be None")

        response = _list_job_results_sync(client=self.__client, job_id=job_id)

        _raise_on_error(response)

        return response.parsed.job_results

    def cancel_job(self, job_id: str) -> ScalewayQaasV1Alpha1Job:
        """Cancel a job

        Cancel the job corresponding to the provided **job ID**.

        Args:
            job_id (str): Unique ID of the job.

        Raises:
            errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
            httpx.TimeoutException: If the request takes longer than Client.timeout.

        Returns:
            ScalewayQaasV1Alpha1Job
        """

        if not job_id:
            raise Exception("cancel_job: job_id cannot be None")

        response = _cancel_job_sync(
            client=self.__client,
            job_id=job_id,
            body=CancelJobBody(),
        )

        _raise_on_error(response)

        return response.parsed

    def get_application(self, application_id: str) -> ScalewayQaasV1Alpha1Application:
        """Get application information

        Retrieve information about the provided **applcation ID**, such as name, type and compatible
        platforms.

        Args:
            application_id (str): Unique ID of the application.

        Raises:
            errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
            httpx.TimeoutException: If the request takes longer than Client.timeout.

        Returns:
            Response[ScalewayQaasV1Alpha1Application]
        """
        if not application_id:
            raise Exception("get_platform: platform_id cannot be None")

        response = _get_application_sync(
            client=self.__client, application_id=application_id
        )

        _raise_on_error(response)

        return response.parsed

    def list_applications(
        self,
        name: Optional[str] = None,
    ) -> List[ScalewayQaasV1Alpha1Application]:
        """List all available applications

        Retrieve information about all applications.

        Args:
            name (Union[Unset, str]): List applications with this name.
            application_type (Union[Unset, ListApplicationsApplicationType]): List applications with
                this type. Default: ListApplicationsApplicationType.UNKNOWN_TYPE.

        Raises:
            errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
            httpx.TimeoutException: If the request takes longer than Client.timeout.

        Returns:
            Response[ScalewayQaasV1Alpha1ListApplicationsResponse]
        """

        response = _list_applications_sync(
            client=self.__client,
            name=name,
        )

        _raise_on_error(response)

        return response.parsed.applications

    def create_process(
        self,
        application_id: str,
        platform_id: str,
        input: Union[List, Dict, str],
        name: Optional[str] = None,
    ) -> ScalewayQaasV1Alpha1Process:
        """Create a process

        Create a new process for the specified application on a specified platform.

        Args:
            platform_id (Union[None, str]): ID of the platform for which the process was created.
            application_id (Union[None, str]): ID of the application for which the process was created.
            name (Union[Unset, str]): Name of the process.
            input_(Union[None, Unset, str]): Process parameters in JSON format.

        Raises:
            errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
            httpx.TimeoutException: If the request takes longer than Client.timeout.

        Returns:
            Response[ScalewayQaasV1Alpha1Process]
        """

        if not platform_id:
            raise Exception("create_process: platform_id cannot be None")

        if not application_id:
            raise Exception("create_process: application_id cannot be None")

        if not input:
            raise Exception("create_process: input cannot be None")

        name = name or f"qp-{randomname.get_name()}"

        input = input if isinstance(input, str) else json.dumps(input)

        response = _create_process_sync(
            client=self.__client,
            body=CreateProcessBody(
                project_id=self.__project_id,
                name=name,
                platform_id=platform_id,
                application_id=application_id,
                input_=input,
            ),
        )

        _raise_on_error(response)

        return response.parsed

    def cancel_process(self, process_id: str) -> ScalewayQaasV1Alpha1Process:
        """Cancel a running process

        Cancel a process by its unique ID. Intermediate results are still available.

        Args:
            process_id (str): Unique ID of the process.

        Raises:
            errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
            httpx.TimeoutException: If the request takes longer than Client.timeout.

        Returns:
            Response[ScalewayQaasV1Alpha1Process]
        """
        if not process_id:
            raise Exception("cancel_process: job_id cannot be None")

        response = _cancel_process_sync(
            client=self.__client,
            process_id=process_id,
            body=CancelProcessBody(),
        )

        _raise_on_error(response)

        return response.parsed

    def delete_process(self, process_id: str):
        """Delete an existing process

        Delete a process by its unique ID and delete all its data.

        Args:
            process_id (str): Unique ID of the process.

        Raises:
            errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
            httpx.TimeoutException: If the request takes longer than Client.timeout.
        """

        if not process_id:
            raise Exception("delete_process: process_id cannot be None")

        _delete_process_sync(client=self.__client, process_id=process_id)

    def get_process(self, process_id: str) -> ScalewayQaasV1Alpha1Session:
        """Get process information

        Retrieve information about the provided **process ID**, such as name, status and progress.

        Args:
            process_id (str): Unique ID of the process.

        Raises:
            errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
            httpx.TimeoutException: If the request takes longer than Client.timeout.

        Returns:
            Response[ScalewayQaasV1Alpha1Process]
        """
        if not process_id:
            raise Exception("get_process: process_id cannot be None")

        response = _get_process_sync(client=self.__client, process_id=process_id)

        _raise_on_error(response)

        return response.parsed

    def list_processes(
        self, application_id: Optional[str] = None
    ) -> List[ScalewayQaasV1Alpha1Session]:
        """List all processes

        Retrieve information about all processes.

        Args:
            application_id (Union[Unset, str]): List processes that have been created for this
                application.

        Raises:
            errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
            httpx.TimeoutException: If the request takes longer than Client.timeout.

        Returns:
            Response[ScalewayQaasV1Alpha1ListProcessesResponse]
        """
        response = _list_processes_sync(
            client=self.__client,
            project_id=self.__project_id,
            application_id=application_id,
        )

        _raise_on_error(response)

        return response.parsed.processes

    def list_process_results(
        self, process_id: str
    ) -> List[ScalewayQaasV1Alpha1ProcessResult]:
        """List all results of a process

        Retrieve all intermediate and final result of a process.

        Args:
            process_id (str): ID of the process.

        Raises:
            errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
            httpx.TimeoutException: If the request takes longer than Client.timeout.

        Returns:
            Response[ScalewayQaasV1Alpha1ListProcessResultsResponse]
        """
        if not process_id:
            raise Exception("list_process_results: process_id cannot be None")

        response = _list_process_results_sync(
            client=self.__client, process_id=process_id
        )

        _raise_on_error(response)

        return response.parsed.process_results

    def create_model(
        self, payload: Union[str, Dict, List]
    ) -> ScalewayQaasV1Alpha1Model:
        """Create a new model

        Create and register a new model that can be executed through next jobs. A model can also be assigned
        to a Session.

        Args:
            payload (Union[None, Unset, str]): The serialized model data.

        Raises:
            errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
            httpx.TimeoutException: If the request takes longer than Client.timeout.

        Returns:
            ScalewayQaasV1Alpha1Model
        """
        if not payload:
            raise Exception("create_model: payload cannot be None")

        payload = payload if isinstance(payload, str) else json.dumps(payload)

        response = _create_model_sync(
            client=self.__client,
            body=CreateModelBody(
                project_id=self.__project_id,
                payload=payload,
            ),
        )

        _raise_on_error(response)

        return response.parsed

    def get_model(self, model_id: str) -> ScalewayQaasV1Alpha1Model:
        """Get model information

        Retrieve information about of the provided **model ID**.

        Args:
            model_id (str): Unique ID of the model.

        Raises:
            errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
            httpx.TimeoutException: If the request takes longer than Client.timeout.

        Returns:
            Response[ScalewayQaasV1Alpha1Model]
        """
        if not model_id:
            raise Exception("get_model: model_id cannot be None")

        response = _get_model_sync(client=self.__client, model_id=model_id)

        _raise_on_error(response)

        return response.parsed

    def list_models(self) -> List[ScalewayQaasV1Alpha1Model]:
        """List all models attached to the **project ID**

        Retrieve information about all models of the provided **project ID**.

        Raises:
            errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
            httpx.TimeoutException: If the request takes longer than Client.timeout.

        Returns:
            Response[ScalewayQaasV1Alpha1ListModelsResponse]
        """
        response = _list_models_sync(
            client=self.__client,
            project_id=self.__project_id,
        )

        _raise_on_error(response)

        return response.parsed.models
