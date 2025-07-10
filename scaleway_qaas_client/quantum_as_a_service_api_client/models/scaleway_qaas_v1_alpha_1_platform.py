from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.scaleway_qaas_v1_alpha_1_platform_availability import (
    ScalewayQaasV1Alpha1PlatformAvailability,
)
from ..models.scaleway_qaas_v1_alpha_1_platform_technology import (
    ScalewayQaasV1Alpha1PlatformTechnology,
)
from ..models.scaleway_qaas_v1_alpha_1_platform_type import (
    ScalewayQaasV1Alpha1PlatformType,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.scaleway_qaas_v1_alpha_1_platform_booking_requirement import (
        ScalewayQaasV1Alpha1PlatformBookingRequirement,
    )
    from ..models.scaleway_qaas_v1_alpha_1_platform_hardware import (
        ScalewayQaasV1Alpha1PlatformHardware,
    )
    from ..models.scaleway_qaas_v1_alpha_1_platform_price_per_circuit import (
        ScalewayQaasV1Alpha1PlatformPricePerCircuit,
    )
    from ..models.scaleway_qaas_v1_alpha_1_platform_price_per_hour import (
        ScalewayQaasV1Alpha1PlatformPricePerHour,
    )
    from ..models.scaleway_qaas_v1_alpha_1_platform_price_per_shot import (
        ScalewayQaasV1Alpha1PlatformPricePerShot,
    )


T = TypeVar("T", bound="ScalewayQaasV1Alpha1Platform")


@_attrs_define
class ScalewayQaasV1Alpha1Platform:
    """
    Attributes:
        id (Union[Unset, str]): Unique ID of the platform.
        version (Union[Unset, str]): Version of the platform.
        name (Union[Unset, str]): Name of the platform.
        provider_name (Union[Unset, str]): Provider name of the platform.
        backend_name (Union[Unset, str]): Name of the running backend over the platform (ascella, qsim, aer...).
        type_ (Union[Unset, ScalewayQaasV1Alpha1PlatformType]): Type of the platform. Default:
            ScalewayQaasV1Alpha1PlatformType.UNKNOWN_TYPE.
        technology (Union[Unset, ScalewayQaasV1Alpha1PlatformTechnology]): Technology used by the platform. Default:
            ScalewayQaasV1Alpha1PlatformTechnology.UNKNOWN_TECHNOLOGY.
        max_qubit_count (Union[Unset, int]): Estimated maximum number of qubits supported by the platform.
        max_shot_count (Union[Unset, int]): Maximum number of shots during a circuit execution.
        max_circuit_count (Union[Unset, int]): Maximum number of circuit that can be executed in one call.
        availability (Union[Unset, ScalewayQaasV1Alpha1PlatformAvailability]): Availability of the platform. Default:
            ScalewayQaasV1Alpha1PlatformAvailability.UNKNOWN_AVAILABILITY.
        metadata (Union[Unset, str]): Metadata provided by the platform.
        price_per_hour (Union[Unset, ScalewayQaasV1Alpha1PlatformPricePerHour]): Price to be paid per hour (excluding
            free tiers).
        price_per_shot (Union[Unset, ScalewayQaasV1Alpha1PlatformPricePerShot]): Price to be paid per shot (excluding
            free tiers).
        price_per_circuit (Union[Unset, ScalewayQaasV1Alpha1PlatformPricePerCircuit]): Price to be paid per circuit
            setup before its execution (excluding free tiers).
        hardware (Union[Unset, ScalewayQaasV1Alpha1PlatformHardware]): Specifications of the underlying hardware.
        booking_requirement (Union[Unset, ScalewayQaasV1Alpha1PlatformBookingRequirement]): Booking constraints to fit
            if the platform is bookable.
        description (Union[Unset, str]): English description of the platform.
        documentation_url (Union[Unset, str]): Documentation link to external documentation to learn more on this
            platform.
        is_bookable (Union[Unset, bool]): Specify if the platform is bookable.
    """

    id: Union[Unset, str] = UNSET
    version: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    provider_name: Union[Unset, str] = UNSET
    backend_name: Union[Unset, str] = UNSET
    type_: Union[Unset, ScalewayQaasV1Alpha1PlatformType] = (
        ScalewayQaasV1Alpha1PlatformType.UNKNOWN_TYPE
    )
    technology: Union[Unset, ScalewayQaasV1Alpha1PlatformTechnology] = (
        ScalewayQaasV1Alpha1PlatformTechnology.UNKNOWN_TECHNOLOGY
    )
    max_qubit_count: Union[Unset, int] = UNSET
    max_shot_count: Union[Unset, int] = UNSET
    max_circuit_count: Union[Unset, int] = UNSET
    availability: Union[Unset, ScalewayQaasV1Alpha1PlatformAvailability] = (
        ScalewayQaasV1Alpha1PlatformAvailability.UNKNOWN_AVAILABILITY
    )
    metadata: Union[Unset, str] = UNSET
    price_per_hour: Union[Unset, "ScalewayQaasV1Alpha1PlatformPricePerHour"] = UNSET
    price_per_shot: Union[Unset, "ScalewayQaasV1Alpha1PlatformPricePerShot"] = UNSET
    price_per_circuit: Union[Unset, "ScalewayQaasV1Alpha1PlatformPricePerCircuit"] = (
        UNSET
    )
    hardware: Union[Unset, "ScalewayQaasV1Alpha1PlatformHardware"] = UNSET
    booking_requirement: Union[
        Unset, "ScalewayQaasV1Alpha1PlatformBookingRequirement"
    ] = UNSET
    description: Union[Unset, str] = UNSET
    documentation_url: Union[Unset, str] = UNSET
    is_bookable: Union[Unset, bool] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        version = self.version

        name = self.name

        provider_name = self.provider_name

        backend_name = self.backend_name

        type_: Union[Unset, str] = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        technology: Union[Unset, str] = UNSET
        if not isinstance(self.technology, Unset):
            technology = self.technology.value

        max_qubit_count = self.max_qubit_count

        max_shot_count = self.max_shot_count

        max_circuit_count = self.max_circuit_count

        availability: Union[Unset, str] = UNSET
        if not isinstance(self.availability, Unset):
            availability = self.availability.value

        metadata = self.metadata

        price_per_hour: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.price_per_hour, Unset):
            price_per_hour = self.price_per_hour.to_dict()

        price_per_shot: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.price_per_shot, Unset):
            price_per_shot = self.price_per_shot.to_dict()

        price_per_circuit: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.price_per_circuit, Unset):
            price_per_circuit = self.price_per_circuit.to_dict()

        hardware: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.hardware, Unset):
            hardware = self.hardware.to_dict()

        booking_requirement: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.booking_requirement, Unset):
            booking_requirement = self.booking_requirement.to_dict()

        description = self.description

        documentation_url = self.documentation_url

        is_bookable = self.is_bookable

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if version is not UNSET:
            field_dict["version"] = version
        if name is not UNSET:
            field_dict["name"] = name
        if provider_name is not UNSET:
            field_dict["provider_name"] = provider_name
        if backend_name is not UNSET:
            field_dict["backend_name"] = backend_name
        if type_ is not UNSET:
            field_dict["type"] = type_
        if technology is not UNSET:
            field_dict["technology"] = technology
        if max_qubit_count is not UNSET:
            field_dict["max_qubit_count"] = max_qubit_count
        if max_shot_count is not UNSET:
            field_dict["max_shot_count"] = max_shot_count
        if max_circuit_count is not UNSET:
            field_dict["max_circuit_count"] = max_circuit_count
        if availability is not UNSET:
            field_dict["availability"] = availability
        if metadata is not UNSET:
            field_dict["metadata"] = metadata
        if price_per_hour is not UNSET:
            field_dict["price_per_hour"] = price_per_hour
        if price_per_shot is not UNSET:
            field_dict["price_per_shot"] = price_per_shot
        if price_per_circuit is not UNSET:
            field_dict["price_per_circuit"] = price_per_circuit
        if hardware is not UNSET:
            field_dict["hardware"] = hardware
        if booking_requirement is not UNSET:
            field_dict["booking_requirement"] = booking_requirement
        if description is not UNSET:
            field_dict["description"] = description
        if documentation_url is not UNSET:
            field_dict["documentation_url"] = documentation_url
        if is_bookable is not UNSET:
            field_dict["is_bookable"] = is_bookable

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.scaleway_qaas_v1_alpha_1_platform_booking_requirement import (
            ScalewayQaasV1Alpha1PlatformBookingRequirement,
        )
        from ..models.scaleway_qaas_v1_alpha_1_platform_hardware import (
            ScalewayQaasV1Alpha1PlatformHardware,
        )
        from ..models.scaleway_qaas_v1_alpha_1_platform_price_per_circuit import (
            ScalewayQaasV1Alpha1PlatformPricePerCircuit,
        )
        from ..models.scaleway_qaas_v1_alpha_1_platform_price_per_hour import (
            ScalewayQaasV1Alpha1PlatformPricePerHour,
        )
        from ..models.scaleway_qaas_v1_alpha_1_platform_price_per_shot import (
            ScalewayQaasV1Alpha1PlatformPricePerShot,
        )

        d = dict(src_dict)
        id = d.pop("id", UNSET)

        version = d.pop("version", UNSET)

        name = d.pop("name", UNSET)

        provider_name = d.pop("provider_name", UNSET)

        backend_name = d.pop("backend_name", UNSET)

        _type_ = d.pop("type", UNSET)
        type_: Union[Unset, ScalewayQaasV1Alpha1PlatformType]
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = ScalewayQaasV1Alpha1PlatformType(_type_)

        _technology = d.pop("technology", UNSET)
        technology: Union[Unset, ScalewayQaasV1Alpha1PlatformTechnology]
        if isinstance(_technology, Unset):
            technology = UNSET
        else:
            technology = ScalewayQaasV1Alpha1PlatformTechnology(_technology)

        max_qubit_count = d.pop("max_qubit_count", UNSET)

        max_shot_count = d.pop("max_shot_count", UNSET)

        max_circuit_count = d.pop("max_circuit_count", UNSET)

        _availability = d.pop("availability", UNSET)
        availability: Union[Unset, ScalewayQaasV1Alpha1PlatformAvailability]
        if isinstance(_availability, Unset):
            availability = UNSET
        else:
            availability = ScalewayQaasV1Alpha1PlatformAvailability(_availability)

        metadata = d.pop("metadata", UNSET)

        _price_per_hour = d.pop("price_per_hour", UNSET)
        price_per_hour: Union[Unset, ScalewayQaasV1Alpha1PlatformPricePerHour]
        if isinstance(_price_per_hour, Unset):
            price_per_hour = UNSET
        else:
            price_per_hour = ScalewayQaasV1Alpha1PlatformPricePerHour.from_dict(
                _price_per_hour
            )

        _price_per_shot = d.pop("price_per_shot", UNSET)
        price_per_shot: Union[Unset, ScalewayQaasV1Alpha1PlatformPricePerShot]
        if isinstance(_price_per_shot, Unset):
            price_per_shot = UNSET
        else:
            price_per_shot = ScalewayQaasV1Alpha1PlatformPricePerShot.from_dict(
                _price_per_shot
            )

        _price_per_circuit = d.pop("price_per_circuit", UNSET)
        price_per_circuit: Union[Unset, ScalewayQaasV1Alpha1PlatformPricePerCircuit]
        if isinstance(_price_per_circuit, Unset):
            price_per_circuit = UNSET
        else:
            price_per_circuit = ScalewayQaasV1Alpha1PlatformPricePerCircuit.from_dict(
                _price_per_circuit
            )

        _hardware = d.pop("hardware", UNSET)
        hardware: Union[Unset, ScalewayQaasV1Alpha1PlatformHardware]
        if isinstance(_hardware, Unset):
            hardware = UNSET
        else:
            hardware = ScalewayQaasV1Alpha1PlatformHardware.from_dict(_hardware)

        _booking_requirement = d.pop("booking_requirement", UNSET)
        booking_requirement: Union[
            Unset, ScalewayQaasV1Alpha1PlatformBookingRequirement
        ]
        if isinstance(_booking_requirement, Unset):
            booking_requirement = UNSET
        else:
            booking_requirement = (
                ScalewayQaasV1Alpha1PlatformBookingRequirement.from_dict(
                    _booking_requirement
                )
            )

        description = d.pop("description", UNSET)

        documentation_url = d.pop("documentation_url", UNSET)

        is_bookable = d.pop("is_bookable", UNSET)

        scaleway_qaas_v1_alpha_1_platform = cls(
            id=id,
            version=version,
            name=name,
            provider_name=provider_name,
            backend_name=backend_name,
            type_=type_,
            technology=technology,
            max_qubit_count=max_qubit_count,
            max_shot_count=max_shot_count,
            max_circuit_count=max_circuit_count,
            availability=availability,
            metadata=metadata,
            price_per_hour=price_per_hour,
            price_per_shot=price_per_shot,
            price_per_circuit=price_per_circuit,
            hardware=hardware,
            booking_requirement=booking_requirement,
            description=description,
            documentation_url=documentation_url,
            is_bookable=is_bookable,
        )

        scaleway_qaas_v1_alpha_1_platform.additional_properties = d
        return scaleway_qaas_v1_alpha_1_platform

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
