from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.scaleway_qaas_v1_alpha_1_booking import ScalewayQaasV1Alpha1Booking


T = TypeVar("T", bound="ScalewayQaasV1Alpha1ListBookingsResponse")


@_attrs_define
class ScalewayQaasV1Alpha1ListBookingsResponse:
    """
    Attributes:
        total_count (Union[Unset, int]): Total number of bookings.
        bookings (Union[Unset, list['ScalewayQaasV1Alpha1Booking']]): List of bookings.
    """

    total_count: Union[Unset, int] = UNSET
    bookings: Union[Unset, list["ScalewayQaasV1Alpha1Booking"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        total_count = self.total_count

        bookings: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.bookings, Unset):
            bookings = []
            for bookings_item_data in self.bookings:
                bookings_item = bookings_item_data.to_dict()
                bookings.append(bookings_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if total_count is not UNSET:
            field_dict["total_count"] = total_count
        if bookings is not UNSET:
            field_dict["bookings"] = bookings

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.scaleway_qaas_v1_alpha_1_booking import (
            ScalewayQaasV1Alpha1Booking,
        )

        d = dict(src_dict)
        total_count = d.pop("total_count", UNSET)

        bookings = []
        _bookings = d.pop("bookings", UNSET)
        for bookings_item_data in _bookings or []:
            bookings_item = ScalewayQaasV1Alpha1Booking.from_dict(bookings_item_data)

            bookings.append(bookings_item)

        scaleway_qaas_v1_alpha_1_list_bookings_response = cls(
            total_count=total_count,
            bookings=bookings,
        )

        scaleway_qaas_v1_alpha_1_list_bookings_response.additional_properties = d
        return scaleway_qaas_v1_alpha_1_list_bookings_response

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
