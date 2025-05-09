// Code generated by Kucoin Universal SDK Generator; DO NOT EDIT.

import { GetTradeHistoryData } from './model_get_trade_history_data';
import { Type, instanceToPlain, Exclude, plainToClassFromExist } from 'class-transformer';
import { RestResponse } from '@model/common';
import { Response } from '@internal/interfaces/serializable';

export class GetTradeHistoryResp implements Response<RestResponse> {
    /**
     *
     */
    @Type(() => GetTradeHistoryData)
    data: Array<GetTradeHistoryData>;

    /**
     * Private constructor, please use the corresponding static methods to construct the object.
     */
    private constructor() {
        // @ts-ignore
        this.data = null;
    }
    /**
     * common response
     */
    @Exclude()
    commonResponse?: RestResponse;

    setCommonResponse(response: RestResponse): void {
        this.commonResponse = response;
    }

    /**
     * Convert the object to a JSON string.
     */
    toJson(): string {
        return JSON.stringify(instanceToPlain(this.data));
    }
    /**
     * Create an object from a JSON string.
     */
    static fromJson(input: string): GetTradeHistoryResp {
        return this.fromObject(JSON.parse(input));
    }
    /**
     * Create an object from Js Object.
     */
    static fromObject(jsonObject: Object): GetTradeHistoryResp {
        return plainToClassFromExist(new GetTradeHistoryResp(), { data: jsonObject });
    }
}
