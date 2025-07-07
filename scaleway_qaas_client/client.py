import json

from typing import List, Optional, Dict

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
    sync as create_session_sync,
)
from quantum_as_a_service_api_client.api.sessions.terminate_session import (
    sync as terminate_session_sync,
)
from quantum_as_a_service_api_client.api.sessions.delete_session import (
    sync_detailed as delete_session_sync,
)
from quantum_as_a_service_api_client.api.platforms.list_platforms import (
    sync as list_platforms_sync,
)
from quantum_as_a_service_api_client.api.jobs.create_job import (
    sync as create_job_sync,
)
from quantum_as_a_service_api_client.api.jobs.get_job import (
    sync as get_job_sync,
)
from quantum_as_a_service_api_client.api.jobs.list_job_results import (
    sync as list_job_result_sync,
)

from quantum_as_a_service_api_client.client import Client


__DEFAULT_URL = "https://api.scaleway.com/qaas/v1alpha1"


class QaaSClient:
    def __init__(self, project_id: str, token: str, url: str = __DEFAULT_URL):
        self.__token = token
        self.__project_id = project_id

        self.__client = Client(
            headers={"X-Auth-Token": self.__token},
            base_url=self.__url,
            timeout=10.0,
            verify_ssl="https" in url,
        )

    def list_platforms(self, name: Optional[str]) -> List[ScalewayQaasV1Alpha1Platform]:
        response = list_platforms_sync(client=self.__client, name=name)

        assert response

        return response.platforms

    def create_session(
        self,
        name: str,
        platform_id: str,
        deduplication_id: str,
        max_duration: str,
        max_idle_duration: str,
    ) -> ScalewayQaasV1Alpha1Session:
        session = create_session_sync(
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

    def terminate_session(self, session_id: str) -> ScalewayQaasV1Alpha1Session:
        session = terminate_session_sync(
            client=self.__client,
            body=TerminateSessionBody(
                session_id=session_id,
            ),
        )

        return session

    def delete_session(self, session_id: str):
        delete_session_sync(client=self.__client, session_id=session_id)

    def create_job(
        self, name: str, session_id: str, circuits: Dict
    ) -> ScalewayQaasV1Alpha1Job:
        circuits = circuits if isinstance(circuits, str) else json.dumps(circuits)

        job = create_job_sync(
            client=self.__client,
            body=CreateJobBody(
                name=name,
                session_id=session_id,
                circuit=CreateJobBodyCircuit(qiskit_circuit=circuits),
            ),
        )

        return job

    def get_job(self, job_id: str) -> ScalewayQaasV1Alpha1Job:
        job = get_job_sync(client=self.__client, job_id=job_id)

        return job

    def list_job_results(self, job_id: str) -> List[ScalewayQaasV1Alpha1JobResult]:
        response = list_job_result_sync(client=self.__client, job_id=job_id)

        return response.job_results
