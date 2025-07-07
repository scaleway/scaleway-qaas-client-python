from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.scaleway_qaas_v1_alpha_1_application_type import (
    ScalewayQaasV1Alpha1ApplicationType,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="ScalewayQaasV1Alpha1Application")


@_attrs_define
class ScalewayQaasV1Alpha1Application:
    """
    Attributes:
        id (Union[Unset, str]): Unique ID of the application.
        name (Union[Unset, str]): Name of the application.
        type_ (Union[Unset, ScalewayQaasV1Alpha1ApplicationType]): Type of the application. Default:
            ScalewayQaasV1Alpha1ApplicationType.UNKNOWN_TYPE.
        compatible_platform_ids (Union[Unset, list[str]]): List of compatible platform (by IDs) able to run this
            application.
        input_template (Union[Unset, str]): JSON format describing the expected input.
    """

    id: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    type_: Union[Unset, ScalewayQaasV1Alpha1ApplicationType] = (
        ScalewayQaasV1Alpha1ApplicationType.UNKNOWN_TYPE
    )
    compatible_platform_ids: Union[Unset, list[str]] = UNSET
    input_template: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        type_: Union[Unset, str] = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        compatible_platform_ids: Union[Unset, list[str]] = UNSET
        if not isinstance(self.compatible_platform_ids, Unset):
            compatible_platform_ids = self.compatible_platform_ids

        input_template = self.input_template

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if type_ is not UNSET:
            field_dict["type"] = type_
        if compatible_platform_ids is not UNSET:
            field_dict["compatible_platform_ids"] = compatible_platform_ids
        if input_template is not UNSET:
            field_dict["input_template"] = input_template

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        _type_ = d.pop("type", UNSET)
        type_: Union[Unset, ScalewayQaasV1Alpha1ApplicationType]
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = ScalewayQaasV1Alpha1ApplicationType(_type_)

        compatible_platform_ids = cast(
            list[str], d.pop("compatible_platform_ids", UNSET)
        )

        input_template = d.pop("input_template", UNSET)

        scaleway_qaas_v1_alpha_1_application = cls(
            id=id,
            name=name,
            type_=type_,
            compatible_platform_ids=compatible_platform_ids,
            input_template=input_template,
        )

        scaleway_qaas_v1_alpha_1_application.additional_properties = d
        return scaleway_qaas_v1_alpha_1_application

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
