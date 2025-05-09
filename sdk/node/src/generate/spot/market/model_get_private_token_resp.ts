// Code generated by Kucoin Universal SDK Generator; DO NOT EDIT.

import { Type, instanceToPlain, Exclude, plainToClassFromExist } from 'class-transformer';
import { GetPrivateTokenInstanceServers } from './model_get_private_token_instance_servers';
import { RestResponse } from '@model/common';
import { Response } from '@internal/interfaces/serializable';

export class GetPrivateTokenResp implements Response<RestResponse> {
    /**
     * The token required to establish a Websocket connection
     */
    token: string;

    /**
     *
     */
    @Type(() => GetPrivateTokenInstanceServers)
    instanceServers: Array<GetPrivateTokenInstanceServers>;

    /**
     * Private constructor, please use the corresponding static methods to construct the object.
     */
    private constructor() {
        // @ts-ignore
        this.token = null;
        // @ts-ignore
        this.instanceServers = null;
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
        return JSON.stringify(instanceToPlain(this));
    }
    /**
     * Create an object from a JSON string.
     */
    static fromJson(input: string): GetPrivateTokenResp {
        return this.fromObject(JSON.parse(input));
    }
    /**
     * Create an object from Js Object.
     */
    static fromObject(jsonObject: Object): GetPrivateTokenResp {
        return plainToClassFromExist(new GetPrivateTokenResp(), jsonObject);
    }
}
