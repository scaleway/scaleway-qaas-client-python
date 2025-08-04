from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.scaleway_qaas_v1_alpha_1_session_access import (
    ScalewayQaasV1Alpha1SessionAccess,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="ScalewayQaasV1Alpha1ListSessionACLsResponse")


@_attrs_define
class ScalewayQaasV1Alpha1ListSessionACLsResponse:
    """
    Attributes:
        total_count (Union[Unset, int]):
        acls (Union[Unset, list[ScalewayQaasV1Alpha1SessionAccess]]):
    """

    total_count: Union[Unset, int] = UNSET
    acls: Union[Unset, list[ScalewayQaasV1Alpha1SessionAccess]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        total_count = self.total_count

        acls: Union[Unset, list[str]] = UNSET
        if not isinstance(self.acls, Unset):
            acls = []
            for acls_item_data in self.acls:
                acls_item = acls_item_data.value
                acls.append(acls_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if total_count is not UNSET:
            field_dict["total_count"] = total_count
        if acls is not UNSET:
            field_dict["acls"] = acls

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        total_count = d.pop("total_count", UNSET)

        acls = []
        _acls = d.pop("acls", UNSET)
        for acls_item_data in _acls or []:
            acls_item = ScalewayQaasV1Alpha1SessionAccess(acls_item_data)

            acls.append(acls_item)

        scaleway_qaas_v1_alpha_1_list_session_ac_ls_response = cls(
            total_count=total_count,
            acls=acls,
        )

        scaleway_qaas_v1_alpha_1_list_session_ac_ls_response.additional_properties = d
        return scaleway_qaas_v1_alpha_1_list_session_ac_ls_response

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
