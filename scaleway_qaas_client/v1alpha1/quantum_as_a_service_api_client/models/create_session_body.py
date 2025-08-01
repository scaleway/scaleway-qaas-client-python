from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.create_session_body_booking_demand import (
        CreateSessionBodyBookingDemand,
    )


T = TypeVar("T", bound="CreateSessionBody")


@_attrs_define
class CreateSessionBody:
    """
    Attributes:
        project_id (str): ID of the Project in which the session was created. (UUID format) Example:
            6170692e-7363-616c-6577-61792e636f6d.
        platform_id (str): ID of the Platform for which the session was created.
        name (Union[None, Unset, str]): Name of the session.
        max_idle_duration (Union[None, Unset, str]): Maximum idle duration before the session ends. (in seconds)
            Example: 2.5s.
        max_duration (Union[None, Unset, str]): Maximum duration before the session ends. (in seconds) Example: 2.5s.
        tags (Union[None, Unset, list[str]]): Tags of the session.
        deduplication_id (Union[None, Unset, str]): Deduplication ID of the session.
        booking_demand (Union[Unset, CreateSessionBodyBookingDemand]): A booking demand to schedule the session, only
            applicable if the platform is bookable.
    """

    project_id: str
    platform_id: str
    name: Union[None, Unset, str] = UNSET
    max_idle_duration: Union[None, Unset, str] = UNSET
    max_duration: Union[None, Unset, str] = UNSET
    tags: Union[None, Unset, list[str]] = UNSET
    deduplication_id: Union[None, Unset, str] = UNSET
    booking_demand: Union[Unset, "CreateSessionBodyBookingDemand"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        project_id = self.project_id

        platform_id = self.platform_id

        name: Union[None, Unset, str]
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

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

        tags: Union[None, Unset, list[str]]
        if isinstance(self.tags, Unset):
            tags = UNSET
        elif isinstance(self.tags, list):
            tags = self.tags

        else:
            tags = self.tags

        deduplication_id: Union[None, Unset, str]
        if isinstance(self.deduplication_id, Unset):
            deduplication_id = UNSET
        else:
            deduplication_id = self.deduplication_id

        booking_demand: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.booking_demand, Unset):
            booking_demand = self.booking_demand.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "project_id": project_id,
                "platform_id": platform_id,
            }
        )
        if name is not UNSET:
            field_dict["name"] = name
        if max_idle_duration is not UNSET:
            field_dict["max_idle_duration"] = max_idle_duration
        if max_duration is not UNSET:
            field_dict["max_duration"] = max_duration
        if tags is not UNSET:
            field_dict["tags"] = tags
        if deduplication_id is not UNSET:
            field_dict["deduplication_id"] = deduplication_id
        if booking_demand is not UNSET:
            field_dict["booking_demand"] = booking_demand

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.create_session_body_booking_demand import (
            CreateSessionBodyBookingDemand,
        )

        d = dict(src_dict)
        project_id = d.pop("project_id")

        platform_id = d.pop("platform_id")

        def _parse_name(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        name = _parse_name(d.pop("name", UNSET))

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

        def _parse_deduplication_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        deduplication_id = _parse_deduplication_id(d.pop("deduplication_id", UNSET))

        _booking_demand = d.pop("booking_demand", UNSET)
        booking_demand: Union[Unset, CreateSessionBodyBookingDemand]
        if isinstance(_booking_demand, Unset):
            booking_demand = UNSET
        else:
            booking_demand = CreateSessionBodyBookingDemand.from_dict(_booking_demand)

        create_session_body = cls(
            project_id=project_id,
            platform_id=platform_id,
            name=name,
            max_idle_duration=max_idle_duration,
            max_duration=max_duration,
            tags=tags,
            deduplication_id=deduplication_id,
            booking_demand=booking_demand,
        )

        create_session_body.additional_properties = d
        return create_session_body

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
