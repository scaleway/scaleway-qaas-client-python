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

from scaleway_qaas_client.v1alpha1 import QaaSClient

_RANDOM_UUID = str(uuid.uuid4())
_TEST_PLATFORM_NAME = os.environ.get("TEST_PLATFORM_NAME", "aer_simulation_pop_c16m128")


def _get_client() -> QaaSClient:
    client = QaaSClient(
        project_id=os.environ["SCALEWAY_PROJECT_ID"],
        secret_key=os.environ["SCALEWAY_SECRET_KEY"],
        url=os.environ["SCALEWAY_API_URL"],
    )

    return client


def test_list_platform():
    client = _get_client()

    platforms = client.list_platforms()

    assert platforms is not None
    assert len(platforms) > 0


def test_list_platforms_by_backend():
    client = _get_client()

    platforms = client.list_platforms(backend_name="aer")

    assert len(platforms) > 0

    for platform in platforms:
        assert platform.backend_name == "aer"


def test_list_platforms_by_provider():
    client = _get_client()

    platforms = client.list_platforms(provider_name="quandela")

    assert len(platforms) > 0

    for platform in platforms:
        assert platform.provider_name == "quandela"


def test_list_platforms_by_unexisting_provider():
    client = _get_client()

    platforms = client.list_platforms(provider_name=_RANDOM_UUID)

    assert platforms == []


def test_list_platforms_by_unexisting_backend():
    client = _get_client()

    platforms = client.list_platforms(backend_name=_RANDOM_UUID)

    assert platforms == []


def test_list_platforms_by_name():
    client = _get_client()

    platforms = client.list_platforms(name=_TEST_PLATFORM_NAME)

    for platform in platforms:
        assert platform.name == _TEST_PLATFORM_NAME

    assert len(platforms) > 0


def test_list_platforms_by_unexisting_name():
    client = _get_client()

    platforms = client.list_platforms(name=_RANDOM_UUID)

    assert platforms == []


def test_list_sessions_unexisting_platform():
    client = _get_client()

    sessions = client.list_sessions(platform_id=_RANDOM_UUID)

    assert sessions == []


def test_create_delete_session():
    client = _get_client()

    try:
        platforms = client.list_platforms(name=_TEST_PLATFORM_NAME)

        assert platforms is not None
        assert len(platforms) == 1

        target_platform = platforms[0]

        assert target_platform.id is not None

        max_duration = "2m"
        max_idle_duration = "2m"

        session = client.create_session(
            platform_id=target_platform.id,
            max_duration=max_duration,
            max_idle_duration=max_idle_duration,
        )

        assert session is not None
        assert session.id is not None
        assert session.platform_id == target_platform.id

        while session.status == "starting":
            session = client.get_session(session.id)
            time.sleep(3)

        assert session.status == "running"

        session_acls = client.list_session_acls(session.id)
        assert len(session_acls) > 0

        session = client.terminate_session(session.id)

        while session.status == "stopping":
            session = client.get_session(session.id)
            time.sleep(3)

        assert session.status == "stopped"
    finally:
        client.delete_session(session.id)


def test_list_platform_bookings():
    client = _get_client()

    platforms = client.list_platforms(name=_TEST_PLATFORM_NAME)

    assert platforms is not None
    assert len(platforms) == 1

    target_platform = platforms[0]

    assert target_platform.id is not None

    bookings = client.list_platform_bookings(target_platform.id)

    assert len(bookings) > 0


def test_create_session_same_deduplication_id():
    client = _get_client()

    try:
        platforms = client.list_platforms(name=_TEST_PLATFORM_NAME)

        assert len(platforms) > 0

        platform = platforms[0]

        max_duration = "2m"
        max_idle_duration = "2m"
        deduplication_id = f"hihaaa-{_RANDOM_UUID}"

        session = client.create_session(
            platform_id=platform.id,
            max_duration=max_duration,
            max_idle_duration=max_idle_duration,
            deduplication_id=deduplication_id,
        )

        assert session is not None
        assert session.id is not None
        assert session.platform_id == platform.id
        assert session.deduplication_id == deduplication_id
        assert session.status in ["starting", "running"]

        second_session = client.create_session(
            platform_id=platform.id,
            deduplication_id=deduplication_id,
        )

        assert second_session != None
        assert second_session.id == session.id
        assert second_session.project_id == session.project_id
        assert second_session.platform_id == session.platform_id
        assert second_session.name == session.name
        assert second_session.max_duration == session.max_duration
        assert second_session.max_idle_duration == session.max_idle_duration
        assert second_session.status in session.status
        assert second_session.deduplication_id == session.deduplication_id
    finally:
        client.delete_session(session.id)
