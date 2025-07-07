from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.scaleway_qaas_v1_alpha_1_session import ScalewayQaasV1Alpha1Session


T = TypeVar("T", bound="ScalewayQaasV1Alpha1ListSessionsResponse")


@_attrs_define
class ScalewayQaasV1Alpha1ListSessionsResponse:
    """
    Attributes:
        total_count (Union[Unset, int]): Total number of sessions.
        sessions (Union[Unset, list['ScalewayQaasV1Alpha1Session']]): List of sessions.
    """

    total_count: Union[Unset, int] = UNSET
    sessions: Union[Unset, list["ScalewayQaasV1Alpha1Session"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        total_count = self.total_count

        sessions: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.sessions, Unset):
            sessions = []
            for sessions_item_data in self.sessions:
                sessions_item = sessions_item_data.to_dict()
                sessions.append(sessions_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if total_count is not UNSET:
            field_dict["total_count"] = total_count
        if sessions is not UNSET:
            field_dict["sessions"] = sessions

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.scaleway_qaas_v1_alpha_1_session import (
            ScalewayQaasV1Alpha1Session,
        )

        d = dict(src_dict)
        total_count = d.pop("total_count", UNSET)

        sessions = []
        _sessions = d.pop("sessions", UNSET)
        for sessions_item_data in _sessions or []:
            sessions_item = ScalewayQaasV1Alpha1Session.from_dict(sessions_item_data)

            sessions.append(sessions_item)

        scaleway_qaas_v1_alpha_1_list_sessions_response = cls(
            total_count=total_count,
            sessions=sessions,
        )

        scaleway_qaas_v1_alpha_1_list_sessions_response.additional_properties = d
        return scaleway_qaas_v1_alpha_1_list_sessions_response

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
