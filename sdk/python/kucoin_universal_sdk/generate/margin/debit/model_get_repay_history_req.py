# coding: utf-8

# Code generated by Kucoin Universal SDK Generator; DO NOT EDIT.

from __future__ import annotations
import pprint
import json

from pydantic import BaseModel, ConfigDict, Field
from typing import Any, ClassVar, Dict, List, Optional


class GetRepayHistoryReq(BaseModel):
    """
    GetRepayHistoryReq

    Attributes:
        currency (str): currency
        is_isolated (bool): true-isolated, false-cross; default is false
        symbol (str): symbol, mandatory for isolated margin account
        order_no (str): Repay order ID
        start_time (int): The start and end times are not restricted. If the start time is empty or less than 1680278400000, the default value is set to 1680278400000 (April 1, 2023, 00:00:00)
        end_time (int): End time
        current_page (int): Current query page, with a starting value of 1. Default:1 
        page_size (int): Number of results per page. Default is 50, minimum is 10, maximum is 500
    """

    currency: Optional[str] = Field(default=None, description="currency")
    is_isolated: Optional[bool] = Field(
        default=False,
        description="true-isolated, false-cross; default is false",
        alias="isIsolated")
    symbol: Optional[str] = Field(
        default=None,
        description="symbol, mandatory for isolated margin account")
    order_no: Optional[str] = Field(default=None,
                                    description="Repay order ID",
                                    alias="orderNo")
    start_time: Optional[int] = Field(
        default=None,
        description=
        "The start and end times are not restricted. If the start time is empty or less than 1680278400000, the default value is set to 1680278400000 (April 1, 2023, 00:00:00)",
        alias="startTime")
    end_time: Optional[int] = Field(default=None,
                                    description="End time",
                                    alias="endTime")
    current_page: Optional[int] = Field(
        default=1,
        description=
        "Current query page, with a starting value of 1. Default:1 ",
        alias="currentPage")
    page_size: Optional[int] = Field(
        default=50,
        description=
        "Number of results per page. Default is 50, minimum is 10, maximum is 500",
        alias="pageSize")

    __properties: ClassVar[List[str]] = [
        "currency", "isIsolated", "symbol", "orderNo", "startTime", "endTime",
        "currentPage", "pageSize"
    ]

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
    def from_json(cls, json_str: str) -> Optional[GetRepayHistoryReq]:
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        _dict = self.model_dump(
            by_alias=True,
            exclude_none=True,
        )
        return _dict

    @classmethod
    def from_dict(
            cls, obj: Optional[Dict[str,
                                    Any]]) -> Optional[GetRepayHistoryReq]:
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "currency":
            obj.get("currency"),
            "isIsolated":
            obj.get("isIsolated")
            if obj.get("isIsolated") is not None else False,
            "symbol":
            obj.get("symbol"),
            "orderNo":
            obj.get("orderNo"),
            "startTime":
            obj.get("startTime"),
            "endTime":
            obj.get("endTime"),
            "currentPage":
            obj.get("currentPage")
            if obj.get("currentPage") is not None else 1,
            "pageSize":
            obj.get("pageSize") if obj.get("pageSize") is not None else 50
        })
        return _obj


class GetRepayHistoryReqBuilder:

    def __init__(self):
        self.obj = {}

    def set_currency(self, value: str) -> GetRepayHistoryReqBuilder:
        """
        currency
        """
        self.obj['currency'] = value
        return self

    def set_is_isolated(self, value: bool) -> GetRepayHistoryReqBuilder:
        """
        true-isolated, false-cross; default is false
        """
        self.obj['isIsolated'] = value
        return self

    def set_symbol(self, value: str) -> GetRepayHistoryReqBuilder:
        """
        symbol, mandatory for isolated margin account
        """
        self.obj['symbol'] = value
        return self

    def set_order_no(self, value: str) -> GetRepayHistoryReqBuilder:
        """
        Repay order ID
        """
        self.obj['orderNo'] = value
        return self

    def set_start_time(self, value: int) -> GetRepayHistoryReqBuilder:
        """
        The start and end times are not restricted. If the start time is empty or less than 1680278400000, the default value is set to 1680278400000 (April 1, 2023, 00:00:00)
        """
        self.obj['startTime'] = value
        return self

    def set_end_time(self, value: int) -> GetRepayHistoryReqBuilder:
        """
        End time
        """
        self.obj['endTime'] = value
        return self

    def set_current_page(self, value: int) -> GetRepayHistoryReqBuilder:
        """
        Current query page, with a starting value of 1. Default:1 
        """
        self.obj['currentPage'] = value
        return self

    def set_page_size(self, value: int) -> GetRepayHistoryReqBuilder:
        """
        Number of results per page. Default is 50, minimum is 10, maximum is 500
        """
        self.obj['pageSize'] = value
        return self

    def build(self) -> GetRepayHistoryReq:
        return GetRepayHistoryReq(**self.obj)
