// Code generated by Kucoin Universal SDK Generator; DO NOT EDIT.

package account

// GetSpotLedgerReq struct for GetSpotLedgerReq
type GetSpotLedgerReq struct {
	// Currency (you can choose more than one currency). You can specify a max. of 10 currencies in one go. If not specified, all currencies will be queried by default.
	Currency *string `json:"currency,omitempty" url:"currency,omitempty"`
	// direction: in, out
	Direction *string `json:"direction,omitempty" url:"direction,omitempty"`
	// Type: DEPOSIT-deposit, WITHDRAW-withdraw, TRANSFER-transfer, SUB_TRANSFER-sub-account transfer, TRADE_EXCHANGE-trade, MARGIN_EXCHANGE-margin trade, KUCOIN_BONUS-bonus, BROKER_TRANSFER-Broker transfer record
	BizType *string `json:"bizType,omitempty" url:"bizType,omitempty"`
	// Start time (milliseconds)
	StartAt *int64 `json:"startAt,omitempty" url:"startAt,omitempty"`
	// End time (milliseconds)
	EndAt *int64 `json:"endAt,omitempty" url:"endAt,omitempty"`
	// Current request page.
	CurrentPage *int32 `json:"currentPage,omitempty" url:"currentPage,omitempty"`
	// Number of results per request. Minimum is 10, maximum is 500.
	PageSize *int32 `json:"pageSize,omitempty" url:"pageSize,omitempty"`
}

// NewGetSpotLedgerReq instantiates a new GetSpotLedgerReq object
// This constructor will assign default values to properties that have it defined
func NewGetSpotLedgerReq() *GetSpotLedgerReq {
	this := GetSpotLedgerReq{}
	var currentPage int32 = 1
	this.CurrentPage = &currentPage
	var pageSize int32 = 50
	this.PageSize = &pageSize
	return &this
}

// NewGetSpotLedgerReqWithDefaults instantiates a new GetSpotLedgerReq object
// This constructor will only assign default values to properties that have it defined,
func NewGetSpotLedgerReqWithDefaults() *GetSpotLedgerReq {
	this := GetSpotLedgerReq{}
	var currentPage int32 = 1
	this.CurrentPage = &currentPage
	var pageSize int32 = 50
	this.PageSize = &pageSize
	return &this
}

func (o *GetSpotLedgerReq) ToMap() map[string]interface{} {
	toSerialize := map[string]interface{}{}
	toSerialize["currency"] = o.Currency
	toSerialize["direction"] = o.Direction
	toSerialize["bizType"] = o.BizType
	toSerialize["startAt"] = o.StartAt
	toSerialize["endAt"] = o.EndAt
	toSerialize["currentPage"] = o.CurrentPage
	toSerialize["pageSize"] = o.PageSize
	return toSerialize
}

type GetSpotLedgerReqBuilder struct {
	obj *GetSpotLedgerReq
}

func NewGetSpotLedgerReqBuilder() *GetSpotLedgerReqBuilder {
	return &GetSpotLedgerReqBuilder{obj: NewGetSpotLedgerReqWithDefaults()}
}

// Currency (you can choose more than one currency). You can specify a max. of 10 currencies in one go. If not specified, all currencies will be queried by default.
func (builder *GetSpotLedgerReqBuilder) SetCurrency(value string) *GetSpotLedgerReqBuilder {
	builder.obj.Currency = &value
	return builder
}

// direction: in, out
func (builder *GetSpotLedgerReqBuilder) SetDirection(value string) *GetSpotLedgerReqBuilder {
	builder.obj.Direction = &value
	return builder
}

// Type: DEPOSIT-deposit, WITHDRAW-withdraw, TRANSFER-transfer, SUB_TRANSFER-sub-account transfer, TRADE_EXCHANGE-trade, MARGIN_EXCHANGE-margin trade, KUCOIN_BONUS-bonus, BROKER_TRANSFER-Broker transfer record
func (builder *GetSpotLedgerReqBuilder) SetBizType(value string) *GetSpotLedgerReqBuilder {
	builder.obj.BizType = &value
	return builder
}

// Start time (milliseconds)
func (builder *GetSpotLedgerReqBuilder) SetStartAt(value int64) *GetSpotLedgerReqBuilder {
	builder.obj.StartAt = &value
	return builder
}

// End time (milliseconds)
func (builder *GetSpotLedgerReqBuilder) SetEndAt(value int64) *GetSpotLedgerReqBuilder {
	builder.obj.EndAt = &value
	return builder
}

// Current request page.
func (builder *GetSpotLedgerReqBuilder) SetCurrentPage(value int32) *GetSpotLedgerReqBuilder {
	builder.obj.CurrentPage = &value
	return builder
}

// Number of results per request. Minimum is 10, maximum is 500.
func (builder *GetSpotLedgerReqBuilder) SetPageSize(value int32) *GetSpotLedgerReqBuilder {
	builder.obj.PageSize = &value
	return builder
}

func (builder *GetSpotLedgerReqBuilder) Build() *GetSpotLedgerReq {
	return builder.obj
}
