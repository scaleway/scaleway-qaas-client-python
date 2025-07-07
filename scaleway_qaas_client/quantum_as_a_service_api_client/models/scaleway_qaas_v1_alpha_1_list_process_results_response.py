from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.scaleway_qaas_v1_alpha_1_process_result import (
        ScalewayQaasV1Alpha1ProcessResult,
    )


T = TypeVar("T", bound="ScalewayQaasV1Alpha1ListProcessResultsResponse")


@_attrs_define
class ScalewayQaasV1Alpha1ListProcessResultsResponse:
    """
    Attributes:
        total_count (Union[Unset, int]): Total number of results.
        process_results (Union[Unset, list['ScalewayQaasV1Alpha1ProcessResult']]): List of results.
    """

    total_count: Union[Unset, int] = UNSET
    process_results: Union[Unset, list["ScalewayQaasV1Alpha1ProcessResult"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        total_count = self.total_count

        process_results: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.process_results, Unset):
            process_results = []
            for process_results_item_data in self.process_results:
                process_results_item = process_results_item_data.to_dict()
                process_results.append(process_results_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if total_count is not UNSET:
            field_dict["total_count"] = total_count
        if process_results is not UNSET:
            field_dict["process_results"] = process_results

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.scaleway_qaas_v1_alpha_1_process_result import (
            ScalewayQaasV1Alpha1ProcessResult,
        )

        d = dict(src_dict)
        total_count = d.pop("total_count", UNSET)

        process_results = []
        _process_results = d.pop("process_results", UNSET)
        for process_results_item_data in _process_results or []:
            process_results_item = ScalewayQaasV1Alpha1ProcessResult.from_dict(
                process_results_item_data
            )

            process_results.append(process_results_item)

        scaleway_qaas_v1_alpha_1_list_process_results_response = cls(
            total_count=total_count,
            process_results=process_results,
        )

        scaleway_qaas_v1_alpha_1_list_process_results_response.additional_properties = d
        return scaleway_qaas_v1_alpha_1_list_process_results_response

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
