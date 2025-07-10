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

from scaleway_qaas_client import QaaSClient


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
