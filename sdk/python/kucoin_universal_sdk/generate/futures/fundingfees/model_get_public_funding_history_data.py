# coding: utf-8

# Code generated by Kucoin Universal SDK Generator; DO NOT EDIT.

from __future__ import annotations
import pprint
import json

from pydantic import BaseModel, ConfigDict, Field
from typing import Any, ClassVar, Dict, List, Optional


class GetPublicFundingHistoryData(BaseModel):
    """
    GetPublicFundingHistoryData

    Attributes:
        symbol (str): Symbol of the contract. Please refer to [Get Symbol endpoint: symbol](https://www.kucoin.com/docs-new/api-3470220) 
        funding_rate (float): Funding rate
        timepoint (int): Time point (milliseconds)  
    """

    symbol: Optional[str] = Field(
        default=None,
        description=
        "Symbol of the contract. Please refer to [Get Symbol endpoint: symbol](https://www.kucoin.com/docs-new/api-3470220) "
    )
    funding_rate: Optional[float] = Field(default=None,
                                          description="Funding rate",
                                          alias="fundingRate")
    timepoint: Optional[int] = Field(default=None,
                                     description="Time point (milliseconds)  ")

    __properties: ClassVar[List[str]] = ["symbol", "fundingRate", "timepoint"]

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=False,
        protected_namespaces=(),
    )

    def to_str(self) -> str:
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        return self.model_dump_json(by_alias=True, exclude_none=True)

    @classmethod
    def from_json(cls, json_str: str) -> Optional[GetPublicFundingHistoryData]:
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        _dict = self.model_dump(
            by_alias=True,
            exclude_none=True,
        )
        return _dict

    @classmethod
    def from_dict(
        cls,
        obj: Optional[Dict[str,
                           Any]]) -> Optional[GetPublicFundingHistoryData]:
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "symbol": obj.get("symbol"),
            "fundingRate": obj.get("fundingRate"),
            "timepoint": obj.get("timepoint")
        })
        return _obj
