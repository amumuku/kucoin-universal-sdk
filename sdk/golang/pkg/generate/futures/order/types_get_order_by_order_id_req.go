// Code generated by Kucoin Universal SDK Generator; DO NOT EDIT.

package order

// GetOrderByOrderIdReq struct for GetOrderByOrderIdReq
type GetOrderByOrderIdReq struct {
	//
	OrderId *string `json:"order-id,omitempty" path:"order-id" url:"-"`
}

// NewGetOrderByOrderIdReq instantiates a new GetOrderByOrderIdReq object
// This constructor will assign default values to properties that have it defined
func NewGetOrderByOrderIdReq() *GetOrderByOrderIdReq {
	this := GetOrderByOrderIdReq{}
	return &this
}

// NewGetOrderByOrderIdReqWithDefaults instantiates a new GetOrderByOrderIdReq object
// This constructor will only assign default values to properties that have it defined,
func NewGetOrderByOrderIdReqWithDefaults() *GetOrderByOrderIdReq {
	this := GetOrderByOrderIdReq{}
	return &this
}

func (o *GetOrderByOrderIdReq) ToMap() map[string]interface{} {
	toSerialize := map[string]interface{}{}
	toSerialize["order-id"] = o.OrderId
	return toSerialize
}

type GetOrderByOrderIdReqBuilder struct {
	obj *GetOrderByOrderIdReq
}

func NewGetOrderByOrderIdReqBuilder() *GetOrderByOrderIdReqBuilder {
	return &GetOrderByOrderIdReqBuilder{obj: NewGetOrderByOrderIdReqWithDefaults()}
}

func (builder *GetOrderByOrderIdReqBuilder) SetOrderId(value string) *GetOrderByOrderIdReqBuilder {
	builder.obj.OrderId = &value
	return builder
}

func (builder *GetOrderByOrderIdReqBuilder) Build() *GetOrderByOrderIdReq {
	return builder.obj
}
