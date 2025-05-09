// Code generated by Kucoin Universal SDK Generator; DO NOT EDIT.

package subaccount

// AddSubAccountApiReq struct for AddSubAccountApiReq
type AddSubAccountApiReq struct {
	// Password (Must contain 7–32 characters. Cannot contain any spaces.)
	Passphrase string `json:"passphrase,omitempty"`
	// Remarks (1–24 characters)
	Remark string `json:"remark,omitempty"`
	// [Permissions](https://www.kucoin.com/docs-new/doc-338144)(Only General, Spot, Futures, Margin, InnerTransfer (Flex Transfer) permissions can be set, such as \"General, Trade\". The default is \"General\")
	Permission *string `json:"permission,omitempty"`
	// IP whitelist (You may add up to 20 IPs. Use a halfwidth comma to each IP)
	IpWhitelist *string `json:"ipWhitelist,omitempty"`
	// API expiration time: Never expire(default)-1, 30Day30, 90Day90, 180Day180, 360Day360
	Expire *string `json:"expire,omitempty"`
	// Sub-account name, create sub account name of API Key.
	SubName string `json:"subName,omitempty"`
}

// NewAddSubAccountApiReq instantiates a new AddSubAccountApiReq object
// This constructor will assign default values to properties that have it defined
func NewAddSubAccountApiReq(passphrase string, remark string, subName string) *AddSubAccountApiReq {
	this := AddSubAccountApiReq{}
	this.Passphrase = passphrase
	this.Remark = remark
	var permission string = "General"
	this.Permission = &permission
	var expire string = "-1"
	this.Expire = &expire
	this.SubName = subName
	return &this
}

// NewAddSubAccountApiReqWithDefaults instantiates a new AddSubAccountApiReq object
// This constructor will only assign default values to properties that have it defined,
func NewAddSubAccountApiReqWithDefaults() *AddSubAccountApiReq {
	this := AddSubAccountApiReq{}
	var permission string = "General"
	this.Permission = &permission
	var expire string = "-1"
	this.Expire = &expire
	return &this
}

func (o *AddSubAccountApiReq) ToMap() map[string]interface{} {
	toSerialize := map[string]interface{}{}
	toSerialize["passphrase"] = o.Passphrase
	toSerialize["remark"] = o.Remark
	toSerialize["permission"] = o.Permission
	toSerialize["ipWhitelist"] = o.IpWhitelist
	toSerialize["expire"] = o.Expire
	toSerialize["subName"] = o.SubName
	return toSerialize
}

type AddSubAccountApiReqBuilder struct {
	obj *AddSubAccountApiReq
}

func NewAddSubAccountApiReqBuilder() *AddSubAccountApiReqBuilder {
	return &AddSubAccountApiReqBuilder{obj: NewAddSubAccountApiReqWithDefaults()}
}

// Password (Must contain 7–32 characters. Cannot contain any spaces.)
func (builder *AddSubAccountApiReqBuilder) SetPassphrase(value string) *AddSubAccountApiReqBuilder {
	builder.obj.Passphrase = value
	return builder
}

// Remarks (1–24 characters)
func (builder *AddSubAccountApiReqBuilder) SetRemark(value string) *AddSubAccountApiReqBuilder {
	builder.obj.Remark = value
	return builder
}

// [Permissions](https://www.kucoin.com/docs-new/doc-338144)(Only General, Spot, Futures, Margin, InnerTransfer (Flex Transfer) permissions can be set, such as \"General, Trade\". The default is \"General\")
func (builder *AddSubAccountApiReqBuilder) SetPermission(value string) *AddSubAccountApiReqBuilder {
	builder.obj.Permission = &value
	return builder
}

// IP whitelist (You may add up to 20 IPs. Use a halfwidth comma to each IP)
func (builder *AddSubAccountApiReqBuilder) SetIpWhitelist(value string) *AddSubAccountApiReqBuilder {
	builder.obj.IpWhitelist = &value
	return builder
}

// API expiration time: Never expire(default)-1, 30Day30, 90Day90, 180Day180, 360Day360
func (builder *AddSubAccountApiReqBuilder) SetExpire(value string) *AddSubAccountApiReqBuilder {
	builder.obj.Expire = &value
	return builder
}

// Sub-account name, create sub account name of API Key.
func (builder *AddSubAccountApiReqBuilder) SetSubName(value string) *AddSubAccountApiReqBuilder {
	builder.obj.SubName = value
	return builder
}

func (builder *AddSubAccountApiReqBuilder) Build() *AddSubAccountApiReq {
	return builder.obj
}
