import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.scaleway_qaas_v1_alpha_1_job_status import ScalewayQaasV1Alpha1JobStatus
from ..types import UNSET, Unset

T = TypeVar("T", bound="ScalewayQaasV1Alpha1Job")


@_attrs_define
class ScalewayQaasV1Alpha1Job:
    """
    Attributes:
        id (Union[Unset, str]): Unique ID of the job.
        name (Union[Unset, str]): Job name.
        tags (Union[None, Unset, list[str]]): Tags of the job.
        session_id (Union[Unset, str]): Session ID in which the job is executed.
        created_at (Union[None, Unset, datetime.datetime]): Time at which the job was created. (RFC 3339 format)
            Example: 2022-03-22T12:34:56.123456Z.
        started_at (Union[None, Unset, datetime.datetime]): Time at which the job was started. (RFC 3339 format)
            Example: 2022-03-22T12:34:56.123456Z.
        updated_at (Union[None, Unset, datetime.datetime]): Time at which the job was updated. (RFC 3339 format)
            Example: 2022-03-22T12:34:56.123456Z.
        status (Union[Unset, ScalewayQaasV1Alpha1JobStatus]): Job status. Default:
            ScalewayQaasV1Alpha1JobStatus.UNKNOWN_STATUS.
        progress_message (Union[None, Unset, str]): Last progress message, if the job has started.
        job_duration (Union[None, Unset, str]): Duration of the job, if the job is finished. (in seconds) Example: 2.5s.
        result_distribution (Union[None, Unset, str]): Result of the job, if the job is finished.
    """

    id: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    tags: Union[None, Unset, list[str]] = UNSET
    session_id: Union[Unset, str] = UNSET
    created_at: Union[None, Unset, datetime.datetime] = UNSET
    started_at: Union[None, Unset, datetime.datetime] = UNSET
    updated_at: Union[None, Unset, datetime.datetime] = UNSET
    status: Union[Unset, ScalewayQaasV1Alpha1JobStatus] = (
        ScalewayQaasV1Alpha1JobStatus.UNKNOWN_STATUS
    )
    progress_message: Union[None, Unset, str] = UNSET
    job_duration: Union[None, Unset, str] = UNSET
    result_distribution: Union[None, Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        tags: Union[None, Unset, list[str]]
        if isinstance(self.tags, Unset):
            tags = UNSET
        elif isinstance(self.tags, list):
            tags = self.tags

        else:
            tags = self.tags

        session_id = self.session_id

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

        status: Union[Unset, str] = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        progress_message: Union[None, Unset, str]
        if isinstance(self.progress_message, Unset):
            progress_message = UNSET
        else:
            progress_message = self.progress_message

        job_duration: Union[None, Unset, str]
        if isinstance(self.job_duration, Unset):
            job_duration = UNSET
        else:
            job_duration = self.job_duration

        result_distribution: Union[None, Unset, str]
        if isinstance(self.result_distribution, Unset):
            result_distribution = UNSET
        else:
            result_distribution = self.result_distribution

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if tags is not UNSET:
            field_dict["tags"] = tags
        if session_id is not UNSET:
            field_dict["session_id"] = session_id
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if started_at is not UNSET:
            field_dict["started_at"] = started_at
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at
        if status is not UNSET:
            field_dict["status"] = status
        if progress_message is not UNSET:
            field_dict["progress_message"] = progress_message
        if job_duration is not UNSET:
            field_dict["job_duration"] = job_duration
        if result_distribution is not UNSET:
            field_dict["result_distribution"] = result_distribution

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

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

        session_id = d.pop("session_id", UNSET)

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

        _status = d.pop("status", UNSET)
        status: Union[Unset, ScalewayQaasV1Alpha1JobStatus]
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = ScalewayQaasV1Alpha1JobStatus(_status)

        def _parse_progress_message(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        progress_message = _parse_progress_message(d.pop("progress_message", UNSET))

        def _parse_job_duration(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        job_duration = _parse_job_duration(d.pop("job_duration", UNSET))

        def _parse_result_distribution(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        result_distribution = _parse_result_distribution(
            d.pop("result_distribution", UNSET)
        )

        scaleway_qaas_v1_alpha_1_job = cls(
            id=id,
            name=name,
            tags=tags,
            session_id=session_id,
            created_at=created_at,
            started_at=started_at,
            updated_at=updated_at,
            status=status,
            progress_message=progress_message,
            job_duration=job_duration,
            result_distribution=result_distribution,
        )

        scaleway_qaas_v1_alpha_1_job.additional_properties = d
        return scaleway_qaas_v1_alpha_1_job

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
