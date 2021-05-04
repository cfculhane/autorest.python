# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from copy import deepcopy
from typing import TYPE_CHECKING

from azure.core import PipelineClient
from azure.core.rest import HttpResponse, _StreamContextManager
from msrest import Deserializer, Serializer

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from typing import Any, Optional

    from azure.core.rest import HttpRequest

from ._configuration import AutoRestRequiredOptionalTestServiceConfiguration
from .operations import ImplicitOperations
from .operations import ExplicitOperations
from . import models


class AutoRestRequiredOptionalTestService(object):
    """Test Infrastructure for AutoRest.

    :ivar implicit: ImplicitOperations operations
    :vartype implicit: requiredoptional.operations.ImplicitOperations
    :ivar explicit: ExplicitOperations operations
    :vartype explicit: requiredoptional.operations.ExplicitOperations
    :param required_global_path: number of items to skip.
    :type required_global_path: str
    :param required_global_query: number of items to skip.
    :type required_global_query: str
    :param optional_global_query: number of items to skip.
    :type optional_global_query: int
    :param base_url: Service URL
    :type base_url: str
    """

    def __init__(
        self,
        required_global_path,  # type: str
        required_global_query,  # type: str
        optional_global_query=None,  # type: Optional[int]
        base_url=None,  # type: Optional[str]
        **kwargs  # type: Any
    ):
        # type: (...) -> None
        if not base_url:
            base_url = "http://localhost:3000"
        self._config = AutoRestRequiredOptionalTestServiceConfiguration(
            required_global_path, required_global_query, optional_global_query, **kwargs
        )
        self._client = PipelineClient(base_url=base_url, config=self._config, **kwargs)

        client_models = {k: v for k, v in models.__dict__.items() if isinstance(v, type)}
        self._serialize = Serializer(client_models)
        self._deserialize = Deserializer(client_models)
        self.implicit = ImplicitOperations(self._client, self._config, self._serialize, self._deserialize)
        self.explicit = ExplicitOperations(self._client, self._config, self._serialize, self._deserialize)

    def _send_request(self, http_request, **kwargs):
        # type: (HttpRequest, Any) -> HttpResponse
        """Runs the network request through the client's chained policies.

        We have helper methods to create requests specific to this service in `requiredoptional.rest`.
        Use these helper methods to create the request you pass to this method. See our example below:

        >>> from requiredoptional.rest import build_get_required_path_request
        >>> request = build_get_required_path_request(path_parameter)
        <HttpRequest [GET], url: '/reqopt/implicit/required/path/{pathParameter}'>
        >>> response = client.send_request(request)
        <HttpResponse: 200 OK>

        For more information on this code flow, see https://aka.ms/azsdk/python/llcwiki

        For advanced cases, you can also create your own :class:`~azure.core.rest.HttpRequest`
        and pass it in.

        :param http_request: The network request you want to make. Required.
        :type http_request: ~azure.core.rest.HttpRequest
        :keyword bool stream_response: Whether the response payload will be streamed. Defaults to False.
        :return: The response of your network call. Does not do error handling on your response.
        :rtype: ~azure.core.rest.HttpResponse
        """
        request_copy = deepcopy(http_request)
        request_copy.url = self._client.format_url(request_copy.url)
        if kwargs.pop("stream_response", False):
            return _StreamContextManager(
                client=self._client._pipeline,
                request=request_copy,
            )
        pipeline_response = self._client._pipeline.run(request_copy._internal_request, **kwargs)
        response = HttpResponse(
            status_code=pipeline_response.http_response.status_code,
            request=request_copy,
            _internal_response=pipeline_response.http_response,
        )
        response.read()
        return response

    def close(self):
        # type: () -> None
        self._client.close()

    def __enter__(self):
        # type: () -> AutoRestRequiredOptionalTestService
        self._client.__enter__()
        return self

    def __exit__(self, *exc_details):
        # type: (Any) -> None
        self._client.__exit__(*exc_details)
