# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from typing import TYPE_CHECKING
import warnings

from azure.core.exceptions import (
    ClientAuthenticationError,
    HttpResponseError,
    ResourceExistsError,
    ResourceNotFoundError,
    map_error,
)
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import HttpResponse
from azure.core.rest import HttpRequest
from azure.core.tracing.decorator import distributed_trace
from azure.mgmt.core.exceptions import ARMErrorFormat

from .. import models as _models
from .._rest import subscription_in_method as rest_subscription_in_method

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from typing import Any, Callable, Dict, Generic, Optional, TypeVar

    T = TypeVar("T")
    ClsType = Optional[Callable[[PipelineResponse[HttpRequest, HttpResponse], T, Dict[str, Any]], Any]]


class SubscriptionInMethodOperations(object):
    """SubscriptionInMethodOperations operations.

    You should not instantiate this class directly. Instead, you should create a Client instance that
    instantiates it for you and attaches it as an attribute.

    :ivar models: Alias to model classes used in this operation group.
    :type models: ~azurespecialproperties.models
    :param client: Client for service requests.
    :param config: Configuration of service client.
    :param serializer: An object model serializer.
    :param deserializer: An object model deserializer.
    """

    models = _models

    def __init__(self, client, config, serializer, deserializer):
        self._client = client
        self._serialize = serializer
        self._deserialize = deserializer
        self._config = config

    @distributed_trace
    def post_method_local_valid(
        self,
        subscription_id,  # type: str
        **kwargs  # type: Any
    ):
        # type: (...) -> None
        """POST method with subscriptionId modeled in the method.  pass in subscription id =
        '1234-5678-9012-3456' to succeed.

        :param subscription_id: This should appear as a method parameter, use value
         '1234-5678-9012-3456'.
        :type subscription_id: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None, or the result of cls(response)
        :rtype: None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop("cls", None)  # type: ClsType[None]
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}))

        request = rest_subscription_in_method.build_post_method_local_valid_request(
            subscription_id=subscription_id, template_url=self.post_method_local_valid.metadata["url"], **kwargs
        )._internal_request
        request.url = self._client.format_url(request.url)
        kwargs.pop("content_type", None)

        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.Error, response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        if cls:
            return cls(pipeline_response, None, {})

    post_method_local_valid.metadata = {"url": "/azurespecials/subscriptionId/method/string/none/path/local/1234-5678-9012-3456/{subscriptionId}"}  # type: ignore

    @distributed_trace
    def post_method_local_null(
        self,
        subscription_id,  # type: str
        **kwargs  # type: Any
    ):
        # type: (...) -> None
        """POST method with subscriptionId modeled in the method.  pass in subscription id = null,
        client-side validation should prevent you from making this call.

        :param subscription_id: This should appear as a method parameter, use value null, client-side
         validation should prvenet the call.
        :type subscription_id: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None, or the result of cls(response)
        :rtype: None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop("cls", None)  # type: ClsType[None]
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}))

        request = rest_subscription_in_method.build_post_method_local_null_request(
            subscription_id=subscription_id, template_url=self.post_method_local_null.metadata["url"], **kwargs
        )._internal_request
        request.url = self._client.format_url(request.url)
        kwargs.pop("content_type", None)

        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.Error, response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        if cls:
            return cls(pipeline_response, None, {})

    post_method_local_null.metadata = {"url": "/azurespecials/subscriptionId/method/string/none/path/local/null/{subscriptionId}"}  # type: ignore

    @distributed_trace
    def post_path_local_valid(
        self,
        subscription_id,  # type: str
        **kwargs  # type: Any
    ):
        # type: (...) -> None
        """POST method with subscriptionId modeled in the method.  pass in subscription id =
        '1234-5678-9012-3456' to succeed.

        :param subscription_id: Should appear as a method parameter -use value '1234-5678-9012-3456'.
        :type subscription_id: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None, or the result of cls(response)
        :rtype: None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop("cls", None)  # type: ClsType[None]
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}))

        request = rest_subscription_in_method.build_post_path_local_valid_request(
            subscription_id=subscription_id, template_url=self.post_path_local_valid.metadata["url"], **kwargs
        )._internal_request
        request.url = self._client.format_url(request.url)
        kwargs.pop("content_type", None)

        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.Error, response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        if cls:
            return cls(pipeline_response, None, {})

    post_path_local_valid.metadata = {"url": "/azurespecials/subscriptionId/path/string/none/path/local/1234-5678-9012-3456/{subscriptionId}"}  # type: ignore

    @distributed_trace
    def post_swagger_local_valid(
        self,
        subscription_id,  # type: str
        **kwargs  # type: Any
    ):
        # type: (...) -> None
        """POST method with subscriptionId modeled in the method.  pass in subscription id =
        '1234-5678-9012-3456' to succeed.

        :param subscription_id: The subscriptionId, which appears in the path, the value is always
         '1234-5678-9012-3456'.
        :type subscription_id: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None, or the result of cls(response)
        :rtype: None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop("cls", None)  # type: ClsType[None]
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}))

        request = rest_subscription_in_method.build_post_swagger_local_valid_request(
            subscription_id=subscription_id, template_url=self.post_swagger_local_valid.metadata["url"], **kwargs
        )._internal_request
        request.url = self._client.format_url(request.url)
        kwargs.pop("content_type", None)

        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.Error, response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        if cls:
            return cls(pipeline_response, None, {})

    post_swagger_local_valid.metadata = {"url": "/azurespecials/subscriptionId/swagger/string/none/path/local/1234-5678-9012-3456/{subscriptionId}"}  # type: ignore
