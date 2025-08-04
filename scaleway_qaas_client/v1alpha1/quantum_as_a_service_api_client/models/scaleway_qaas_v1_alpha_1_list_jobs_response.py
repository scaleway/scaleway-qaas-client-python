from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.scaleway_qaas_v1_alpha_1_job import ScalewayQaasV1Alpha1Job


T = TypeVar("T", bound="ScalewayQaasV1Alpha1ListJobsResponse")


@_attrs_define
class ScalewayQaasV1Alpha1ListJobsResponse:
    """
    Attributes:
        total_count (Union[Unset, int]): Total number of jobs.
        jobs (Union[Unset, list['ScalewayQaasV1Alpha1Job']]): List of jobs.
    """

    total_count: Union[Unset, int] = UNSET
    jobs: Union[Unset, list["ScalewayQaasV1Alpha1Job"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        total_count = self.total_count

        jobs: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.jobs, Unset):
            jobs = []
            for jobs_item_data in self.jobs:
                jobs_item = jobs_item_data.to_dict()
                jobs.append(jobs_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if total_count is not UNSET:
            field_dict["total_count"] = total_count
        if jobs is not UNSET:
            field_dict["jobs"] = jobs

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.scaleway_qaas_v1_alpha_1_job import ScalewayQaasV1Alpha1Job

        d = dict(src_dict)
        total_count = d.pop("total_count", UNSET)

        jobs = []
        _jobs = d.pop("jobs", UNSET)
        for jobs_item_data in _jobs or []:
            jobs_item = ScalewayQaasV1Alpha1Job.from_dict(jobs_item_data)

            jobs.append(jobs_item)

        scaleway_qaas_v1_alpha_1_list_jobs_response = cls(
            total_count=total_count,
            jobs=jobs,
        )

        scaleway_qaas_v1_alpha_1_list_jobs_response.additional_properties = d
        return scaleway_qaas_v1_alpha_1_list_jobs_response

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
