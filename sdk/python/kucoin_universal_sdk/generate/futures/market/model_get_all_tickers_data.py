# coding: utf-8

# Code generated by Kucoin Universal SDK Generator; DO NOT EDIT.

from __future__ import annotations
import pprint
import json

from enum import Enum
from pydantic import BaseModel, ConfigDict, Field
from typing import Any, ClassVar, Dict, List, Optional


class GetAllTickersData(BaseModel):
    """
    GetAllTickersData

    Attributes:
        sequence (int): Sequence number, used to judge whether the messages pushed by Websocket are continuous.
        symbol (str): Symbol
        side (SideEnum): Trade direction
        size (int): Filled side; the trade side indicates the taker order side. A taker order is the order that was matched with orders opened on the order book.
        trade_id (str): Transaction ID
        price (str): Filled price
        best_bid_price (str): Best bid price
        best_bid_size (int): Best bid size
        best_ask_price (str): Best ask price
        best_ask_size (int): Best ask size
        ts (int): Filled time (nanoseconds)
    """

    class SideEnum(Enum):
        """
        Attributes:
            BUY: 
            SELL: 
        """
        BUY = 'buy'
        SELL = 'sell'

    sequence: Optional[int] = Field(
        default=None,
        description=
        "Sequence number, used to judge whether the messages pushed by Websocket are continuous."
    )
    symbol: Optional[str] = Field(default=None, description="Symbol")
    side: Optional[SideEnum] = Field(default=None,
                                     description="Trade direction")
    size: Optional[int] = Field(
        default=None,
        description=
        "Filled side; the trade side indicates the taker order side. A taker order is the order that was matched with orders opened on the order book."
    )
    trade_id: Optional[str] = Field(default=None,
                                    description="Transaction ID",
                                    alias="tradeId")
    price: Optional[str] = Field(default=None, description="Filled price")
    best_bid_price: Optional[str] = Field(default=None,
                                          description="Best bid price",
                                          alias="bestBidPrice")
    best_bid_size: Optional[int] = Field(default=None,
                                         description="Best bid size",
                                         alias="bestBidSize")
    best_ask_price: Optional[str] = Field(default=None,
                                          description="Best ask price",
                                          alias="bestAskPrice")
    best_ask_size: Optional[int] = Field(default=None,
                                         description="Best ask size",
                                         alias="bestAskSize")
    ts: Optional[int] = Field(default=None,
                              description="Filled time (nanoseconds)")

    __properties: ClassVar[List[str]] = [
        "sequence", "symbol", "side", "size", "tradeId", "price",
        "bestBidPrice", "bestBidSize", "bestAskPrice", "bestAskSize", "ts"
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
    def from_json(cls, json_str: str) -> Optional[GetAllTickersData]:
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        _dict = self.model_dump(
            by_alias=True,
            exclude_none=True,
        )
        return _dict

    @classmethod
    def from_dict(
            cls, obj: Optional[Dict[str, Any]]) -> Optional[GetAllTickersData]:
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "sequence": obj.get("sequence"),
            "symbol": obj.get("symbol"),
            "side": obj.get("side"),
            "size": obj.get("size"),
            "tradeId": obj.get("tradeId"),
            "price": obj.get("price"),
            "bestBidPrice": obj.get("bestBidPrice"),
            "bestBidSize": obj.get("bestBidSize"),
            "bestAskPrice": obj.get("bestAskPrice"),
            "bestAskSize": obj.get("bestAskSize"),
            "ts": obj.get("ts")
        })
        return _obj
