# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
import functools
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
from msrest import Serializer

from .. import models as _models
from .._vendor import _convert_request, _get_from_dict

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from typing import Any, Callable, Dict, Generic, Optional, TypeVar

    T = TypeVar("T")
    ClsType = Optional[Callable[[PipelineResponse[HttpRequest, HttpResponse], T, Dict[str, Any]], Any]]

_SERIALIZER = Serializer()
_SERIALIZER.client_side_validation = False
# fmt: off

def build_get_true_request(
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    _headers = kwargs.pop("headers", {}) or {}  # type: Dict[str, Any]

    accept = _get_from_dict(_headers, 'Accept') or "application/json"

    # Construct URL
    url = kwargs.pop("template_url", '/bool/true')

    # Construct headers
    _headers['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="GET",
        url=url,
        headers=_headers,
        **kwargs
    )


def build_put_true_request(
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    _headers = kwargs.pop("headers", {}) or {}  # type: Dict[str, Any]

    content_type = kwargs.pop('content_type', _get_from_dict(_headers, 'Content-Type') or None)  # type: Optional[str]
    json = kwargs.pop('json', True)  # type: bool
    accept = _get_from_dict(_headers, 'Accept') or "application/json"

    # Construct URL
    url = kwargs.pop("template_url", '/bool/true')

    # Construct headers
    if content_type is not None:
        _headers['Content-Type'] = _SERIALIZER.header("content_type", content_type, 'str')
    _headers['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="PUT",
        url=url,
        headers=_headers,
        json=json,
        **kwargs
    )


def build_get_false_request(
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    _headers = kwargs.pop("headers", {}) or {}  # type: Dict[str, Any]

    accept = _get_from_dict(_headers, 'Accept') or "application/json"

    # Construct URL
    url = kwargs.pop("template_url", '/bool/false')

    # Construct headers
    _headers['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="GET",
        url=url,
        headers=_headers,
        **kwargs
    )


def build_put_false_request(
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    _headers = kwargs.pop("headers", {}) or {}  # type: Dict[str, Any]

    content_type = kwargs.pop('content_type', _get_from_dict(_headers, 'Content-Type') or None)  # type: Optional[str]
    json = kwargs.pop('json', False)  # type: bool
    accept = _get_from_dict(_headers, 'Accept') or "application/json"

    # Construct URL
    url = kwargs.pop("template_url", '/bool/false')

    # Construct headers
    if content_type is not None:
        _headers['Content-Type'] = _SERIALIZER.header("content_type", content_type, 'str')
    _headers['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="PUT",
        url=url,
        headers=_headers,
        json=json,
        **kwargs
    )


def build_get_null_request(
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    _headers = kwargs.pop("headers", {}) or {}  # type: Dict[str, Any]

    accept = _get_from_dict(_headers, 'Accept') or "application/json"

    # Construct URL
    url = kwargs.pop("template_url", '/bool/null')

    # Construct headers
    _headers['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="GET",
        url=url,
        headers=_headers,
        **kwargs
    )


def build_get_invalid_request(
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    _headers = kwargs.pop("headers", {}) or {}  # type: Dict[str, Any]

    accept = _get_from_dict(_headers, 'Accept') or "application/json"

    # Construct URL
    url = kwargs.pop("template_url", '/bool/invalid')

    # Construct headers
    _headers['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="GET",
        url=url,
        headers=_headers,
        **kwargs
    )

# fmt: on
class BoolOperations(object):
    """BoolOperations operations.

    You should not instantiate this class directly. Instead, you should create a Client instance that
    instantiates it for you and attaches it as an attribute.

    :ivar models: Alias to model classes used in this operation group.
    :type models: ~bodyboolean.models
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
    def get_true(
        self, **kwargs  # type: Any
    ):
        # type: (...) -> bool
        """Get true Boolean value.

        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: bool, or the result of cls(response)
        :rtype: bool
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop("cls", None)  # type: ClsType[bool]
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = kwargs.pop("headers", {}) or {}  # type: Dict[str, Any]
        _params = kwargs.pop("params", {}) or {}  # type: Dict[str, Any]

        request = build_get_true_request(
            template_url=self.get_true.metadata["url"],
            headers=_headers,
            params=_params,
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)

        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.Error, pipeline_response)
            raise HttpResponseError(response=response, model=error)

        deserialized = self._deserialize("bool", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    get_true.metadata = {"url": "/bool/true"}  # type: ignore

    @distributed_trace
    def put_true(
        self, **kwargs  # type: Any
    ):
        # type: (...) -> None
        """Set Boolean value true.

        :keyword bool_body: The default value is True. Note that overriding this default value may
         result in unsupported behavior.
        :paramtype bool_body: bool
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None, or the result of cls(response)
        :rtype: None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop("cls", None)  # type: ClsType[None]
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = kwargs.pop("headers", {}) or {}  # type: Dict[str, Any]
        _params = kwargs.pop("params", {}) or {}  # type: Dict[str, Any]

        content_type = kwargs.pop(
            "content_type", _get_from_dict(_headers, "Content-Type") or "application/json"
        )  # type: Optional[str]
        bool_body = kwargs.pop("bool_body", True)  # type: bool

        request = build_put_true_request(
            content_type=content_type,
            json=bool_body,
            template_url=self.put_true.metadata["url"],
            headers=_headers,
            params=_params,
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)

        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.Error, pipeline_response)
            raise HttpResponseError(response=response, model=error)

        if cls:
            return cls(pipeline_response, None, {})

    put_true.metadata = {"url": "/bool/true"}  # type: ignore

    @distributed_trace
    def get_false(
        self, **kwargs  # type: Any
    ):
        # type: (...) -> bool
        """Get false Boolean value.

        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: bool, or the result of cls(response)
        :rtype: bool
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop("cls", None)  # type: ClsType[bool]
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = kwargs.pop("headers", {}) or {}  # type: Dict[str, Any]
        _params = kwargs.pop("params", {}) or {}  # type: Dict[str, Any]

        request = build_get_false_request(
            template_url=self.get_false.metadata["url"],
            headers=_headers,
            params=_params,
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)

        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.Error, pipeline_response)
            raise HttpResponseError(response=response, model=error)

        deserialized = self._deserialize("bool", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    get_false.metadata = {"url": "/bool/false"}  # type: ignore

    @distributed_trace
    def put_false(
        self, **kwargs  # type: Any
    ):
        # type: (...) -> None
        """Set Boolean value false.

        :keyword bool_body: The default value is False. Note that overriding this default value may
         result in unsupported behavior.
        :paramtype bool_body: bool
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None, or the result of cls(response)
        :rtype: None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop("cls", None)  # type: ClsType[None]
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = kwargs.pop("headers", {}) or {}  # type: Dict[str, Any]
        _params = kwargs.pop("params", {}) or {}  # type: Dict[str, Any]

        content_type = kwargs.pop(
            "content_type", _get_from_dict(_headers, "Content-Type") or "application/json"
        )  # type: Optional[str]
        bool_body = kwargs.pop("bool_body", False)  # type: bool

        request = build_put_false_request(
            content_type=content_type,
            json=bool_body,
            template_url=self.put_false.metadata["url"],
            headers=_headers,
            params=_params,
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)

        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.Error, pipeline_response)
            raise HttpResponseError(response=response, model=error)

        if cls:
            return cls(pipeline_response, None, {})

    put_false.metadata = {"url": "/bool/false"}  # type: ignore

    @distributed_trace
    def get_null(
        self, **kwargs  # type: Any
    ):
        # type: (...) -> Optional[bool]
        """Get null Boolean value.

        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: bool or None, or the result of cls(response)
        :rtype: bool or None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop("cls", None)  # type: ClsType[Optional[bool]]
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = kwargs.pop("headers", {}) or {}  # type: Dict[str, Any]
        _params = kwargs.pop("params", {}) or {}  # type: Dict[str, Any]

        request = build_get_null_request(
            template_url=self.get_null.metadata["url"],
            headers=_headers,
            params=_params,
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)

        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.Error, pipeline_response)
            raise HttpResponseError(response=response, model=error)

        deserialized = self._deserialize("bool", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    get_null.metadata = {"url": "/bool/null"}  # type: ignore

    @distributed_trace
    def get_invalid(
        self, **kwargs  # type: Any
    ):
        # type: (...) -> bool
        """Get invalid Boolean value.

        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: bool, or the result of cls(response)
        :rtype: bool
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop("cls", None)  # type: ClsType[bool]
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = kwargs.pop("headers", {}) or {}  # type: Dict[str, Any]
        _params = kwargs.pop("params", {}) or {}  # type: Dict[str, Any]

        request = build_get_invalid_request(
            template_url=self.get_invalid.metadata["url"],
            headers=_headers,
            params=_params,
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)

        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.Error, pipeline_response)
            raise HttpResponseError(response=response, model=error)

        deserialized = self._deserialize("bool", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    get_invalid.metadata = {"url": "/bool/invalid"}  # type: ignore
