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

from typing import List, Optional, Dict, Union

from quantum_as_a_service_api_client.models import (
    CreateJobBody,
    CreateJobBodyCircuit,
    CreateSessionBody,
    TerminateSessionBody,
    ScalewayQaasV1Alpha1Platform,
    ScalewayQaasV1Alpha1Job,
    ScalewayQaasV1Alpha1JobResult,
    ScalewayQaasV1Alpha1Session,
)

from quantum_as_a_service_api_client.api.sessions.create_session import (
    sync as _create_session_sync,
)
from quantum_as_a_service_api_client.api.sessions.get_session import (
    sync as _get_session_sync,
)
from quantum_as_a_service_api_client.api.sessions.terminate_session import (
    sync as _terminate_session_sync,
)
from quantum_as_a_service_api_client.api.sessions.delete_session import (
    sync_detailed as _delete_session_sync,
)
from quantum_as_a_service_api_client.api.platforms.list_platforms import (
    sync as _list_platforms_sync,
)
from quantum_as_a_service_api_client.api.platforms.get_platform import (
    sync as _get_platform_sync,
)
from quantum_as_a_service_api_client.api.jobs.create_job import (
    sync as _create_job_sync,
)
from quantum_as_a_service_api_client.api.jobs.get_job import (
    sync as _get_job_sync,
)
from quantum_as_a_service_api_client.api.jobs.list_job_results import (
    sync as _list_job_result_sync,
)

from quantum_as_a_service_api_client.client import Client


__DEFAULT_URL = "https://api.scaleway.com/qaas/v1alpha1"


class QaaSClient:
    def __init__(self, project_id: str, secret_key: str, url: str = __DEFAULT_URL):
        self.__project_id = project_id

        self.__client = Client(
            headers={"X-Auth-Token": secret_key},
            base_url=url,
            timeout=10.0,
            verify_ssl="https" in url,
        )

    def get_platform(self, platform_id: str) -> ScalewayQaasV1Alpha1Platform:
        platform = _get_platform_sync(client=self.__client, platform_id=platform_id)

        return platform

    def list_platforms(
        self, name: Optional[str] = None
    ) -> List[ScalewayQaasV1Alpha1Platform]:
        response = _list_platforms_sync(client=self.__client, name=name)

        assert response

        return response.platforms

    def create_session(
        self,
        platform_id: str,
        max_duration: str,
        max_idle_duration: str,
        deduplication_id: Optional[str] = None,
        name: Optional[str] = None,
    ) -> ScalewayQaasV1Alpha1Session:
        name = name if name else f"qs-{randomname.get_name()}"

        session = _create_session_sync(
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

        return session

    def get_session(self, session_id: str) -> ScalewayQaasV1Alpha1Session:
        session = _get_session_sync(client=self.__client, session_id=session_id)

        return session

    def terminate_session(self, session_id: str) -> ScalewayQaasV1Alpha1Session:
        session = _terminate_session_sync(
            client=self.__client,
            body=TerminateSessionBody(
                session_id=session_id,
            ),
        )

        return session

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

        job = _create_job_sync(
            client=self.__client,
            body=CreateJobBody(
                name=name,
                session_id=session_id,
                circuit=CreateJobBodyCircuit(qiskit_circuit=payload),
            ),
        )

        return job

    def get_job(self, job_id: str) -> ScalewayQaasV1Alpha1Job:
        job = _get_job_sync(client=self.__client, job_id=job_id)

        return job

    def list_job_results(self, job_id: str) -> List[ScalewayQaasV1Alpha1JobResult]:
        response = _list_job_result_sync(client=self.__client, job_id=job_id)

        return response.job_results
