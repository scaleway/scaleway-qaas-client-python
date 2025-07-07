import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="ScalewayQaasV1Alpha1ProcessResult")


@_attrs_define
class ScalewayQaasV1Alpha1ProcessResult:
    """
    Attributes:
        process_id (Union[Unset, str]): ID of the parent process.
        result (Union[Unset, str]): Result in JSON format.
        created_at (Union[None, Unset, datetime.datetime]): Creation time of the result. (RFC 3339 format) Example:
            2022-03-22T12:34:56.123456Z.
    """

    process_id: Union[Unset, str] = UNSET
    result: Union[Unset, str] = UNSET
    created_at: Union[None, Unset, datetime.datetime] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        process_id = self.process_id

        result = self.result

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
        if process_id is not UNSET:
            field_dict["process_id"] = process_id
        if result is not UNSET:
            field_dict["result"] = result
        if created_at is not UNSET:
            field_dict["created_at"] = created_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        process_id = d.pop("process_id", UNSET)

        result = d.pop("result", UNSET)

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

        scaleway_qaas_v1_alpha_1_process_result = cls(
            process_id=process_id,
            result=result,
            created_at=created_at,
        )

        scaleway_qaas_v1_alpha_1_process_result.additional_properties = d
        return scaleway_qaas_v1_alpha_1_process_result

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
