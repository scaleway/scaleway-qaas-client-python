from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.scaleway_qaas_v1_alpha_1_model import ScalewayQaasV1Alpha1Model


T = TypeVar("T", bound="ScalewayQaasV1Alpha1ListModelsResponse")


@_attrs_define
class ScalewayQaasV1Alpha1ListModelsResponse:
    """
    Attributes:
        total_count (Union[Unset, int]): Total number of models.
        models (Union[Unset, list['ScalewayQaasV1Alpha1Model']]): List of models.
    """

    total_count: Union[Unset, int] = UNSET
    models: Union[Unset, list["ScalewayQaasV1Alpha1Model"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        total_count = self.total_count

        models: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.models, Unset):
            models = []
            for models_item_data in self.models:
                models_item = models_item_data.to_dict()
                models.append(models_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if total_count is not UNSET:
            field_dict["total_count"] = total_count
        if models is not UNSET:
            field_dict["models"] = models

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.scaleway_qaas_v1_alpha_1_model import ScalewayQaasV1Alpha1Model

        d = dict(src_dict)
        total_count = d.pop("total_count", UNSET)

        models = []
        _models = d.pop("models", UNSET)
        for models_item_data in _models or []:
            models_item = ScalewayQaasV1Alpha1Model.from_dict(models_item_data)

            models.append(models_item)

        scaleway_qaas_v1_alpha_1_list_models_response = cls(
            total_count=total_count,
            models=models,
        )

        scaleway_qaas_v1_alpha_1_list_models_response.additional_properties = d
        return scaleway_qaas_v1_alpha_1_list_models_response

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
