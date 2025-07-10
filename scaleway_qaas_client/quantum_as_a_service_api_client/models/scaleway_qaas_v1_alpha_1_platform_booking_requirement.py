from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ScalewayQaasV1Alpha1PlatformBookingRequirement")


@_attrs_define
class ScalewayQaasV1Alpha1PlatformBookingRequirement:
    """Booking constraints to fit if the platform is bookable.

    Attributes:
        min_duration (Union[None, Unset, str]): Minimal duration of any booking based on this platform. (in seconds)
            Example: 2.5s.
        max_duration (Union[None, Unset, str]): Maximal duration of any bookings based on this platform. (in seconds)
            Example: 2.5s.
        max_cancellation_duration (Union[None, Unset, str]): Allowed time to cancel a booking attached to this platform
            before the beginning of the session. (in seconds) Example: 2.5s.
        max_planification_duration (Union[None, Unset, str]): Allowed planification time from now where the platform can
            be booked in the future. (in seconds) Example: 2.5s.
    """

    min_duration: Union[None, Unset, str] = UNSET
    max_duration: Union[None, Unset, str] = UNSET
    max_cancellation_duration: Union[None, Unset, str] = UNSET
    max_planification_duration: Union[None, Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        min_duration: Union[None, Unset, str]
        if isinstance(self.min_duration, Unset):
            min_duration = UNSET
        else:
            min_duration = self.min_duration

        max_duration: Union[None, Unset, str]
        if isinstance(self.max_duration, Unset):
            max_duration = UNSET
        else:
            max_duration = self.max_duration

        max_cancellation_duration: Union[None, Unset, str]
        if isinstance(self.max_cancellation_duration, Unset):
            max_cancellation_duration = UNSET
        else:
            max_cancellation_duration = self.max_cancellation_duration

        max_planification_duration: Union[None, Unset, str]
        if isinstance(self.max_planification_duration, Unset):
            max_planification_duration = UNSET
        else:
            max_planification_duration = self.max_planification_duration

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if min_duration is not UNSET:
            field_dict["min_duration"] = min_duration
        if max_duration is not UNSET:
            field_dict["max_duration"] = max_duration
        if max_cancellation_duration is not UNSET:
            field_dict["max_cancellation_duration"] = max_cancellation_duration
        if max_planification_duration is not UNSET:
            field_dict["max_planification_duration"] = max_planification_duration

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_min_duration(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        min_duration = _parse_min_duration(d.pop("min_duration", UNSET))

        def _parse_max_duration(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        max_duration = _parse_max_duration(d.pop("max_duration", UNSET))

        def _parse_max_cancellation_duration(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        max_cancellation_duration = _parse_max_cancellation_duration(
            d.pop("max_cancellation_duration", UNSET)
        )

        def _parse_max_planification_duration(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        max_planification_duration = _parse_max_planification_duration(
            d.pop("max_planification_duration", UNSET)
        )

        scaleway_qaas_v1_alpha_1_platform_booking_requirement = cls(
            min_duration=min_duration,
            max_duration=max_duration,
            max_cancellation_duration=max_cancellation_duration,
            max_planification_duration=max_planification_duration,
        )

        scaleway_qaas_v1_alpha_1_platform_booking_requirement.additional_properties = d
        return scaleway_qaas_v1_alpha_1_platform_booking_requirement

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
