// Code generated by Kucoin Universal SDK Generator; DO NOT EDIT.

import { instanceToPlain, plainToClassFromExist } from 'class-transformer';
import 'reflect-metadata';
import { Serializable } from '@internal/interfaces/serializable';

export class GetOrderByOrderIdReq implements Serializable {
    /**
     * The unique order id generated by the trading system
     */
    @Reflect.metadata('path', 'orderId')
    orderId?: string;

    /**
     * symbol
     */
    symbol?: string;

    /**
     * Private constructor, please use the corresponding static methods to construct the object.
     */
    private constructor() {}
    /**
     * Creates a new instance of the `GetOrderByOrderIdReq` class.
     * The builder pattern allows step-by-step construction of a `GetOrderByOrderIdReq` object.
     */
    static builder(): GetOrderByOrderIdReqBuilder {
        return new GetOrderByOrderIdReqBuilder(new GetOrderByOrderIdReq());
    }

    /**
     * Creates a new instance of the `GetOrderByOrderIdReq` class with the given data.
     */
    static create(data: {
        /**
         * The unique order id generated by the trading system
         */
        orderId?: string;
        /**
         * symbol
         */
        symbol?: string;
    }): GetOrderByOrderIdReq {
        let obj = new GetOrderByOrderIdReq();
        obj.orderId = data.orderId;
        obj.symbol = data.symbol;
        return obj;
    }

    /**
     * Convert the object to a JSON string.
     */
    toJson(): string {
        return JSON.stringify(instanceToPlain(this));
    }
    /**
     * Create an object from a JSON string.
     */
    static fromJson(input: string): GetOrderByOrderIdReq {
        return this.fromObject(JSON.parse(input));
    }
    /**
     * Create an object from Js Object.
     */
    static fromObject(jsonObject: Object): GetOrderByOrderIdReq {
        return plainToClassFromExist(new GetOrderByOrderIdReq(), jsonObject);
    }
}

export class GetOrderByOrderIdReqBuilder {
    constructor(readonly obj: GetOrderByOrderIdReq) {
        this.obj = obj;
    }
    /**
     * The unique order id generated by the trading system
     */
    setOrderId(value: string): GetOrderByOrderIdReqBuilder {
        this.obj.orderId = value;
        return this;
    }

    /**
     * symbol
     */
    setSymbol(value: string): GetOrderByOrderIdReqBuilder {
        this.obj.symbol = value;
        return this;
    }

    /**
     * Get the final object.
     */
    build(): GetOrderByOrderIdReq {
        return this.obj;
    }
}
