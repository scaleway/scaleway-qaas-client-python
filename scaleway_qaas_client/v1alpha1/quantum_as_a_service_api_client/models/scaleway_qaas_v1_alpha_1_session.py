import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.scaleway_qaas_v1_alpha_1_session_origin_type import (
    ScalewayQaasV1Alpha1SessionOriginType,
)
from ..models.scaleway_qaas_v1_alpha_1_session_status import (
    ScalewayQaasV1Alpha1SessionStatus,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="ScalewayQaasV1Alpha1Session")


@_attrs_define
class ScalewayQaasV1Alpha1Session:
    """
    Attributes:
        id (Union[Unset, str]): Unique ID of the session.
        name (Union[Unset, str]): Name of the session.
        platform_id (Union[Unset, str]): Platform ID for which the session has been created.
        created_at (Union[None, Unset, datetime.datetime]): The time at which the session was created. (RFC 3339 format)
            Example: 2022-03-22T12:34:56.123456Z.
        started_at (Union[None, Unset, datetime.datetime]): The time at which the session started. (RFC 3339 format)
            Example: 2022-03-22T12:34:56.123456Z.
        updated_at (Union[None, Unset, datetime.datetime]): The time at which the session was updated. (RFC 3339 format)
            Example: 2022-03-22T12:34:56.123456Z.
        terminated_at (Union[None, Unset, datetime.datetime]): The time at which the session was terminated. (RFC 3339
            format) Example: 2022-03-22T12:34:56.123456Z.
        max_idle_duration (Union[None, Unset, str]): Maximum idle time before the session ends. (in seconds) Example:
            2.5s.
        max_duration (Union[None, Unset, str]): Maximum duration before the session ends. (in seconds) Example: 2.5s.
        waiting_job_count (Union[Unset, int]): Number of waiting jobs linked to the session.
        finished_job_count (Union[Unset, int]): Number of finished jobs linked to the session.
        status (Union[Unset, ScalewayQaasV1Alpha1SessionStatus]): Status of the session. Default:
            ScalewayQaasV1Alpha1SessionStatus.UNKNOWN_STATUS.
        project_id (Union[Unset, str]): Project ID in which the session has been created.
        tags (Union[None, Unset, list[str]]): Tags of the session.
        deduplication_id (Union[Unset, str]): Deduplication ID of the session.
        origin_type (Union[Unset, ScalewayQaasV1Alpha1SessionOriginType]): Resource type that creates the session.
            Default: ScalewayQaasV1Alpha1SessionOriginType.UNKNOWN_ORIGIN_TYPE.
        origin_id (Union[None, Unset, str]): Unique ID of the session's origin resource (if exists).
        progress_message (Union[None, Unset, str]): Any progress of the session.
        booking_id (Union[None, Unset, str]): An optional booking unique ID of an attached booking.
    """

    id: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    platform_id: Union[Unset, str] = UNSET
    created_at: Union[None, Unset, datetime.datetime] = UNSET
    started_at: Union[None, Unset, datetime.datetime] = UNSET
    updated_at: Union[None, Unset, datetime.datetime] = UNSET
    terminated_at: Union[None, Unset, datetime.datetime] = UNSET
    max_idle_duration: Union[None, Unset, str] = UNSET
    max_duration: Union[None, Unset, str] = UNSET
    waiting_job_count: Union[Unset, int] = UNSET
    finished_job_count: Union[Unset, int] = UNSET
    status: Union[Unset, ScalewayQaasV1Alpha1SessionStatus] = (
        ScalewayQaasV1Alpha1SessionStatus.UNKNOWN_STATUS
    )
    project_id: Union[Unset, str] = UNSET
    tags: Union[None, Unset, list[str]] = UNSET
    deduplication_id: Union[Unset, str] = UNSET
    origin_type: Union[Unset, ScalewayQaasV1Alpha1SessionOriginType] = (
        ScalewayQaasV1Alpha1SessionOriginType.UNKNOWN_ORIGIN_TYPE
    )
    origin_id: Union[None, Unset, str] = UNSET
    progress_message: Union[None, Unset, str] = UNSET
    booking_id: Union[None, Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        platform_id = self.platform_id

        created_at: Union[None, Unset, str]
        if isinstance(self.created_at, Unset):
            created_at = UNSET
        elif isinstance(self.created_at, datetime.datetime):
            created_at = self.created_at.isoformat()
        else:
            created_at = self.created_at

        started_at: Union[None, Unset, str]
        if isinstance(self.started_at, Unset):
            started_at = UNSET
        elif isinstance(self.started_at, datetime.datetime):
            started_at = self.started_at.isoformat()
        else:
            started_at = self.started_at

        updated_at: Union[None, Unset, str]
        if isinstance(self.updated_at, Unset):
            updated_at = UNSET
        elif isinstance(self.updated_at, datetime.datetime):
            updated_at = self.updated_at.isoformat()
        else:
            updated_at = self.updated_at

        terminated_at: Union[None, Unset, str]
        if isinstance(self.terminated_at, Unset):
            terminated_at = UNSET
        elif isinstance(self.terminated_at, datetime.datetime):
            terminated_at = self.terminated_at.isoformat()
        else:
            terminated_at = self.terminated_at

        max_idle_duration: Union[None, Unset, str]
        if isinstance(self.max_idle_duration, Unset):
            max_idle_duration = UNSET
        else:
            max_idle_duration = self.max_idle_duration

        max_duration: Union[None, Unset, str]
        if isinstance(self.max_duration, Unset):
            max_duration = UNSET
        else:
            max_duration = self.max_duration

        waiting_job_count = self.waiting_job_count

        finished_job_count = self.finished_job_count

        status: Union[Unset, str] = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        project_id = self.project_id

        tags: Union[None, Unset, list[str]]
        if isinstance(self.tags, Unset):
            tags = UNSET
        elif isinstance(self.tags, list):
            tags = self.tags

        else:
            tags = self.tags

        deduplication_id = self.deduplication_id

        origin_type: Union[Unset, str] = UNSET
        if not isinstance(self.origin_type, Unset):
            origin_type = self.origin_type.value

        origin_id: Union[None, Unset, str]
        if isinstance(self.origin_id, Unset):
            origin_id = UNSET
        else:
            origin_id = self.origin_id

        progress_message: Union[None, Unset, str]
        if isinstance(self.progress_message, Unset):
            progress_message = UNSET
        else:
            progress_message = self.progress_message

        booking_id: Union[None, Unset, str]
        if isinstance(self.booking_id, Unset):
            booking_id = UNSET
        else:
            booking_id = self.booking_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if platform_id is not UNSET:
            field_dict["platform_id"] = platform_id
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if started_at is not UNSET:
            field_dict["started_at"] = started_at
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at
        if terminated_at is not UNSET:
            field_dict["terminated_at"] = terminated_at
        if max_idle_duration is not UNSET:
            field_dict["max_idle_duration"] = max_idle_duration
        if max_duration is not UNSET:
            field_dict["max_duration"] = max_duration
        if waiting_job_count is not UNSET:
            field_dict["waiting_job_count"] = waiting_job_count
        if finished_job_count is not UNSET:
            field_dict["finished_job_count"] = finished_job_count
        if status is not UNSET:
            field_dict["status"] = status
        if project_id is not UNSET:
            field_dict["project_id"] = project_id
        if tags is not UNSET:
            field_dict["tags"] = tags
        if deduplication_id is not UNSET:
            field_dict["deduplication_id"] = deduplication_id
        if origin_type is not UNSET:
            field_dict["origin_type"] = origin_type
        if origin_id is not UNSET:
            field_dict["origin_id"] = origin_id
        if progress_message is not UNSET:
            field_dict["progress_message"] = progress_message
        if booking_id is not UNSET:
            field_dict["booking_id"] = booking_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        platform_id = d.pop("platform_id", UNSET)

        def _parse_created_at(data: object) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                created_at_type_0 = isoparse(data)

                return created_at_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.datetime], data)

        created_at = _parse_created_at(d.pop("created_at", UNSET))

        def _parse_started_at(data: object) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                started_at_type_0 = isoparse(data)

                return started_at_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.datetime], data)

        started_at = _parse_started_at(d.pop("started_at", UNSET))

        def _parse_updated_at(data: object) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                updated_at_type_0 = isoparse(data)

                return updated_at_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.datetime], data)

        updated_at = _parse_updated_at(d.pop("updated_at", UNSET))

        def _parse_terminated_at(data: object) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                terminated_at_type_0 = isoparse(data)

                return terminated_at_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.datetime], data)

        terminated_at = _parse_terminated_at(d.pop("terminated_at", UNSET))

        def _parse_max_idle_duration(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        max_idle_duration = _parse_max_idle_duration(d.pop("max_idle_duration", UNSET))

        def _parse_max_duration(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        max_duration = _parse_max_duration(d.pop("max_duration", UNSET))

        waiting_job_count = d.pop("waiting_job_count", UNSET)

        finished_job_count = d.pop("finished_job_count", UNSET)

        _status = d.pop("status", UNSET)
        status: Union[Unset, ScalewayQaasV1Alpha1SessionStatus]
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = ScalewayQaasV1Alpha1SessionStatus(_status)

        project_id = d.pop("project_id", UNSET)

        def _parse_tags(data: object) -> Union[None, Unset, list[str]]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                tags_type_0 = cast(list[str], data)

                return tags_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, list[str]], data)

        tags = _parse_tags(d.pop("tags", UNSET))

        deduplication_id = d.pop("deduplication_id", UNSET)

        _origin_type = d.pop("origin_type", UNSET)
        origin_type: Union[Unset, ScalewayQaasV1Alpha1SessionOriginType]
        if isinstance(_origin_type, Unset):
            origin_type = UNSET
        else:
            origin_type = ScalewayQaasV1Alpha1SessionOriginType(_origin_type)

        def _parse_origin_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        origin_id = _parse_origin_id(d.pop("origin_id", UNSET))

        def _parse_progress_message(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        progress_message = _parse_progress_message(d.pop("progress_message", UNSET))

        def _parse_booking_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        booking_id = _parse_booking_id(d.pop("booking_id", UNSET))

        scaleway_qaas_v1_alpha_1_session = cls(
            id=id,
            name=name,
            platform_id=platform_id,
            created_at=created_at,
            started_at=started_at,
            updated_at=updated_at,
            terminated_at=terminated_at,
            max_idle_duration=max_idle_duration,
            max_duration=max_duration,
            waiting_job_count=waiting_job_count,
            finished_job_count=finished_job_count,
            status=status,
            project_id=project_id,
            tags=tags,
            deduplication_id=deduplication_id,
            origin_type=origin_type,
            origin_id=origin_id,
            progress_message=progress_message,
            booking_id=booking_id,
        )

        scaleway_qaas_v1_alpha_1_session.additional_properties = d
        return scaleway_qaas_v1_alpha_1_session

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
