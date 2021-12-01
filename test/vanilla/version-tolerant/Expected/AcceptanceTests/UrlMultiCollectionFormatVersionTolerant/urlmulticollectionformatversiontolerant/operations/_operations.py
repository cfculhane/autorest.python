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

from .._vendor import _get_from_dict

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from typing import Any, Callable, Dict, Generic, List, Optional, TypeVar

    T = TypeVar("T")
    ClsType = Optional[Callable[[PipelineResponse[HttpRequest, HttpResponse], T, Dict[str, Any]], Any]]

_SERIALIZER = Serializer()
_SERIALIZER.client_side_validation = False
# fmt: off

def build_queries_array_string_multi_null_request(
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    _headers = kwargs.pop("headers", {}) or {}  # type: Dict[str, Any]
    _params = kwargs.pop("params", {}) or {}  # type: Dict[str, Any]

    array_query = kwargs.pop('array_query', _get_from_dict(_params, 'arrayQuery') or None)  # type: Optional[List[str]]
    accept = _get_from_dict(_headers, 'Accept') or "application/json"

    # Construct URL
    url = '/queries/array/multi/string/null'

    # Construct parameters
    if array_query is not None:
        _params['arrayQuery'] = [_SERIALIZER.query("array_query", q, 'str') if q is not None else '' for q in array_query]

    # Construct headers
    _headers['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="GET",
        url=url,
        params=_params,
        headers=_headers,
        **kwargs
    )


def build_queries_array_string_multi_empty_request(
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    _headers = kwargs.pop("headers", {}) or {}  # type: Dict[str, Any]
    _params = kwargs.pop("params", {}) or {}  # type: Dict[str, Any]

    array_query = kwargs.pop('array_query', _get_from_dict(_params, 'arrayQuery') or None)  # type: Optional[List[str]]
    accept = _get_from_dict(_headers, 'Accept') or "application/json"

    # Construct URL
    url = '/queries/array/multi/string/empty'

    # Construct parameters
    if array_query is not None:
        _params['arrayQuery'] = [_SERIALIZER.query("array_query", q, 'str') if q is not None else '' for q in array_query]

    # Construct headers
    _headers['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="GET",
        url=url,
        params=_params,
        headers=_headers,
        **kwargs
    )


def build_queries_array_string_multi_valid_request(
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    _headers = kwargs.pop("headers", {}) or {}  # type: Dict[str, Any]
    _params = kwargs.pop("params", {}) or {}  # type: Dict[str, Any]

    array_query = kwargs.pop('array_query', _get_from_dict(_params, 'arrayQuery') or None)  # type: Optional[List[str]]
    accept = _get_from_dict(_headers, 'Accept') or "application/json"

    # Construct URL
    url = '/queries/array/multi/string/valid'

    # Construct parameters
    if array_query is not None:
        _params['arrayQuery'] = [_SERIALIZER.query("array_query", q, 'str') if q is not None else '' for q in array_query]

    # Construct headers
    _headers['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="GET",
        url=url,
        params=_params,
        headers=_headers,
        **kwargs
    )

# fmt: on
class QueriesOperations(object):
    """QueriesOperations operations.

    You should not instantiate this class directly. Instead, you should create a Client instance that
    instantiates it for you and attaches it as an attribute.

    :param client: Client for service requests.
    :param config: Configuration of service client.
    :param serializer: An object model serializer.
    :param deserializer: An object model deserializer.
    """

    def __init__(self, client, config, serializer, deserializer):
        self._client = client
        self._serialize = serializer
        self._deserialize = deserializer
        self._config = config

    @distributed_trace
    def array_string_multi_null(
        self, **kwargs  # type: Any
    ):
        # type: (...) -> None
        """Get a null array of string using the multi-array format.

        :keyword array_query: a null array of string using the multi-array format.
        :paramtype array_query: list[str]
        :return: None
        :rtype: None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop("cls", None)  # type: ClsType[None]
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = kwargs.pop("headers", {}) or {}  # type: Dict[str, Any]
        _params = kwargs.pop("params", {}) or {}  # type: Dict[str, Any]

        array_query = kwargs.pop(
            "array_query", _get_from_dict(_params, "arrayQuery") or None
        )  # type: Optional[List[str]]

        request = build_queries_array_string_multi_null_request(
            array_query=array_query,
            headers=_headers,
            params=_params,
        )
        request.url = self._client.format_url(request.url)

        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if cls:
            return cls(pipeline_response, None, {})

    array_string_multi_null.metadata = {"url": "/queries/array/multi/string/null"}  # type: ignore

    @distributed_trace
    def array_string_multi_empty(
        self, **kwargs  # type: Any
    ):
        # type: (...) -> None
        """Get an empty array [] of string using the multi-array format.

        :keyword array_query: an empty array [] of string using the multi-array format.
        :paramtype array_query: list[str]
        :return: None
        :rtype: None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop("cls", None)  # type: ClsType[None]
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = kwargs.pop("headers", {}) or {}  # type: Dict[str, Any]
        _params = kwargs.pop("params", {}) or {}  # type: Dict[str, Any]

        array_query = kwargs.pop(
            "array_query", _get_from_dict(_params, "arrayQuery") or None
        )  # type: Optional[List[str]]

        request = build_queries_array_string_multi_empty_request(
            array_query=array_query,
            headers=_headers,
            params=_params,
        )
        request.url = self._client.format_url(request.url)

        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if cls:
            return cls(pipeline_response, None, {})

    array_string_multi_empty.metadata = {"url": "/queries/array/multi/string/empty"}  # type: ignore

    @distributed_trace
    def array_string_multi_valid(
        self, **kwargs  # type: Any
    ):
        # type: (...) -> None
        """Get an array of string ['ArrayQuery1', 'begin!*'();:@ &=+$,/?#[]end' , null, ''] using the
        mult-array format.

        :keyword array_query: an array of string ['ArrayQuery1', 'begin!*'();:@ &=+$,/?#[]end' , null,
         ''] using the mult-array format.
        :paramtype array_query: list[str]
        :return: None
        :rtype: None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop("cls", None)  # type: ClsType[None]
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = kwargs.pop("headers", {}) or {}  # type: Dict[str, Any]
        _params = kwargs.pop("params", {}) or {}  # type: Dict[str, Any]

        array_query = kwargs.pop(
            "array_query", _get_from_dict(_params, "arrayQuery") or None
        )  # type: Optional[List[str]]

        request = build_queries_array_string_multi_valid_request(
            array_query=array_query,
            headers=_headers,
            params=_params,
        )
        request.url = self._client.format_url(request.url)

        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if cls:
            return cls(pipeline_response, None, {})

    array_string_multi_valid.metadata = {"url": "/queries/array/multi/string/valid"}  # type: ignore
