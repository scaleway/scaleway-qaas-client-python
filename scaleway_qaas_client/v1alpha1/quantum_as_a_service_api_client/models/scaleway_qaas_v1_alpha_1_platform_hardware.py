from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ScalewayQaasV1Alpha1PlatformHardware")


@_attrs_define
class ScalewayQaasV1Alpha1PlatformHardware:
    """Specifications of the underlying hardware.

    Attributes:
        name (Union[Unset, str]): Product name of the hardware.
        vcpus (Union[Unset, int]): Number of vCPUs available.
        gpus (Union[Unset, int]): Number of GPUs available (0 if no GPU).
        gpus_network (Union[Unset, str]): Network topology of GPUs (PCIe, NVLink...).
        ram (Union[Unset, int]): Amount of RAM available in byte.
        vram (Union[Unset, int]): Amount of VRAM available in byte (0 if no GPU).
    """

    name: Union[Unset, str] = UNSET
    vcpus: Union[Unset, int] = UNSET
    gpus: Union[Unset, int] = UNSET
    gpus_network: Union[Unset, str] = UNSET
    ram: Union[Unset, int] = UNSET
    vram: Union[Unset, int] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        vcpus = self.vcpus

        gpus = self.gpus

        gpus_network = self.gpus_network

        ram = self.ram

        vram = self.vram

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if vcpus is not UNSET:
            field_dict["vcpus"] = vcpus
        if gpus is not UNSET:
            field_dict["gpus"] = gpus
        if gpus_network is not UNSET:
            field_dict["gpus_network"] = gpus_network
        if ram is not UNSET:
            field_dict["ram"] = ram
        if vram is not UNSET:
            field_dict["vram"] = vram

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name", UNSET)

        vcpus = d.pop("vcpus", UNSET)

        gpus = d.pop("gpus", UNSET)

        gpus_network = d.pop("gpus_network", UNSET)

        ram = d.pop("ram", UNSET)

        vram = d.pop("vram", UNSET)

        scaleway_qaas_v1_alpha_1_platform_hardware = cls(
            name=name,
            vcpus=vcpus,
            gpus=gpus,
            gpus_network=gpus_network,
            ram=ram,
            vram=vram,
        )

        scaleway_qaas_v1_alpha_1_platform_hardware.additional_properties = d
        return scaleway_qaas_v1_alpha_1_platform_hardware

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
