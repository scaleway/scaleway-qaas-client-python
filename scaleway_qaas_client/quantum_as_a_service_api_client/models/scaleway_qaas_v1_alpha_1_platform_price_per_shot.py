from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ScalewayQaasV1Alpha1PlatformPricePerShot")


@_attrs_define
class ScalewayQaasV1Alpha1PlatformPricePerShot:
    """Price to be paid per shot (excluding free tiers).

    Attributes:
        currency_code (Union[Unset, str]):
        units (Union[Unset, int]):
        nanos (Union[Unset, int]):
    """

    currency_code: Union[Unset, str] = UNSET
    units: Union[Unset, int] = UNSET
    nanos: Union[Unset, int] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        currency_code = self.currency_code

        units = self.units

        nanos = self.nanos

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if currency_code is not UNSET:
            field_dict["currency_code"] = currency_code
        if units is not UNSET:
            field_dict["units"] = units
        if nanos is not UNSET:
            field_dict["nanos"] = nanos

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        currency_code = d.pop("currency_code", UNSET)

        units = d.pop("units", UNSET)

        nanos = d.pop("nanos", UNSET)

        scaleway_qaas_v1_alpha_1_platform_price_per_shot = cls(
            currency_code=currency_code,
            units=units,
            nanos=nanos,
        )

        scaleway_qaas_v1_alpha_1_platform_price_per_shot.additional_properties = d
        return scaleway_qaas_v1_alpha_1_platform_price_per_shot

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
