import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="ScalewayQaasV1Alpha1JobResult")


@_attrs_define
class ScalewayQaasV1Alpha1JobResult:
    """
    Attributes:
        job_id (Union[Unset, str]): ID of the parent job.
        result (Union[None, Unset, str]): Result in JSON format.
        url (Union[None, Unset, str]): URL to download a large result (optional).
        created_at (Union[None, Unset, datetime.datetime]): Creation time of the result. (RFC 3339 format) Example:
            2022-03-22T12:34:56.123456Z.
    """

    job_id: Union[Unset, str] = UNSET
    result: Union[None, Unset, str] = UNSET
    url: Union[None, Unset, str] = UNSET
    created_at: Union[None, Unset, datetime.datetime] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        job_id = self.job_id

        result: Union[None, Unset, str]
        if isinstance(self.result, Unset):
            result = UNSET
        else:
            result = self.result

        url: Union[None, Unset, str]
        if isinstance(self.url, Unset):
            url = UNSET
        else:
            url = self.url

        created_at: Union[None, Unset, str]
        if isinstance(self.created_at, Unset):
            created_at = UNSET
        elif isinstance(self.created_at, datetime.datetime):
            created_at = self.created_at.isoformat()
        else:
            created_at = self.created_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if job_id is not UNSET:
            field_dict["job_id"] = job_id
        if result is not UNSET:
            field_dict["result"] = result
        if url is not UNSET:
            field_dict["url"] = url
        if created_at is not UNSET:
            field_dict["created_at"] = created_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        job_id = d.pop("job_id", UNSET)

        def _parse_result(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        result = _parse_result(d.pop("result", UNSET))

        def _parse_url(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        url = _parse_url(d.pop("url", UNSET))

        def _parse_created_at(data: object) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                created_at_type_0 = isoparse(data)

                return created_at_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.datetime], data)

        created_at = _parse_created_at(d.pop("created_at", UNSET))

        scaleway_qaas_v1_alpha_1_job_result = cls(
            job_id=job_id,
            result=result,
            url=url,
            created_at=created_at,
        )

        scaleway_qaas_v1_alpha_1_job_result.additional_properties = d
        return scaleway_qaas_v1_alpha_1_job_result

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
