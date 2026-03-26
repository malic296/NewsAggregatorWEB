from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ResponseDTONoneType")


@_attrs_define
class ResponseDTONoneType:
    """
    Attributes:
        success (bool):
        message (str):
        status_code (int):
        data (None | Unset):
    """

    success: bool
    message: str
    status_code: int
    data: None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        success = self.success

        message = self.message

        status_code = self.status_code

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
        d = dict(src_dict)
        success = d.pop("success")

        message = d.pop("message")

        status_code = d.pop("status_code")

        data = d.pop("data", UNSET)

        response_dto_none_type = cls(
            success=success,
            message=message,
            status_code=status_code,
            data=data,
        )

        response_dto_none_type.additional_properties = d
        return response_dto_none_type

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
