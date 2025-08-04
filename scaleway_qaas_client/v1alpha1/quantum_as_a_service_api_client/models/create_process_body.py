from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CreateProcessBody")


@_attrs_define
class CreateProcessBody:
    """
    Attributes:
        project_id (str): ID of the project in which the process was created. (UUID format) Example:
            6170692e-7363-616c-6577-61792e636f6d.
        platform_id (Union[None, str]): ID of the platform for which the process was created.
        application_id (Union[None, str]): ID of the application for which the process was created.
        name (Union[Unset, str]): Name of the process.
        input_ (Union[None, Unset, str]): Process parameters in JSON format.
        tags (Union[Unset, list[str]]): Tags of the process.
    """

    project_id: str
    platform_id: Union[None, str]
    application_id: Union[None, str]
    name: Union[Unset, str] = UNSET
    input_: Union[None, Unset, str] = UNSET
    tags: Union[Unset, list[str]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        project_id = self.project_id

        platform_id: Union[None, str]
        platform_id = self.platform_id

        application_id: Union[None, str]
        application_id = self.application_id

        name = self.name

        input_: Union[None, Unset, str]
        if isinstance(self.input_, Unset):
            input_ = UNSET
        else:
            input_ = self.input_

        tags: Union[Unset, list[str]] = UNSET
        if not isinstance(self.tags, Unset):
            tags = self.tags

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "project_id": project_id,
                "platform_id": platform_id,
                "application_id": application_id,
            }
        )
        if name is not UNSET:
            field_dict["name"] = name
        if input_ is not UNSET:
            field_dict["input"] = input_
        if tags is not UNSET:
            field_dict["tags"] = tags

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        project_id = d.pop("project_id")

        def _parse_platform_id(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        platform_id = _parse_platform_id(d.pop("platform_id"))

        def _parse_application_id(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        application_id = _parse_application_id(d.pop("application_id"))

        name = d.pop("name", UNSET)

        def _parse_input_(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        input_ = _parse_input_(d.pop("input", UNSET))

        tags = cast(list[str], d.pop("tags", UNSET))

        create_process_body = cls(
            project_id=project_id,
            platform_id=platform_id,
            application_id=application_id,
            name=name,
            input_=input_,
            tags=tags,
        )

        create_process_body.additional_properties = d
        return create_process_body

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
