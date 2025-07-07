from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.create_job_body_circuit import CreateJobBodyCircuit


T = TypeVar("T", bound="CreateJobBody")


@_attrs_define
class CreateJobBody:
    """
    Attributes:
        name (str): Name of the job.
        session_id (str): Session in which the job is executed.
        circuit (CreateJobBodyCircuit): Quantum circuit that should be executed.
        tags (Union[None, Unset, list[str]]): Tags of the job.
        max_duration (Union[None, Unset, str]): Maximum duration of the job. (in seconds) Example: 2.5s.
    """

    name: str
    session_id: str
    circuit: "CreateJobBodyCircuit"
    tags: Union[None, Unset, list[str]] = UNSET
    max_duration: Union[None, Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        session_id = self.session_id

        circuit = self.circuit.to_dict()

        tags: Union[None, Unset, list[str]]
        if isinstance(self.tags, Unset):
            tags = UNSET
        elif isinstance(self.tags, list):
            tags = self.tags

        else:
            tags = self.tags

        max_duration: Union[None, Unset, str]
        if isinstance(self.max_duration, Unset):
            max_duration = UNSET
        else:
            max_duration = self.max_duration

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "session_id": session_id,
                "circuit": circuit,
            }
        )
        if tags is not UNSET:
            field_dict["tags"] = tags
        if max_duration is not UNSET:
            field_dict["max_duration"] = max_duration

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.create_job_body_circuit import CreateJobBodyCircuit

        d = dict(src_dict)
        name = d.pop("name")

        session_id = d.pop("session_id")

        circuit = CreateJobBodyCircuit.from_dict(d.pop("circuit"))

        def _parse_tags(data: object) -> Union[None, Unset, list[str]]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                tags_type_0 = cast(list[str], data)

                return tags_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, list[str]], data)

        tags = _parse_tags(d.pop("tags", UNSET))

        def _parse_max_duration(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        max_duration = _parse_max_duration(d.pop("max_duration", UNSET))

        create_job_body = cls(
            name=name,
            session_id=session_id,
            circuit=circuit,
            tags=tags,
            max_duration=max_duration,
        )

        create_job_body.additional_properties = d
        return create_job_body

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
