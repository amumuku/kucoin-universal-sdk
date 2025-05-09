// Code generated by Kucoin Universal SDK Generator; DO NOT EDIT.

package earn

// GetETHStakingProductsData struct for GetETHStakingProductsData
type GetETHStakingProductsData struct {
	// Product ID
	Id string `json:"id,omitempty"`
	// Product category:  ETH2 (ETH Staking)
	Category string `json:"category,omitempty"`
	// Product subtype: DEMAND (demand)
	Type string `json:"type,omitempty"`
	// Maximum precision supported
	Precision int32 `json:"precision,omitempty"`
	// currency
	Currency string `json:"currency,omitempty"`
	// Income currency
	IncomeCurrency string `json:"incomeCurrency,omitempty"`
	// Annualized Rate of Return, for example, 0.035 is equal to 3.5% annualized rate of return
	ReturnRate string `json:"returnRate,omitempty"`
	// Min. user subscribe amount
	UserLowerLimit string `json:"userLowerLimit,omitempty"`
	// Max. user subscription amount
	UserUpperLimit string `json:"userUpperLimit,omitempty"`
	// Products total subscription amount
	ProductUpperLimit string `json:"productUpperLimit,omitempty"`
	// Remaining product subscription amount
	ProductRemainAmount string `json:"productRemainAmount,omitempty"`
	// Redemption waiting period (days)
	RedeemPeriod int32 `json:"redeemPeriod,omitempty"`
	// Redemption channel: MANUAL (manual redemption), TRANS_DEMAND (transfer to corresponding demand product upon maturity), AUTO (redeem to funding account upon maturity)
	RedeemType string `json:"redeemType,omitempty"`
	// Income release type: DAILY (daily release), AFTER (release after product ends)
	IncomeReleaseType string `json:"incomeReleaseType,omitempty"`
	// Subscription start time, in milliseconds
	ApplyStartTime *int64 `json:"applyStartTime,omitempty"`
	// Subscription end time, in milliseconds
	ApplyEndTime *int64 `json:"applyEndTime,omitempty"`
	// Product earliest interest start time, in milliseconds
	LockStartTime *int64 `json:"lockStartTime,omitempty"`
	// Product maturity time, in milliseconds
	LockEndTime *int64 `json:"lockEndTime,omitempty"`
	// Most recent interest date (milliseconds)
	InterestDate int64 `json:"interestDate,omitempty"`
	// Whether the product is exclusive to new users: 0 (no), 1 (yes)
	NewUserOnly int32 `json:"newUserOnly,omitempty"`
	// Whether the fixed product supports early redemption: 0 (no), 1 (yes)
	EarlyRedeemSupported int32 `json:"earlyRedeemSupported,omitempty"`
	// Product duration (days)
	Duration int32 `json:"duration,omitempty"`
	// Product status: ONGOING (Subscription in progress), PENDING (Preheating Subscription), FULL (Subscribed), INTERESTING (Interest in progress)
	Status string `json:"status,omitempty"`
}

// NewGetETHStakingProductsData instantiates a new GetETHStakingProductsData object
// This constructor will assign default values to properties that have it defined
func NewGetETHStakingProductsData(id string, category string, Type_ string, precision int32, currency string, incomeCurrency string, returnRate string, userLowerLimit string, userUpperLimit string, productUpperLimit string, productRemainAmount string, redeemPeriod int32, redeemType string, incomeReleaseType string, interestDate int64, newUserOnly int32, earlyRedeemSupported int32, duration int32, status string) *GetETHStakingProductsData {
	this := GetETHStakingProductsData{}
	this.Id = id
	this.Category = category
	this.Type = Type_
	this.Precision = precision
	this.Currency = currency
	this.IncomeCurrency = incomeCurrency
	this.ReturnRate = returnRate
	this.UserLowerLimit = userLowerLimit
	this.UserUpperLimit = userUpperLimit
	this.ProductUpperLimit = productUpperLimit
	this.ProductRemainAmount = productRemainAmount
	this.RedeemPeriod = redeemPeriod
	this.RedeemType = redeemType
	this.IncomeReleaseType = incomeReleaseType
	this.InterestDate = interestDate
	this.NewUserOnly = newUserOnly
	this.EarlyRedeemSupported = earlyRedeemSupported
	this.Duration = duration
	this.Status = status
	return &this
}

// NewGetETHStakingProductsDataWithDefaults instantiates a new GetETHStakingProductsData object
// This constructor will only assign default values to properties that have it defined,
func NewGetETHStakingProductsDataWithDefaults() *GetETHStakingProductsData {
	this := GetETHStakingProductsData{}
	return &this
}

func (o *GetETHStakingProductsData) ToMap() map[string]interface{} {
	toSerialize := map[string]interface{}{}
	toSerialize["id"] = o.Id
	toSerialize["category"] = o.Category
	toSerialize["type"] = o.Type
	toSerialize["precision"] = o.Precision
	toSerialize["currency"] = o.Currency
	toSerialize["incomeCurrency"] = o.IncomeCurrency
	toSerialize["returnRate"] = o.ReturnRate
	toSerialize["userLowerLimit"] = o.UserLowerLimit
	toSerialize["userUpperLimit"] = o.UserUpperLimit
	toSerialize["productUpperLimit"] = o.ProductUpperLimit
	toSerialize["productRemainAmount"] = o.ProductRemainAmount
	toSerialize["redeemPeriod"] = o.RedeemPeriod
	toSerialize["redeemType"] = o.RedeemType
	toSerialize["incomeReleaseType"] = o.IncomeReleaseType
	toSerialize["applyStartTime"] = o.ApplyStartTime
	toSerialize["applyEndTime"] = o.ApplyEndTime
	toSerialize["lockStartTime"] = o.LockStartTime
	toSerialize["lockEndTime"] = o.LockEndTime
	toSerialize["interestDate"] = o.InterestDate
	toSerialize["newUserOnly"] = o.NewUserOnly
	toSerialize["earlyRedeemSupported"] = o.EarlyRedeemSupported
	toSerialize["duration"] = o.Duration
	toSerialize["status"] = o.Status
	return toSerialize
}
