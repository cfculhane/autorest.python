# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from typing import Any, Optional

from azure.core import AsyncPipelineClient
from azure.core.pipeline.transport import AsyncHttpResponse, HttpRequest
from msrest import Deserializer, Serializer

from ._configuration import AutoRestHttpInfrastructureTestServiceConfiguration
from .operations import HttpFailureOperations
from .operations import HttpSuccessOperations
from .operations import HttpRedirectsOperations
from .operations import HttpClientFailureOperations
from .operations import HttpServerFailureOperations
from .operations import HttpRetryOperations
from .operations import MultipleResponsesOperations
from .. import models


class AutoRestHttpInfrastructureTestService(object):
    """Test Infrastructure for AutoRest.

    :ivar http_failure: HttpFailureOperations operations
    :vartype http_failure: httpinfrastructure.aio.operations.HttpFailureOperations
    :ivar http_success: HttpSuccessOperations operations
    :vartype http_success: httpinfrastructure.aio.operations.HttpSuccessOperations
    :ivar http_redirects: HttpRedirectsOperations operations
    :vartype http_redirects: httpinfrastructure.aio.operations.HttpRedirectsOperations
    :ivar http_client_failure: HttpClientFailureOperations operations
    :vartype http_client_failure: httpinfrastructure.aio.operations.HttpClientFailureOperations
    :ivar http_server_failure: HttpServerFailureOperations operations
    :vartype http_server_failure: httpinfrastructure.aio.operations.HttpServerFailureOperations
    :ivar http_retry: HttpRetryOperations operations
    :vartype http_retry: httpinfrastructure.aio.operations.HttpRetryOperations
    :ivar multiple_responses: MultipleResponsesOperations operations
    :vartype multiple_responses: httpinfrastructure.aio.operations.MultipleResponsesOperations
    :param str base_url: Service URL
    """

    def __init__(self, base_url: Optional[str] = None, **kwargs: Any) -> None:
        if not base_url:
            base_url = "http://localhost:3000"
        self._config = AutoRestHttpInfrastructureTestServiceConfiguration(**kwargs)
        self._client = AsyncPipelineClient(base_url=base_url, config=self._config, **kwargs)

        client_models = {k: v for k, v in models.__dict__.items() if isinstance(v, type)}
        self._serialize = Serializer(client_models)
        self._serialize.client_side_validation = False
        self._deserialize = Deserializer(client_models)

        self.http_failure = HttpFailureOperations(self._client, self._config, self._serialize, self._deserialize)
        self.http_success = HttpSuccessOperations(self._client, self._config, self._serialize, self._deserialize)
        self.http_redirects = HttpRedirectsOperations(self._client, self._config, self._serialize, self._deserialize)
        self.http_client_failure = HttpClientFailureOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.http_server_failure = HttpServerFailureOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.http_retry = HttpRetryOperations(self._client, self._config, self._serialize, self._deserialize)
        self.multiple_responses = MultipleResponsesOperations(
            self._client, self._config, self._serialize, self._deserialize
        )

    async def _send_request(self, http_request: HttpRequest, **kwargs: Any) -> AsyncHttpResponse:
        """Runs the network request through the client's chained policies.

        :param http_request: The network request you want to make. Required.
        :type http_request: ~azure.core.pipeline.transport.HttpRequest
        :keyword bool stream: Whether the response payload will be streamed. Defaults to True.
        :return: The response of your network call. Does not do error handling on your response.
        :rtype: ~azure.core.pipeline.transport.AsyncHttpResponse
        """
        http_request.url = self._client.format_url(http_request.url)
        stream = kwargs.pop("stream", True)
        pipeline_response = await self._client._pipeline.run(http_request, stream=stream, **kwargs)
        return pipeline_response.http_response

    async def close(self) -> None:
        await self._client.close()

    async def __aenter__(self) -> "AutoRestHttpInfrastructureTestService":
        await self._client.__aenter__()
        return self

    async def __aexit__(self, *exc_details) -> None:
        await self._client.__aexit__(*exc_details)
