# Code generated by Kucoin Universal SDK Generator; DO NOT EDIT.

from abc import ABC, abstractmethod
from typing import Any
from kucoin_universal_sdk.internal.interfaces.transport import Transport
from .model_add_sub_account_api_req import AddSubAccountApiReq
from .model_add_sub_account_api_resp import AddSubAccountApiResp
from .model_add_sub_account_futures_permission_req import AddSubAccountFuturesPermissionReq
from .model_add_sub_account_futures_permission_resp import AddSubAccountFuturesPermissionResp
from .model_add_sub_account_margin_permission_req import AddSubAccountMarginPermissionReq
from .model_add_sub_account_margin_permission_resp import AddSubAccountMarginPermissionResp
from .model_add_sub_account_req import AddSubAccountReq
from .model_add_sub_account_resp import AddSubAccountResp
from .model_delete_sub_account_api_req import DeleteSubAccountApiReq
from .model_delete_sub_account_api_resp import DeleteSubAccountApiResp
from .model_get_futures_sub_account_list_v2_req import GetFuturesSubAccountListV2Req
from .model_get_futures_sub_account_list_v2_resp import GetFuturesSubAccountListV2Resp
from .model_get_spot_sub_account_detail_req import GetSpotSubAccountDetailReq
from .model_get_spot_sub_account_detail_resp import GetSpotSubAccountDetailResp
from .model_get_spot_sub_account_list_v1_resp import GetSpotSubAccountListV1Resp
from .model_get_spot_sub_account_list_v2_req import GetSpotSubAccountListV2Req
from .model_get_spot_sub_account_list_v2_resp import GetSpotSubAccountListV2Resp
from .model_get_spot_sub_accounts_summary_v1_resp import GetSpotSubAccountsSummaryV1Resp
from .model_get_spot_sub_accounts_summary_v2_req import GetSpotSubAccountsSummaryV2Req
from .model_get_spot_sub_accounts_summary_v2_resp import GetSpotSubAccountsSummaryV2Resp
from .model_get_sub_account_api_list_req import GetSubAccountApiListReq
from .model_get_sub_account_api_list_resp import GetSubAccountApiListResp
from .model_modify_sub_account_api_req import ModifySubAccountApiReq
from .model_modify_sub_account_api_resp import ModifySubAccountApiResp
from typing_extensions import deprecated


class SubAccountAPI(ABC):

    @abstractmethod
    def add_sub_account(self, req: AddSubAccountReq,
                        **kwargs: Any) -> AddSubAccountResp:
        """
        summary: Add sub-account
        description: This endpoint can be used to create sub-accounts.
        documentation: https://www.kucoin.com/docs-new/api-3470135
        +-----------------------+------------+
        | Extra API Info        | Value      |
        +-----------------------+------------+
        | API-DOMAIN            | SPOT       |
        | API-CHANNEL           | PRIVATE    |
        | API-PERMISSION        | GENERAL    |
        | API-RATE-LIMIT-POOL   | MANAGEMENT |
        | API-RATE-LIMIT-WEIGHT | 15         |
        +-----------------------+------------+
        """
        pass

    @abstractmethod
    def add_sub_account_margin_permission(
            self, req: AddSubAccountMarginPermissionReq,
            **kwargs: Any) -> AddSubAccountMarginPermissionResp:
        """
        summary: Add sub-account Margin Permission
        description: This endpoint can be used to add sub-account Margin permissions. Before using this endpoint, you need to ensure that the master account apikey has Margin permissions and the Margin function has been activated.
        documentation: https://www.kucoin.com/docs-new/api-3470331
        +-----------------------+------------+
        | Extra API Info        | Value      |
        +-----------------------+------------+
        | API-DOMAIN            | SPOT       |
        | API-CHANNEL           | PRIVATE    |
        | API-PERMISSION        | MARGIN     |
        | API-RATE-LIMIT-POOL   | MANAGEMENT |
        | API-RATE-LIMIT-WEIGHT | 15         |
        +-----------------------+------------+
        """
        pass

    @abstractmethod
    def add_sub_account_futures_permission(
            self, req: AddSubAccountFuturesPermissionReq,
            **kwargs: Any) -> AddSubAccountFuturesPermissionResp:
        """
        summary: Add sub-account Futures Permission
        description: This endpoint can be used to add sub-account Futures permissions. Before using this endpoint, you need to ensure that the master account apikey has Futures permissions and the Futures function has been activated.
        documentation: https://www.kucoin.com/docs-new/api-3470332
        +-----------------------+------------+
        | Extra API Info        | Value      |
        +-----------------------+------------+
        | API-DOMAIN            | SPOT       |
        | API-CHANNEL           | PRIVATE    |
        | API-PERMISSION        | FUTURES    |
        | API-RATE-LIMIT-POOL   | MANAGEMENT |
        | API-RATE-LIMIT-WEIGHT | 15         |
        +-----------------------+------------+
        """
        pass

    @abstractmethod
    def get_spot_sub_accounts_summary_v2(
            self, req: GetSpotSubAccountsSummaryV2Req,
            **kwargs: Any) -> GetSpotSubAccountsSummaryV2Resp:
        """
        summary: Get sub-account List - Summary Info
        description: This endpoint can be used to get a paginated list of sub-accounts. Pagination is required.
        documentation: https://www.kucoin.com/docs-new/api-3470131
        +-----------------------+------------+
        | Extra API Info        | Value      |
        +-----------------------+------------+
        | API-DOMAIN            | SPOT       |
        | API-CHANNEL           | PRIVATE    |
        | API-PERMISSION        | GENERAL    |
        | API-RATE-LIMIT-POOL   | MANAGEMENT |
        | API-RATE-LIMIT-WEIGHT | 20         |
        +-----------------------+------------+
        """
        pass

    @abstractmethod
    def get_spot_sub_account_detail(
            self, req: GetSpotSubAccountDetailReq,
            **kwargs: Any) -> GetSpotSubAccountDetailResp:
        """
        summary: Get sub-account Detail - Balance
        description: This endpoint returns the account info of a sub-user specified by the subUserId.
        documentation: https://www.kucoin.com/docs-new/api-3470132
        +-----------------------+------------+
        | Extra API Info        | Value      |
        +-----------------------+------------+
        | API-DOMAIN            | SPOT       |
        | API-CHANNEL           | PRIVATE    |
        | API-PERMISSION        | GENERAL    |
        | API-RATE-LIMIT-POOL   | MANAGEMENT |
        | API-RATE-LIMIT-WEIGHT | 15         |
        +-----------------------+------------+
        """
        pass

    @abstractmethod
    def get_spot_sub_account_list_v2(
            self, req: GetSpotSubAccountListV2Req,
            **kwargs: Any) -> GetSpotSubAccountListV2Resp:
        """
        summary: Get sub-account List - Spot Balance (V2)
        description: This endpoint can be used to get paginated Spot sub-account information. Pagination is required.
        documentation: https://www.kucoin.com/docs-new/api-3470133
        +-----------------------+------------+
        | Extra API Info        | Value      |
        +-----------------------+------------+
        | API-DOMAIN            | SPOT       |
        | API-CHANNEL           | PRIVATE    |
        | API-PERMISSION        | GENERAL    |
        | API-RATE-LIMIT-POOL   | MANAGEMENT |
        | API-RATE-LIMIT-WEIGHT | 20         |
        +-----------------------+------------+
        """
        pass

    @abstractmethod
    def get_futures_sub_account_list_v2(
            self, req: GetFuturesSubAccountListV2Req,
            **kwargs: Any) -> GetFuturesSubAccountListV2Resp:
        """
        summary: Get sub-account List - Futures Balance (V2)
        description: This endpoint can be used to get Futures sub-account information. 
        documentation: https://www.kucoin.com/docs-new/api-3470134
        +-----------------------+---------+
        | Extra API Info        | Value   |
        +-----------------------+---------+
        | API-DOMAIN            | FUTURES |
        | API-CHANNEL           | PRIVATE |
        | API-PERMISSION        | GENERAL |
        | API-RATE-LIMIT-POOL   | FUTURES |
        | API-RATE-LIMIT-WEIGHT | 6       |
        +-----------------------+---------+
        """
        pass

    @abstractmethod
    def add_sub_account_api(self, req: AddSubAccountApiReq,
                            **kwargs: Any) -> AddSubAccountApiResp:
        """
        summary: Add sub-account API
        description: This endpoint can be used to create APIs for sub-accounts.
        documentation: https://www.kucoin.com/docs-new/api-3470138
        +-----------------------+------------+
        | Extra API Info        | Value      |
        +-----------------------+------------+
        | API-DOMAIN            | SPOT       |
        | API-CHANNEL           | PRIVATE    |
        | API-PERMISSION        | GENERAL    |
        | API-RATE-LIMIT-POOL   | MANAGEMENT |
        | API-RATE-LIMIT-WEIGHT | 20         |
        +-----------------------+------------+
        """
        pass

    @abstractmethod
    def modify_sub_account_api(self, req: ModifySubAccountApiReq,
                               **kwargs: Any) -> ModifySubAccountApiResp:
        """
        summary: Modify sub-account API
        description: This endpoint can be used to modify sub-account APIs.
        documentation: https://www.kucoin.com/docs-new/api-3470139
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

    @abstractmethod
    def get_sub_account_api_list(self, req: GetSubAccountApiListReq,
                                 **kwargs: Any) -> GetSubAccountApiListResp:
        """
        summary: Get sub-account API List
        description: This endpoint can be used to obtain a list of APIs pertaining to a sub-account (not including ND broker sub-accounts).
        documentation: https://www.kucoin.com/docs-new/api-3470136
        +-----------------------+------------+
        | Extra API Info        | Value      |
        +-----------------------+------------+
        | API-DOMAIN            | SPOT       |
        | API-CHANNEL           | PRIVATE    |
        | API-PERMISSION        | GENERAL    |
        | API-RATE-LIMIT-POOL   | MANAGEMENT |
        | API-RATE-LIMIT-WEIGHT | 20         |
        +-----------------------+------------+
        """
        pass

    @abstractmethod
    def delete_sub_account_api(self, req: DeleteSubAccountApiReq,
                               **kwargs: Any) -> DeleteSubAccountApiResp:
        """
        summary: Delete sub-account API
        description: This endpoint can be used to delete sub-account APIs.
        documentation: https://www.kucoin.com/docs-new/api-3470137
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

    @abstractmethod
    @deprecated('')
    def get_spot_sub_accounts_summary_v1(
            self, **kwargs: Any) -> GetSpotSubAccountsSummaryV1Resp:
        """
        summary: Get sub-account List - Summary Info (V1)
        description: You can get the user info of all sub-account via this interface; it is recommended to use the GET /api/v2/sub/user interface for paging query
        documentation: https://www.kucoin.com/docs-new/api-3470298
        +-----------------------+------------+
        | Extra API Info        | Value      |
        +-----------------------+------------+
        | API-DOMAIN            | SPOT       |
        | API-CHANNEL           | PRIVATE    |
        | API-PERMISSION        | GENERAL    |
        | API-RATE-LIMIT-POOL   | MANAGEMENT |
        | API-RATE-LIMIT-WEIGHT | 20         |
        +-----------------------+------------+
        """
        pass

    @abstractmethod
    @deprecated('')
    def get_spot_sub_account_list_v1(
            self, **kwargs: Any) -> GetSpotSubAccountListV1Resp:
        """
        summary: Get sub-account List - Spot Balance (V1)
        description: This endpoint returns the account info of all sub-users.
        documentation: https://www.kucoin.com/docs-new/api-3470299
        +-----------------------+------------+
        | Extra API Info        | Value      |
        +-----------------------+------------+
        | API-DOMAIN            | SPOT       |
        | API-CHANNEL           | PRIVATE    |
        | API-PERMISSION        | GENERAL    |
        | API-RATE-LIMIT-POOL   | MANAGEMENT |
        | API-RATE-LIMIT-WEIGHT | 20         |
        +-----------------------+------------+
        """
        pass


class SubAccountAPIImpl(SubAccountAPI):

    def __init__(self, transport: Transport):
        self.transport = transport

    def add_sub_account(self, req: AddSubAccountReq,
                        **kwargs: Any) -> AddSubAccountResp:
        return self.transport.call("spot", False, "POST",
                                   "/api/v2/sub/user/created", req,
                                   AddSubAccountResp(), False, **kwargs)

    def add_sub_account_margin_permission(
            self, req: AddSubAccountMarginPermissionReq,
            **kwargs: Any) -> AddSubAccountMarginPermissionResp:
        return self.transport.call("spot", False, "POST",
                                   "/api/v3/sub/user/margin/enable", req,
                                   AddSubAccountMarginPermissionResp(), False,
                                   **kwargs)

    def add_sub_account_futures_permission(
            self, req: AddSubAccountFuturesPermissionReq,
            **kwargs: Any) -> AddSubAccountFuturesPermissionResp:
        return self.transport.call("spot", False, "POST",
                                   "/api/v3/sub/user/futures/enable", req,
                                   AddSubAccountFuturesPermissionResp(), False,
                                   **kwargs)

    def get_spot_sub_accounts_summary_v2(
            self, req: GetSpotSubAccountsSummaryV2Req,
            **kwargs: Any) -> GetSpotSubAccountsSummaryV2Resp:
        return self.transport.call("spot", False, "GET",
                                   "/api/v2/sub/user", req,
                                   GetSpotSubAccountsSummaryV2Resp(), False,
                                   **kwargs)

    def get_spot_sub_account_detail(
            self, req: GetSpotSubAccountDetailReq,
            **kwargs: Any) -> GetSpotSubAccountDetailResp:
        return self.transport.call("spot", False, "GET",
                                   "/api/v1/sub-accounts/{subUserId}", req,
                                   GetSpotSubAccountDetailResp(), False,
                                   **kwargs)

    def get_spot_sub_account_list_v2(
            self, req: GetSpotSubAccountListV2Req,
            **kwargs: Any) -> GetSpotSubAccountListV2Resp:
        return self.transport.call("spot", False, "GET",
                                   "/api/v2/sub-accounts", req,
                                   GetSpotSubAccountListV2Resp(), False,
                                   **kwargs)

    def get_futures_sub_account_list_v2(
            self, req: GetFuturesSubAccountListV2Req,
            **kwargs: Any) -> GetFuturesSubAccountListV2Resp:
        return self.transport.call("futures", False, "GET",
                                   "/api/v1/account-overview-all", req,
                                   GetFuturesSubAccountListV2Resp(), False,
                                   **kwargs)

    def add_sub_account_api(self, req: AddSubAccountApiReq,
                            **kwargs: Any) -> AddSubAccountApiResp:
        return self.transport.call("spot", False, "POST",
                                   "/api/v1/sub/api-key", req,
                                   AddSubAccountApiResp(), False, **kwargs)

    def modify_sub_account_api(self, req: ModifySubAccountApiReq,
                               **kwargs: Any) -> ModifySubAccountApiResp:
        return self.transport.call("spot", False, "POST",
                                   "/api/v1/sub/api-key/update", req,
                                   ModifySubAccountApiResp(), False, **kwargs)

    def get_sub_account_api_list(self, req: GetSubAccountApiListReq,
                                 **kwargs: Any) -> GetSubAccountApiListResp:
        return self.transport.call("spot", False, "GET",
                                   "/api/v1/sub/api-key", req,
                                   GetSubAccountApiListResp(), False, **kwargs)

    def delete_sub_account_api(self, req: DeleteSubAccountApiReq,
                               **kwargs: Any) -> DeleteSubAccountApiResp:
        return self.transport.call("spot", False, "DELETE",
                                   "/api/v1/sub/api-key", req,
                                   DeleteSubAccountApiResp(), False, **kwargs)

    def get_spot_sub_accounts_summary_v1(
            self, **kwargs: Any) -> GetSpotSubAccountsSummaryV1Resp:
        return self.transport.call("spot", False, "GET",
                                   "/api/v1/sub/user", None,
                                   GetSpotSubAccountsSummaryV1Resp(), False,
                                   **kwargs)

    def get_spot_sub_account_list_v1(
            self, **kwargs: Any) -> GetSpotSubAccountListV1Resp:
        return self.transport.call("spot", False, "GET",
                                   "/api/v1/sub-accounts", None,
                                   GetSpotSubAccountListV1Resp(), False,
                                   **kwargs)
