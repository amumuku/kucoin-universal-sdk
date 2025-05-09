// Code generated by Kucoin Universal SDK Generator; DO NOT EDIT.

import { instanceToPlain, plainToClassFromExist } from 'class-transformer';
import { Serializable } from '@internal/interfaces/serializable';

export class GetSymbolsWithOpenOrderReq implements Serializable {
    /**
     * Cross Margin: MARGIN_TRADE, Isolated Margin: MARGIN_ISOLATED_TRADE
     */
    tradeType?: GetSymbolsWithOpenOrderReq.TradeTypeEnum;

    /**
     * Private constructor, please use the corresponding static methods to construct the object.
     */
    private constructor() {}
    /**
     * Creates a new instance of the `GetSymbolsWithOpenOrderReq` class.
     * The builder pattern allows step-by-step construction of a `GetSymbolsWithOpenOrderReq` object.
     */
    static builder(): GetSymbolsWithOpenOrderReqBuilder {
        return new GetSymbolsWithOpenOrderReqBuilder(new GetSymbolsWithOpenOrderReq());
    }

    /**
     * Creates a new instance of the `GetSymbolsWithOpenOrderReq` class with the given data.
     */
    static create(data: {
        /**
         * Cross Margin: MARGIN_TRADE, Isolated Margin: MARGIN_ISOLATED_TRADE
         */
        tradeType?: GetSymbolsWithOpenOrderReq.TradeTypeEnum;
    }): GetSymbolsWithOpenOrderReq {
        let obj = new GetSymbolsWithOpenOrderReq();
        obj.tradeType = data.tradeType;
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
    static fromJson(input: string): GetSymbolsWithOpenOrderReq {
        return this.fromObject(JSON.parse(input));
    }
    /**
     * Create an object from Js Object.
     */
    static fromObject(jsonObject: Object): GetSymbolsWithOpenOrderReq {
        return plainToClassFromExist(new GetSymbolsWithOpenOrderReq(), jsonObject);
    }
}

export namespace GetSymbolsWithOpenOrderReq {
    export enum TradeTypeEnum {
        /**
         *
         */
        MARGIN_TRADE = <any>'MARGIN_TRADE',
        /**
         *
         */
        MARGIN_ISOLATED_TRADE = <any>'MARGIN_ISOLATED_TRADE',
    }
}

export class GetSymbolsWithOpenOrderReqBuilder {
    constructor(readonly obj: GetSymbolsWithOpenOrderReq) {
        this.obj = obj;
    }
    /**
     * Cross Margin: MARGIN_TRADE, Isolated Margin: MARGIN_ISOLATED_TRADE
     */
    setTradeType(
        value: GetSymbolsWithOpenOrderReq.TradeTypeEnum,
    ): GetSymbolsWithOpenOrderReqBuilder {
        this.obj.tradeType = value;
        return this;
    }

    /**
     * Get the final object.
     */
    build(): GetSymbolsWithOpenOrderReq {
        return this.obj;
    }
}
