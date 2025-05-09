// Code generated by Kucoin Universal SDK Generator; DO NOT EDIT.

import { instanceToPlain, plainToClassFromExist } from 'class-transformer';
import 'reflect-metadata';
import { Serializable } from '@internal/interfaces/serializable';

export class CancelOrderByOrderIdOldReq implements Serializable {
    /**
     * The unique order id generated by the trading system
     */
    @Reflect.metadata('path', 'orderId')
    orderId?: string;

    /**
     * Private constructor, please use the corresponding static methods to construct the object.
     */
    private constructor() {}
    /**
     * Creates a new instance of the `CancelOrderByOrderIdOldReq` class.
     * The builder pattern allows step-by-step construction of a `CancelOrderByOrderIdOldReq` object.
     */
    static builder(): CancelOrderByOrderIdOldReqBuilder {
        return new CancelOrderByOrderIdOldReqBuilder(new CancelOrderByOrderIdOldReq());
    }

    /**
     * Creates a new instance of the `CancelOrderByOrderIdOldReq` class with the given data.
     */
    static create(data: {
        /**
         * The unique order id generated by the trading system
         */
        orderId?: string;
    }): CancelOrderByOrderIdOldReq {
        let obj = new CancelOrderByOrderIdOldReq();
        obj.orderId = data.orderId;
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
    static fromJson(input: string): CancelOrderByOrderIdOldReq {
        return this.fromObject(JSON.parse(input));
    }
    /**
     * Create an object from Js Object.
     */
    static fromObject(jsonObject: Object): CancelOrderByOrderIdOldReq {
        return plainToClassFromExist(new CancelOrderByOrderIdOldReq(), jsonObject);
    }
}

export class CancelOrderByOrderIdOldReqBuilder {
    constructor(readonly obj: CancelOrderByOrderIdOldReq) {
        this.obj = obj;
    }
    /**
     * The unique order id generated by the trading system
     */
    setOrderId(value: string): CancelOrderByOrderIdOldReqBuilder {
        this.obj.orderId = value;
        return this;
    }

    /**
     * Get the final object.
     */
    build(): CancelOrderByOrderIdOldReq {
        return this.obj;
    }
}
