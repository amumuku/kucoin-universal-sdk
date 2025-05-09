# Code generated by Kucoin Universal SDK Generator; DO NOT EDIT.

from abc import ABC, abstractmethod
from typing import Any
from kucoin_universal_sdk.internal.interfaces.transport import Transport
from .model_get_account_resp import GetAccountResp


class AffiliateAPI(ABC):

    @abstractmethod
    def get_account(self, **kwargs: Any) -> GetAccountResp:
        """
        summary: Get Account
        description: Affiliate user rebate information can be obtained at this endpoint.
        documentation: https://www.kucoin.com/docs-new/api-3470279
        +-----------------------+------------+
        | Extra API Info        | Value      |
        +-----------------------+------------+
        | API-DOMAIN            | SPOT       |
        | API-CHANNEL           | PRIVATE    |
        | API-PERMISSION        | GENERAL    |
        | API-RATE-LIMIT-POOL   | MANAGEMENT |
        | API-RATE-LIMIT-WEIGHT | 30         |
        +-----------------------+------------+
        """
        pass


class AffiliateAPIImpl(AffiliateAPI):

    def __init__(self, transport: Transport):
        self.transport = transport

    def get_account(self, **kwargs: Any) -> GetAccountResp:
        return self.transport.call("spot", False, "GET",
                                   "/api/v2/affiliate/inviter/statistics",
                                   None, GetAccountResp(), False, **kwargs)
