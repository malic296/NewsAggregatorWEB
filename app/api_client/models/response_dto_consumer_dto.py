from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.consumer_dto import ConsumerDTO


T = TypeVar("T", bound="ResponseDTOConsumerDTO")


@_attrs_define
class ResponseDTOConsumerDTO:
    """
    Attributes:
        success (bool):
        message (str):
        status_code (int):
        data (ConsumerDTO | None | Unset):
    """

    success: bool
    message: str
    status_code: int
    data: ConsumerDTO | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.consumer_dto import ConsumerDTO

        success = self.success

        message = self.message

        status_code = self.status_code

        data: dict[str, Any] | None | Unset
        if isinstance(self.data, Unset):
            data = UNSET
        elif isinstance(self.data, ConsumerDTO):
            data = self.data.to_dict()
        else:
            data = self.data

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "success": success,
                "message": message,
                "status_code": status_code,
            }
        )
        if data is not UNSET:
            field_dict["data"] = data

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.consumer_dto import ConsumerDTO

        d = dict(src_dict)
        success = d.pop("success")

        message = d.pop("message")

        status_code = d.pop("status_code")

        def _parse_data(data: object) -> ConsumerDTO | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                data_type_0 = ConsumerDTO.from_dict(data)

                return data_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(ConsumerDTO | None | Unset, data)

        data = _parse_data(d.pop("data", UNSET))

        response_dto_consumer_dto = cls(
            success=success,
            message=message,
            status_code=status_code,
            data=data,
        )

        response_dto_consumer_dto.additional_properties = d
        return response_dto_consumer_dto

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
