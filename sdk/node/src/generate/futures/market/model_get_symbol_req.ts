// Code generated by Kucoin Universal SDK Generator; DO NOT EDIT.

import { instanceToPlain, plainToClassFromExist } from 'class-transformer';
import 'reflect-metadata';
import { Serializable } from '@internal/interfaces/serializable';

export class GetSymbolReq implements Serializable {
    /**
     * Path Parameter. Symbol of the contract
     */
    @Reflect.metadata('path', 'symbol')
    symbol?: string;

    /**
     * Private constructor, please use the corresponding static methods to construct the object.
     */
    private constructor() {}
    /**
     * Creates a new instance of the `GetSymbolReq` class.
     * The builder pattern allows step-by-step construction of a `GetSymbolReq` object.
     */
    static builder(): GetSymbolReqBuilder {
        return new GetSymbolReqBuilder(new GetSymbolReq());
    }

    /**
     * Creates a new instance of the `GetSymbolReq` class with the given data.
     */
    static create(data: {
        /**
         * Path Parameter. Symbol of the contract
         */
        symbol?: string;
    }): GetSymbolReq {
        let obj = new GetSymbolReq();
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
    static fromJson(input: string): GetSymbolReq {
        return this.fromObject(JSON.parse(input));
    }
    /**
     * Create an object from Js Object.
     */
    static fromObject(jsonObject: Object): GetSymbolReq {
        return plainToClassFromExist(new GetSymbolReq(), jsonObject);
    }
}

export class GetSymbolReqBuilder {
    constructor(readonly obj: GetSymbolReq) {
        this.obj = obj;
    }
    /**
     * Path Parameter. Symbol of the contract
     */
    setSymbol(value: string): GetSymbolReqBuilder {
        this.obj.symbol = value;
        return this;
    }

    /**
     * Get the final object.
     */
    build(): GetSymbolReq {
        return this.obj;
    }
}
