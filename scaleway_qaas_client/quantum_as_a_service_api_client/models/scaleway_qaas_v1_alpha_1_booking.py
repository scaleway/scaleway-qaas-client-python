import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.scaleway_qaas_v1_alpha_1_booking_status import (
    ScalewayQaasV1Alpha1BookingStatus,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="ScalewayQaasV1Alpha1Booking")


@_attrs_define
class ScalewayQaasV1Alpha1Booking:
    """
    Attributes:
        id (Union[Unset, str]): Unique ID of the booking.
        created_at (Union[None, Unset, datetime.datetime]): Time at which the booking was created. (RFC 3339 format)
            Example: 2022-03-22T12:34:56.123456Z.
        started_at (Union[None, Unset, datetime.datetime]): Time at which the booking starts. (RFC 3339 format) Example:
            2022-03-22T12:34:56.123456Z.
        updated_at (Union[None, Unset, datetime.datetime]): Time at which the booking was updated. (RFC 3339 format)
            Example: 2022-03-22T12:34:56.123456Z.
        finished_at (Union[None, Unset, datetime.datetime]): Time at which the booking finishes. (RFC 3339 format)
            Example: 2022-03-22T12:34:56.123456Z.
        status (Union[Unset, ScalewayQaasV1Alpha1BookingStatus]): Status of the booking. Default:
            ScalewayQaasV1Alpha1BookingStatus.UNKNOWN_STATUS.
        description (Union[Unset, str]): Description of the booking slot.
        progress_message (Union[Unset, str]): Any progress message of the booking.
    """

    id: Union[Unset, str] = UNSET
    created_at: Union[None, Unset, datetime.datetime] = UNSET
    started_at: Union[None, Unset, datetime.datetime] = UNSET
    updated_at: Union[None, Unset, datetime.datetime] = UNSET
    finished_at: Union[None, Unset, datetime.datetime] = UNSET
    status: Union[Unset, ScalewayQaasV1Alpha1BookingStatus] = (
        ScalewayQaasV1Alpha1BookingStatus.UNKNOWN_STATUS
    )
    description: Union[Unset, str] = UNSET
    progress_message: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

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

        finished_at: Union[None, Unset, str]
        if isinstance(self.finished_at, Unset):
            finished_at = UNSET
        elif isinstance(self.finished_at, datetime.datetime):
            finished_at = self.finished_at.isoformat()
        else:
            finished_at = self.finished_at

        status: Union[Unset, str] = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        description = self.description

        progress_message = self.progress_message

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if started_at is not UNSET:
            field_dict["started_at"] = started_at
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at
        if finished_at is not UNSET:
            field_dict["finished_at"] = finished_at
        if status is not UNSET:
            field_dict["status"] = status
        if description is not UNSET:
            field_dict["description"] = description
        if progress_message is not UNSET:
            field_dict["progress_message"] = progress_message

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

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

        def _parse_finished_at(data: object) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                finished_at_type_0 = isoparse(data)

                return finished_at_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.datetime], data)

        finished_at = _parse_finished_at(d.pop("finished_at", UNSET))

        _status = d.pop("status", UNSET)
        status: Union[Unset, ScalewayQaasV1Alpha1BookingStatus]
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = ScalewayQaasV1Alpha1BookingStatus(_status)

        description = d.pop("description", UNSET)

        progress_message = d.pop("progress_message", UNSET)

        scaleway_qaas_v1_alpha_1_booking = cls(
            id=id,
            created_at=created_at,
            started_at=started_at,
            updated_at=updated_at,
            finished_at=finished_at,
            status=status,
            description=description,
            progress_message=progress_message,
        )

        scaleway_qaas_v1_alpha_1_booking.additional_properties = d
        return scaleway_qaas_v1_alpha_1_booking

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
