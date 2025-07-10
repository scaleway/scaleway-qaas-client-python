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
import randomname

from pytimeparse.timeparse import timeparse

from typing import List, Optional, Dict, Union

from scaleway_qaas_client.quantum_as_a_service_api_client.models import (
    CreateJobBody,
    CreateJobBodyCircuit,
    CreateSessionBody,
    TerminateSessionBody,
    CancelJobBody,
    ScalewayQaasV1Alpha1Platform,
    ScalewayQaasV1Alpha1Job,
    ScalewayQaasV1Alpha1JobResult,
    ScalewayQaasV1Alpha1Session,
)

from scaleway_qaas_client.quantum_as_a_service_api_client.api.sessions.create_session import (
    sync_detailed as _create_session_sync,
)
from scaleway_qaas_client.quantum_as_a_service_api_client.api.sessions.get_session import (
    sync_detailed as _get_session_sync,
)
from scaleway_qaas_client.quantum_as_a_service_api_client.api.sessions.list_sessions import (
    sync_detailed as _list_session_sync,
)
from scaleway_qaas_client.quantum_as_a_service_api_client.api.sessions.terminate_session import (
    sync_detailed as _terminate_session_sync,
)
from scaleway_qaas_client.quantum_as_a_service_api_client.api.sessions.delete_session import (
    sync_detailed as _delete_session_sync,
)
from scaleway_qaas_client.quantum_as_a_service_api_client.api.platforms.list_platforms import (
    sync_detailed as _list_platforms_sync,
)
from scaleway_qaas_client.quantum_as_a_service_api_client.api.platforms.get_platform import (
    sync_detailed as _get_platform_sync,
)
from scaleway_qaas_client.quantum_as_a_service_api_client.api.jobs.create_job import (
    sync_detailed as _create_job_sync,
)
from scaleway_qaas_client.quantum_as_a_service_api_client.api.jobs.get_job import (
    sync_detailed as _get_job_sync,
)
from scaleway_qaas_client.quantum_as_a_service_api_client.api.jobs.cancel_job import (
    sync_detailed as _cancel_job_sync,
)
from scaleway_qaas_client.quantum_as_a_service_api_client.api.jobs.list_job_results import (
    sync_detailed as _list_job_result_sync,
)
from scaleway_qaas_client.quantum_as_a_service_api_client.types import Response

from scaleway_qaas_client.quantum_as_a_service_api_client.client import (
    AuthenticatedClient,
)


_DEFAULT_URL = "https://api.scaleway.com"


def _raise_on_error(response: Response):
    if not response:
        raise Exception("error: None response")

    if response.status_code.is_server_error or response.status_code.is_client_error:
        raise Exception(
            f"error {response.status_code}: {response.content.decode("utf-8")}"
        )


class QaaSClient:
    def __init__(self, project_id: str, secret_key: str, url: str = _DEFAULT_URL):
        self.__project_id = project_id

        self.__client = AuthenticatedClient(
            # headers={"X-Auth-Token": secret_key},
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
        response = _get_platform_sync(client=self.__client, platform_id=platform_id)

        _raise_on_error(response)

        return response.parsed

    def list_platforms(
        self, name: Optional[str] = None
    ) -> List[ScalewayQaasV1Alpha1Platform]:
        response = _list_platforms_sync(client=self.__client, name=name)

        _raise_on_error(response)

        return response.parsed.platforms

    def create_session(
        self,
        platform_id: str,
        max_duration: Union[str, int],
        max_idle_duration: Union[str, int],
        deduplication_id: Optional[str] = None,
        name: Optional[str] = None,
    ) -> ScalewayQaasV1Alpha1Session:
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

    def get_session(self, session_id: str) -> ScalewayQaasV1Alpha1Session:
        response = _get_session_sync(client=self.__client, session_id=session_id)

        _raise_on_error(response)

        return response.parsed

    def list_session(
        self, platform_id: Optional[str] = None
    ) -> List[ScalewayQaasV1Alpha1Session]:
        response = _list_session_sync(
            client=self.__client, project_id=self.__project_id, platform_id=platform_id
        )

        _raise_on_error(response)

        return response.parsed.sessions

    def terminate_session(self, session_id: str) -> ScalewayQaasV1Alpha1Session:
        response = _terminate_session_sync(
            client=self.__client,
            session_id=session_id,
            body=TerminateSessionBody(),
        )

        _raise_on_error(response)

        return response.parsed

    def delete_session(self, session_id: str):
        _delete_session_sync(client=self.__client, session_id=session_id)

    def create_job(
        self,
        session_id: str,
        payload: Union[Dict, List, str],
        name: Optional[str] = None,
    ) -> ScalewayQaasV1Alpha1Job:
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

    def get_job(self, job_id: str) -> ScalewayQaasV1Alpha1Job:
        response = _get_job_sync(client=self.__client, job_id=job_id)

        _raise_on_error(response)

        return response.parsed

    def list_job_results(self, job_id: str) -> List[ScalewayQaasV1Alpha1JobResult]:
        response = _list_job_result_sync(client=self.__client, job_id=job_id)

        _raise_on_error(response)

        return response.parsed.job_results

    def cancel_job(self, job_id: str) -> ScalewayQaasV1Alpha1Job:
        response = _cancel_job_sync(
            client=self.__client,
            job_id=job_id,
            body=CancelJobBody(),
        )

        _raise_on_error(response)

        return response.parsed
