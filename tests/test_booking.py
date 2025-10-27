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
import pytz

from datetime import datetime, timedelta, timezone

from scaleway_qaas_client.v1alpha1 import QaaSClient

_TEST_PLATFORM_NAME = os.environ.get("TEST_PLATFORM_NAME", "aer_simulation_pop_c16m128")


def _get_now_utc() -> datetime:
    return datetime.now(timezone.utc)


def _get_now_paris() -> datetime:
    return datetime.now(pytz.timezone("Europe/Paris"))


def _get_client() -> QaaSClient:
    client = QaaSClient(
        project_id=os.environ["SCALEWAY_PROJECT_ID"],
        secret_key=os.environ["SCALEWAY_SECRET_KEY"],
        url=os.environ["SCALEWAY_API_URL"],
    )

    return client


def test_create_and_cancel_booking():
    client = _get_client()

    platforms = client.list_platforms(name=_TEST_PLATFORM_NAME)

    assert len(platforms) > 0

    target_platform = platforms[0]

    try:
        now = _get_now_paris()
        booking_start = now + timedelta(days=7)
        booking_finish = booking_start + timedelta(hours=1)
        booking_description = "my lovely booking"

        session = client.create_session(
            platform_id=target_platform.id,
            booking_demand_started_at=booking_start,
            booking_demand_finished_at=booking_finish,
            booking_demand_description=booking_description,
        )

        assert session is not None
        assert session.id is not None
        assert session.platform_id == target_platform.id
        assert session.booking_id is not None

        booking = client.get_booking(booking_id=session.booking_id)

        assert booking is not None
        assert booking.id is not None
        assert booking.description == booking_description
        assert booking.started_at is not None
        assert booking.finished_at is not None
        assert booking.status in ["validated", "waiting", "validating"]

        while True:
            time.sleep(2)
            session = client.get_session(session_id=session.id)
            booking = client.get_booking(booking_id=session.booking_id)

            assert session.status in ["starting", "running"]
            assert booking.status in ["waiting", "validating", "validated"]

            if booking.status == "validated":
                break

    finally:
        client.delete_session(session.id)

        while True:
            time.sleep(2)
            booking = client.get_booking(booking_id=session.booking_id)

            assert booking.status in ["validated", "cancelling", "cancelled"]

            if booking.status == "cancelled":
                break


def test_create_overlaping_booking():
    client = _get_client()

    platforms = client.list_platforms(name=_TEST_PLATFORM_NAME)

    assert len(platforms) > 0

    target_platform = platforms[0]

    now = _get_now_paris()
    booking_start = now + timedelta(days=1)
    booking_finish = booking_start + timedelta(hours=1)
    booking_description = "my overlaping booking"

    try:
        session = client.create_session(
            platform_id=target_platform.id,
            booking_demand_started_at=booking_start,
            booking_demand_finished_at=booking_finish,
            booking_demand_description=booking_description,
        )

        assert session == None
    except Exception as e:
        assert "existing booking" in str(e)


def test_create_too_long_booking():
    client = _get_client()

    platforms = client.list_platforms(name=_TEST_PLATFORM_NAME)

    assert len(platforms) > 0

    target_platform = platforms[0]

    now = _get_now_paris()
    booking_start = now + timedelta(minutes=1)
    booking_finish = booking_start + timedelta(hours=10)
    booking_description = "my too long booking"

    try:
        _ = client.create_session(
            platform_id=target_platform.id,
            booking_demand_started_at=booking_start,
            booking_demand_finished_at=booking_finish,
            booking_demand_description=booking_description,
        )
    except Exception as e:
        assert "max_duration not respected" in str(e)


def test_create_too_short_booking():
    client = _get_client()

    platforms = client.list_platforms(name=_TEST_PLATFORM_NAME)

    assert len(platforms) > 0

    target_platform = platforms[0]

    now = _get_now_paris()
    booking_start = now + timedelta(minutes=1)
    booking_finish = booking_start + timedelta(seconds=10)
    booking_description = "my lovely booking"

    try:
        _ = client.create_session(
            platform_id=target_platform.id,
            booking_demand_started_at=booking_start,
            booking_demand_finished_at=booking_finish,
            booking_demand_description=booking_description,
        )
    except Exception as e:
        assert "min_duration not respected" in str(e)


def test_create_too_far_booking():
    client = _get_client()

    platforms = client.list_platforms(name=_TEST_PLATFORM_NAME)

    assert len(platforms) > 0

    target_platform = platforms[0]

    now = _get_now_paris()
    booking_start = now + timedelta(days=30)
    booking_finish = booking_start + timedelta(hours=2)
    booking_description = "my lovely booking"

    try:
        _ = client.create_session(
            platform_id=target_platform.id,
            booking_demand_started_at=booking_start,
            booking_demand_finished_at=booking_finish,
            booking_demand_description=booking_description,
        )
    except Exception as e:
        assert "max_planification_duration not respected" in str(e)


def test_create_too_close_booking():
    client = _get_client()

    platforms = client.list_platforms(name=_TEST_PLATFORM_NAME)

    assert len(platforms) > 0

    target_platform = platforms[0]

    now = _get_now_paris()
    booking_start = now + timedelta(seconds=10)
    booking_finish = booking_start + timedelta(hours=2)
    booking_description = "my lovely booking"

    try:
        _ = client.create_session(
            platform_id=target_platform.id,
            booking_demand_started_at=booking_start,
            booking_demand_finished_at=booking_finish,
            booking_demand_description=booking_description,
        )
    except Exception as e:
        assert "min_planification_duration not respected" in str(e)


def test_stop_too_close_booking():
    client = _get_client()

    platforms = client.list_platforms(name=_TEST_PLATFORM_NAME)

    assert len(platforms) > 0

    target_platform = platforms[0]

    now = _get_now_paris()
    booking_start = now + timedelta(seconds=20)
    booking_finish = booking_start + timedelta(seconds=30)
    booking_description = "my lovely booking"

    try:
        session = client.create_session(
            platform_id=target_platform.id,
            booking_demand_started_at=booking_start,
            booking_demand_finished_at=booking_finish,
            booking_demand_description=booking_description,
        )

        time.sleep(15)

        session = client.terminate_session(session.id)

        while True:
            session = client.get_session(session.id)

            assert session.status in ["starting", "running"]

            if session.status == "running":
                break

    except Exception as e:
        assert "max_cancellation_time passed" in str(e)

    while True:
        session = client.get_session(session.id)

        assert session.status in ["starting", "running", "stopped"]

        if session.status == "stopped":
            break


def test_cannot_start_not_booked_session_during_booked_session_is_running():
    client = _get_client()

    platforms = client.list_platforms(name=_TEST_PLATFORM_NAME)

    assert len(platforms) > 0

    target_platform = platforms[0]

    now = _get_now_paris()
    booking_start = now + timedelta(seconds=20)
    booking_finish = booking_start + timedelta(seconds=20)
    booking_description = "my booking"

    booked_session = client.create_session(
        platform_id=target_platform.id,
        booking_demand_started_at=booking_start,
        booking_demand_finished_at=booking_finish,
        booking_demand_description=booking_description,
    )

    while True:
        time.sleep(2)
        booked_session = client.get_session(session_id=booked_session.id)

        assert booked_session.status in ["starting", "running"]

        if booked_session.status == "running":
            break

    not_booked_session = client.create_session(
        platform_id=target_platform.id,
    )

    while True:
        time.sleep(2)
        not_booked_session = client.get_session(session_id=not_booked_session.id)
        booked_session = client.get_session(session_id=booked_session.id)

        assert (
            not_booked_session.status == "starting"
            if booked_session.status == "running"
            else "running"
        )
        assert booked_session.status in ["running", "stopping", "stopped"]

        if booked_session.status == "stopped":
            break

    while True:
        time.sleep(2)
        not_booked_session = client.get_session(session_id=not_booked_session.id)

        assert not_booked_session.status in ["starting", "running"]

        if not_booked_session.status == "running":
            break

    client.delete_session(not_booked_session.id)


def test_not_booked_session_is_killed_when_booked_session_starts():
    client = _get_client()

    platforms = client.list_platforms(name=_TEST_PLATFORM_NAME)

    assert len(platforms) > 0

    target_platform = platforms[0]

    try:
        not_booked_session_1 = client.create_session(
            platform_id=target_platform.id,
        )

        assert not_booked_session_1

        not_booked_session_2 = client.create_session(
            platform_id=target_platform.id,
        )

        assert not_booked_session_2

        now = _get_now_paris()
        booking_start = now + timedelta(seconds=20)
        booking_finish = booking_start + timedelta(seconds=20)
        booking_description = "my booking"

        booked_session = client.create_session(
            platform_id=target_platform.id,
            booking_demand_started_at=booking_start,
            booking_demand_finished_at=booking_finish,
            booking_demand_description=booking_description,
        )

        while True:
            time.sleep(2)

            not_booked_session_1 = client.get_session(
                session_id=not_booked_session_1.id
            )
            not_booked_session_2 = client.get_session(
                session_id=not_booked_session_2.id
            )
            booked_session = client.get_session(session_id=booked_session.id)

            assert not_booked_session_1.status in ["starting", "running"]
            assert not_booked_session_2.status in ["starting", "running"]
            assert booked_session.status in ["starting"]

            if (
                not_booked_session_1.status == "running"
                and not_booked_session_2.status == "running"
            ):
                break

        while True:
            time.sleep(2)

            booked_session = client.get_session(session_id=booked_session.id)

            assert booked_session.status in ["starting", "running"]

            if booked_session.status == "running":
                break

        while True:
            time.sleep(2)

            not_booked_session_1 = client.get_session(
                session_id=not_booked_session_1.id
            )
            not_booked_session_2 = client.get_session(
                session_id=not_booked_session_2.id
            )

            assert not_booked_session_1.status in ["running", "stopping", "stopped"]
            assert not_booked_session_2.status in ["running", "stopping", "stopped"]

            if (
                not_booked_session_1.status == "stopped"
                and not_booked_session_2.status == "stopped"
            ):
                break

        while True:
            booked_session = client.get_session(booked_session.id)

            assert booked_session.status in ["running", "stopped"]

            if booked_session.status == "stopped":
                break

    finally:
        client.delete_session(not_booked_session_1.id)
        client.delete_session(not_booked_session_2.id)
        client.delete_session(booked_session.id)
