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
import os
import time
import uuid

from scaleway_qaas_client import QaaSClient

_RANDOM_UUID = str(uuid.uuid4())

def _get_client() -> QaaSClient:
    client = QaaSClient(
        project_id=os.environ["SCALEWAY_PROJECT_ID"],
        secret_key=os.environ["SCALEWAY_API_TOKEN"],
        url=os.environ["SCALEWAY_API_URL"],
    )

    return client


def test_list_platform():
    client = _get_client()

    platforms = client.list_platforms()

    assert platforms is not None
    assert len(platforms) > 0


def test_create_delete_session():
    client = _get_client()

    platforms = client.list_platforms(
        name=os.environ.get("TEST_PLATFORM_NAME", "aer_simulation_pop_c16m128")
    )

    assert platforms is not None
    assert len(platforms) == 1

    target_platform = platforms[0]

    assert target_platform.id is not None

    session = client.create_session(
        platform_id=target_platform.id, max_duration="2m", max_idle_duration="2m"
    )

    assert session is not None
    assert session.id is not None
    assert session.platform_id == target_platform.id

    while session.status == "starting":
        session = client.get_session(session.id)
        time.sleep(3)

    assert session.status == "running"

    session = client.terminate_session(session.id)

    while session.status == "stopping":
        session = client.get_session(session.id)
        time.sleep(3)

    assert session.status == "stopped"

    client.delete_session(session.id)

# def test_list_platforms_by_backend(self):
#     if self._PLATFORM_NAME.startswith("qsim"):
#         backend_name = "qsim"
#     elif self._PLATFORM_NAME.startswith("aer"):
#         backend_name = "aer"

#     platforms = self._client.list_platforms(backend_name=backend_name)

#     for platform in platforms:
#         assert platform.backend_name == backend_name

#     assert len(platforms) > 0

# def test_list_platforms_by_provider(self):
#     provider_name = "qiskit"
#     platforms = self._client.list_platforms(provider_name=provider_name)

#     for platform in platforms:
#         assert platform.provider_name == provider_name
#     assert len(platforms) > 0

# def test_list_platforms_by_unexisting_provider(self):
#     platforms = self._client.list_platforms(provider_name=random_name())

#     assert platforms == []

# def test_list_platforms_by_unexisting_backend(self):
#     platforms = self._client.list_platforms(backend_name=random_name())

#     assert platforms == []

# def test_list_platforms_by_name(self):
#     name = self._PLATFORM_NAME
#     platforms = self._client.list_platforms(name=name)

#     for platform in platforms:
#         assert platform.name == name
#     assert len(platforms) > 0

# def test_list_platforms_by_unexisting_name(self):
#     platforms = self._client.list_platforms(name=random_name())

#     assert platforms == []

# def test_list_platforms_by_technology(self):
#     technology = PlatformTechnology.GENERAL_PURPOSE
#     platforms = self._client.list_platforms(technology=technology)

#     for platform in platforms:
#         assert platform.technology == technology
#     assert len(platforms) > 0

# def test_get_platform(self):
#     platform = self._client.get_platform(self._PLATFORM_ID)

#     assert platform.id == self._PLATFORM_ID

# def test_get_unexisting_platform(self):
#     platform = self._client.get_platform(self._RANDOM_UUID)

#     assert platform == None

# def test_list_platforms_by_provider(self):
#     provider_name = "quandela"
#     platforms = self._client.list_platforms(provider_name=provider_name)

#     for platform in platforms:
#         assert platform.provider_name == provider_name
#     assert len(platforms) > 0

# def test_list_platforms_by_unexisting_provider(self):
#     platforms = self._client.list_platforms(provider_name=random_name())

#     assert platforms == []

# def test_list_platforms_by_name(self):
#     name = self._PLATFORM_NAME
#     platforms = self._client.list_platforms(name=name)

#     for platform in platforms:
#         assert platform.name == name
#     assert len(platforms) > 0

# def test_list_platforms_by_unexisting_name(self):
#     platforms = self._client.list_platforms(name=random_name())

#     assert platforms == []

# def test_list_platforms_by_type(self):
#     type = PlatformType.SIMULATOR
#     platforms = self._client.list_platforms(type=type)

#     for platform in platforms:
#         assert platform.type == type
#     assert len(platforms) > 0

# def test_list_platforms_by_qpu_type(self):
#     plttype = PlatformType.QPU
#     platforms = self._client.list_platforms(type=plttype)

#     for platform in platforms:
#         assert platform.type == plttype

# def test_list_platforms_by_technology(self):
#     technology = PlatformTechnology.PHOTONIC
#     platforms = self._client.list_platforms(technology=technology)

#     for platform in platforms:
#         assert platform.technology == technology
#     assert len(platforms) > 0

# def test_get_platform(self):
#     platform = self._client.get_platform(self._PLATFORM_ID)

#     assert platform.id == self._PLATFORM_ID

# def test_get_unexisting_platform(self):
#     platform = self._client.get_platform(self._RANDOM_UUID)

#     assert platform == None

# #
# # Applications tests
# #
# def test_list_applications(self):
#     applications = self._client.list_applications()

#     assert len(applications) > 0

# def test_list_applications_by_name(self):
#     name = self._APPLICATION_NAME
#     applications = self._client.list_applications(name=name)

#     for application in applications:
#         assert application.name == name
#     assert len(applications) > 0

# def test_get_application(self):
#     application = self._client.get_application(self._APPLICATION_ID)

#     assert self._PLATFORM_ID in application.compatible_platform_ids
#     assert application.id == self._APPLICATION_ID
#     assert application.name == self._APPLICATION_NAME

# def test_get_unexisting_application(self):
#     application = self._client.get_application(self._RANDOM_UUID)

#     assert application == None

# def test_list_applications_by_unexisting_name(self):
#     application = self._client.list_applications(name=random_name())

#     assert application == []

# def test_list_applications_by_type(self):
#     type = ApplicationType.VQE
#     applications = self._client.list_applications(type=type)

#     for application in applications:
#         assert application.type == type
#     assert len(applications) > 0

# def test_get_platform(self):
#     platform = self._client.get_platform(self._PLATFORM_ID)

#     assert platform.id == self._PLATFORM_ID

# def test_get_unexisting_platform(self):
#     platform = self._client.get_platform(self._RANDOM_UUID)

#     assert platform == None


# #
# # Session tests
# #
# def test_list_session_acl(self):
#     session_acls = self._client.list_session_acls(self._SESSION_ID)

#     assert session_acls == [SessionAcl.FULL.name.lower()]

# def test_create_session_with_unexisting_platform(self):
#     session = self._client.create_session(self._PROJECT_ID, self._RANDOM_UUID)

#     assert session == None

# def test_get_unexisting_session(self):
#     session = self._client.get_session(self._RANDOM_UUID)

#     assert session == None

# def test_delete_unexisting_session(self):
#     self._client.delete_session(self._RANDOM_UUID)

# def test_list_sessions_by_project_without_premission(self):
#     sessions = self._client.list_sessions(self._RANDOM_UUID)

#     assert sessions == []

# def test_list_sessions_unexisting_platform(self):
#     sessions = self._client.list_sessions(
#         self._PROJECT_ID, platform_id=self._RANDOM_UUID
#     )

#     assert sessions == []

# def test_get_session(self):
#     session = self._client.get_session(self._SESSION_ID)

#     assert session != None
#     assert session.id == self._SESSION_ID
#     assert session.project_id == self._PROJECT_ID
#     assert session.platform_id == self._PLATFORM_ID
#     assert session.name == self._SESSION_NAME
#     assert session.max_duration == self._SESSION_MAX_DURATION
#     assert session.max_idle_duration == self._SESSION_MAX_IDLE_DURATION
#     assert session.status in [SessionStatus.STARTING, SessionStatus.RUNNING]
#     assert session.deduplication_id == self._SESSION_DEDUPLICATION_ID
#     assert session.tags == self._SESSION_TAGS

# def test_list_sessions_by_project(self):
#     process = self._client.create_process(
#         self._PROJECT_ID,
#         self._PLATFORM_ID,
#         self._APPLICATION_ID,
#         self._PROCESS_NAME,
#     )

#     # Wait that the process create some sessions
#     sessions = None
#     while sessions is None or len(sessions) == 0:
#         sessions = self._client.list_sessions(self._PROJECT_ID)
#         time.sleep(2)

#     assert sessions != None
#     assert len(sessions) > 0

#     session_found = None
#     session_from_process_found = False
#     for session in sessions:
#         if session.id == self._SESSION_ID:
#             session_found = session
#         if session.origin_id == process.id:
#             session_from_process_found = True

#     assert session_from_process_found == False
#     assert session_found is not None
#     assert session_found.project_id == self._PROJECT_ID
#     assert session_found.platform_id == self._PLATFORM_ID
#     assert session_found.name == self._SESSION_NAME
#     assert session_found.max_duration == self._SESSION_MAX_DURATION
#     assert session_found.max_idle_duration == self._SESSION_MAX_IDLE_DURATION
#     assert session_found.status in [SessionStatus.STARTING, SessionStatus.RUNNING]
#     assert session_found.deduplication_id == self._SESSION_DEDUPLICATION_ID
#     assert session_found.tags == self._SESSION_TAGS

# def test_list_sessions_by_platform(self):
#     sessions = self._client.list_sessions(
#         self._PROJECT_ID, platform_id=self._PLATFORM_ID
#     )

#     assert sessions != None
#     assert len(sessions) > 0

#     session_found = False
#     for session in sessions:
#         if session.id == self._SESSION_ID:
#             session_found = True
#             break

#     assert session_found == True
#     assert session.project_id == self._PROJECT_ID
#     assert session.platform_id == self._PLATFORM_ID
#     assert session.name == self._SESSION_NAME
#     assert session.max_duration == self._SESSION_MAX_DURATION
#     assert session.max_idle_duration == self._SESSION_MAX_IDLE_DURATION
#     assert session.status in [SessionStatus.STARTING, SessionStatus.RUNNING]
#     assert session.deduplication_id == self._SESSION_DEDUPLICATION_ID
#     assert session.tags == self._SESSION_TAGS

# def test_create_session_same_deduplication_id(self):
#     session = self._client.create_session(
#         project_id=self._PROJECT_ID,
#         platform_id=self._PLATFORM_ID,
#         deduplication_id=self._SESSION_DEDUPLICATION_ID,
#     )

#     assert session != None
#     assert session.id == self._SESSION_ID
#     assert session.project_id == self._PROJECT_ID
#     assert session.platform_id == self._PLATFORM_ID
#     assert session.name == self._SESSION_NAME
#     assert session.max_duration == self._SESSION_MAX_DURATION
#     assert session.max_idle_duration == self._SESSION_MAX_IDLE_DURATION
#     assert session.status in [SessionStatus.STARTING, SessionStatus.RUNNING]
#     assert session.deduplication_id == self._SESSION_DEDUPLICATION_ID
#     # assert session.tags == self._SESSION_TAGS

# def test_update_session(self):
#     self._SESSION_NAME = "poney"
#     self._SESSION_MAX_DURATION = "555s"
#     self._SESSION_MAX_IDLE_DURATION = "555s"
#     session = self._client.update_session(
#         self._SESSION_ID,
#         name=self._SESSION_NAME,
#         max_duration=self._SESSION_MAX_DURATION,
#         max_idle_duration=self._SESSION_MAX_IDLE_DURATION,
#     )

#     assert session != None
#     assert session.project_id == self._PROJECT_ID
#     assert session.platform_id == self._PLATFORM_ID
#     assert session.name == self._SESSION_NAME
#     assert session.max_duration == self._SESSION_MAX_DURATION
#     assert session.max_idle_duration == self._SESSION_MAX_IDLE_DURATION
#     assert session.deduplication_id == self._SESSION_DEDUPLICATION_ID

#     session = self._client.get_session(self._SESSION_ID)

#     assert session != None
#     assert session.project_id == self._PROJECT_ID
#     assert session.platform_id == self._PLATFORM_ID
#     assert session.name == self._SESSION_NAME
#     assert session.max_duration == self._SESSION_MAX_DURATION
#     assert session.max_idle_duration == self._SESSION_MAX_IDLE_DURATION
#     assert session.deduplication_id == self._SESSION_DEDUPLICATION_ID

# def test_update_session_tags(self):
#     tags = ["updated", "other"]
#     session = self._client.update_session(self._SESSION_ID, tags=tags)

#     assert session != None
#     assert session.project_id == self._PROJECT_ID
#     assert session.platform_id == self._PLATFORM_ID
#     assert session.deduplication_id == self._SESSION_DEDUPLICATION_ID
#     assert session.tags == tags

#     session = self._client.get_session(self._SESSION_ID)

#     assert session != None
#     assert session.project_id == self._PROJECT_ID
#     assert session.platform_id == self._PLATFORM_ID
#     assert session.deduplication_id == self._SESSION_DEDUPLICATION_ID
#     assert session.tags == tags

# def test_remove_session_tags(self):
#     tags = []
#     session = self._client.update_session(self._SESSION_ID, tags=tags)

#     assert session != None
#     assert session.project_id == self._PROJECT_ID
#     assert session.platform_id == self._PLATFORM_ID
#     assert session.deduplication_id == self._SESSION_DEDUPLICATION_ID
#     assert session.tags == tags

#     session = self._client.get_session(self._SESSION_ID)

#     assert session != None
#     assert session.project_id == self._PROJECT_ID
#     assert session.platform_id == self._PLATFORM_ID
#     assert session.deduplication_id == self._SESSION_DEDUPLICATION_ID
#     assert session.tags == tags

# #
# # Job tests
# #
# def test_create_job_with_unexisting_session(self):
#     name = random_name()
#     circuit = {"perceval_circuit": self._PERCEVAL_CIRCUIT}
#     job = self._client.create_job(name, self._RANDOM_UUID, circuit)

#     assert job == None

# def test_get_unexisting_job(self):
#     job = self._client.get_job(self._RANDOM_UUID)

#     assert job == None

# def test_update_unexisting_job(self):
#     job = self._client.update_job(self._RANDOM_UUID, name="toto")

#     assert job == None

# def test_cancel_unexisting_job(self):
#     job = self._client.cancel_job(self._RANDOM_UUID)

#     assert job == None