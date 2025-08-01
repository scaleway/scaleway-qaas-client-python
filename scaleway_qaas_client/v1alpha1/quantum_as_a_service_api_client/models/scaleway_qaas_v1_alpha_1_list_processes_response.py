from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.scaleway_qaas_v1_alpha_1_process import ScalewayQaasV1Alpha1Process


T = TypeVar("T", bound="ScalewayQaasV1Alpha1ListProcessesResponse")


@_attrs_define
class ScalewayQaasV1Alpha1ListProcessesResponse:
    """
    Attributes:
        total_count (Union[Unset, int]): Total number of processes.
        processes (Union[Unset, list['ScalewayQaasV1Alpha1Process']]): List of processes.
    """

    total_count: Union[Unset, int] = UNSET
    processes: Union[Unset, list["ScalewayQaasV1Alpha1Process"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        total_count = self.total_count

        processes: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.processes, Unset):
            processes = []
            for processes_item_data in self.processes:
                processes_item = processes_item_data.to_dict()
                processes.append(processes_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if total_count is not UNSET:
            field_dict["total_count"] = total_count
        if processes is not UNSET:
            field_dict["processes"] = processes

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.scaleway_qaas_v1_alpha_1_process import (
            ScalewayQaasV1Alpha1Process,
        )

        d = dict(src_dict)
        total_count = d.pop("total_count", UNSET)

        processes = []
        _processes = d.pop("processes", UNSET)
        for processes_item_data in _processes or []:
            processes_item = ScalewayQaasV1Alpha1Process.from_dict(processes_item_data)

            processes.append(processes_item)

        scaleway_qaas_v1_alpha_1_list_processes_response = cls(
            total_count=total_count,
            processes=processes,
        )

        scaleway_qaas_v1_alpha_1_list_processes_response.additional_properties = d
        return scaleway_qaas_v1_alpha_1_list_processes_response

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
