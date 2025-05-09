// Code generated by Kucoin Universal SDK Generator; DO NOT EDIT.

package marginprivate

// IsolatedMarginPositionChangeAssetsValue struct for IsolatedMarginPositionChangeAssetsValue
type IsolatedMarginPositionChangeAssetsValue struct {
	Total              string `json:"total,omitempty"`
	Hold               string `json:"hold,omitempty"`
	LiabilityPrincipal string `json:"liabilityPrincipal,omitempty"`
	LiabilityInterest  string `json:"liabilityInterest,omitempty"`
}

// NewIsolatedMarginPositionChangeAssetsValue instantiates a new IsolatedMarginPositionChangeAssetsValue object
// This constructor will assign default values to properties that have it defined
func NewIsolatedMarginPositionChangeAssetsValue(total string, hold string, liabilityPrincipal string, liabilityInterest string) *IsolatedMarginPositionChangeAssetsValue {
	this := IsolatedMarginPositionChangeAssetsValue{}
	this.Total = total
	this.Hold = hold
	this.LiabilityPrincipal = liabilityPrincipal
	this.LiabilityInterest = liabilityInterest
	return &this
}

// NewIsolatedMarginPositionChangeAssetsValueWithDefaults instantiates a new IsolatedMarginPositionChangeAssetsValue object
// This constructor will only assign default values to properties that have it defined,
func NewIsolatedMarginPositionChangeAssetsValueWithDefaults() *IsolatedMarginPositionChangeAssetsValue {
	this := IsolatedMarginPositionChangeAssetsValue{}
	return &this
}

func (o *IsolatedMarginPositionChangeAssetsValue) ToMap() map[string]interface{} {
	toSerialize := map[string]interface{}{}
	toSerialize["total"] = o.Total
	toSerialize["hold"] = o.Hold
	toSerialize["liabilityPrincipal"] = o.LiabilityPrincipal
	toSerialize["liabilityInterest"] = o.LiabilityInterest
	return toSerialize
}
