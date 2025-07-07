from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.scaleway_qaas_v1_alpha_1_platform import ScalewayQaasV1Alpha1Platform


T = TypeVar("T", bound="ScalewayQaasV1Alpha1ListPlatformsResponse")


@_attrs_define
class ScalewayQaasV1Alpha1ListPlatformsResponse:
    """
    Attributes:
        total_count (Union[Unset, int]): Total number of platforms.
        platforms (Union[Unset, list['ScalewayQaasV1Alpha1Platform']]): List of platforms.
    """

    total_count: Union[Unset, int] = UNSET
    platforms: Union[Unset, list["ScalewayQaasV1Alpha1Platform"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        total_count = self.total_count

        platforms: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.platforms, Unset):
            platforms = []
            for platforms_item_data in self.platforms:
                platforms_item = platforms_item_data.to_dict()
                platforms.append(platforms_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if total_count is not UNSET:
            field_dict["total_count"] = total_count
        if platforms is not UNSET:
            field_dict["platforms"] = platforms

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.scaleway_qaas_v1_alpha_1_platform import (
            ScalewayQaasV1Alpha1Platform,
        )

        d = dict(src_dict)
        total_count = d.pop("total_count", UNSET)

        platforms = []
        _platforms = d.pop("platforms", UNSET)
        for platforms_item_data in _platforms or []:
            platforms_item = ScalewayQaasV1Alpha1Platform.from_dict(platforms_item_data)

            platforms.append(platforms_item)

        scaleway_qaas_v1_alpha_1_list_platforms_response = cls(
            total_count=total_count,
            platforms=platforms,
        )

        scaleway_qaas_v1_alpha_1_list_platforms_response.additional_properties = d
        return scaleway_qaas_v1_alpha_1_list_platforms_response

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
