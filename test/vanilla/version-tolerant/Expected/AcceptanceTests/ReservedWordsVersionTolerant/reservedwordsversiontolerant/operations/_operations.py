# pylint: disable=too-many-lines
# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from typing import Any, Callable, Dict, IO, List, Optional, TypeVar, cast

from msrest import Serializer

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
from azure.core.utils import case_insensitive_dict

from .._vendor import MixinABC, _format_url_section

T = TypeVar("T")
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, HttpResponse], T, Dict[str, Any]], Any]]

_SERIALIZER = Serializer()
_SERIALIZER.client_side_validation = False


def build_import_builders_operation_one_request(*, parameter1: str, **kwargs: Any) -> HttpRequest:
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
    _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

    accept = _headers.pop("Accept", "application/json")

    # Construct URL
    _url = "/reservedWords/operationGroup/import"

    # Construct parameters
    _params["parameter1"] = _SERIALIZER.query("parameter1", parameter1, "str")

    # Construct headers
    _headers["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="PUT", url=_url, params=_params, headers=_headers, **kwargs)


def build_operation_with_content_param_request(*, content: Any, **kwargs: Any) -> HttpRequest:
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})

    content_type = kwargs.pop("content_type", _headers.pop("Content-Type", None))  # type: Optional[str]
    accept = _headers.pop("Accept", "application/json")

    # Construct URL
    _url = "/reservedWords/operation/content"

    # Construct headers
    if content_type is not None:
        _headers["Content-Type"] = _SERIALIZER.header("content_type", content_type, "str")
    _headers["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="PUT", url=_url, headers=_headers, content=content, **kwargs)


def build_operation_with_json_param_request(*, json: Any = None, content: Any = None, **kwargs: Any) -> HttpRequest:
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})

    content_type = kwargs.pop("content_type", _headers.pop("Content-Type", None))  # type: Optional[str]
    accept = _headers.pop("Accept", "application/json")

    # Construct URL
    _url = "/reservedWords/operation/json"

    # Construct headers
    if content_type is not None:
        _headers["Content-Type"] = _SERIALIZER.header("content_type", content_type, "str")
    _headers["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="PUT", url=_url, headers=_headers, json=json, content=content, **kwargs)


def build_operation_with_data_param_request(
    *, data: Optional[Dict[str, Any]] = None, content: Any = None, **kwargs: Any
) -> HttpRequest:
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})

    content_type = kwargs.pop("content_type", _headers.pop("Content-Type", None))  # type: Optional[str]
    accept = _headers.pop("Accept", "application/json")

    # Construct URL
    _url = "/reservedWords/operation/data"

    # Construct headers
    if content_type is not None:
        _headers["Content-Type"] = _SERIALIZER.header("content_type", content_type, "str")
    _headers["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="PUT", url=_url, headers=_headers, data=data, content=content, **kwargs)


def build_operation_with_files_param_request(
    *, files: Optional[Dict[str, Any]] = None, content: Any = None, **kwargs: Any
) -> HttpRequest:
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})

    content_type = kwargs.pop("content_type", _headers.pop("Content-Type", None))  # type: Optional[str]
    accept = _headers.pop("Accept", "application/json")

    # Construct URL
    _url = "/reservedWords/operation/files"

    # Construct headers
    if content_type is not None:
        _headers["Content-Type"] = _SERIALIZER.header("content_type", content_type, "str")
    _headers["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="PUT", url=_url, headers=_headers, files=files, content=content, **kwargs)


def build_operation_with_url_request(
    url: str, *, header_parameters: str, query_parameters: Optional[List[str]] = None, **kwargs: Any
) -> HttpRequest:
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
    _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

    accept = _headers.pop("Accept", "application/json")

    # Construct URL
    _url = "/reservedWords/{url}"
    path_format_arguments = {
        "url": _SERIALIZER.url("url", url, "str"),
    }

    _url = _format_url_section(_url, **path_format_arguments)

    # Construct parameters
    if query_parameters is not None:
        _params["queryParameters"] = [
            _SERIALIZER.query("query_parameters", q, "str") if q is not None else "" for q in query_parameters
        ]

    # Construct headers
    _headers["headerParameters"] = _SERIALIZER.header("header_parameters", header_parameters, "str")
    _headers["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="GET", url=_url, params=_params, headers=_headers, **kwargs)


class ImportOperations:
    """
    .. warning::
        **DO NOT** instantiate this class directly.

        Instead, you should access the following operations through
        :class:`~reservedwordsversiontolerant.ReservedWordsClient`'s
        :attr:`import_operations` attribute.
    """

    def __init__(self, *args, **kwargs):
        input_args = list(args)
        self._client = input_args.pop(0) if input_args else kwargs.pop("client")
        self._config = input_args.pop(0) if input_args else kwargs.pop("config")
        self._serialize = input_args.pop(0) if input_args else kwargs.pop("serializer")
        self._deserialize = input_args.pop(0) if input_args else kwargs.pop("deserializer")

    @distributed_trace
    def operation_one(self, *, parameter1: str, **kwargs: Any) -> Any:
        """Operation in operation group import, a reserved word.

        :keyword parameter1: Pass in 'foo' to pass this test.
        :paramtype parameter1: str
        :return: any
        :rtype: any
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = kwargs.pop("headers", {}) or {}
        _params = kwargs.pop("params", {}) or {}

        cls = kwargs.pop("cls", None)  # type: ClsType[Any]

        request = build_import_builders_operation_one_request(
            parameter1=parameter1,
            headers=_headers,
            params=_params,
        )
        request.url = self._client.format_url(request.url)  # type: ignore

        pipeline_response = self._client._pipeline.run(  # type: ignore # pylint: disable=protected-access
            request, stream=False, **kwargs
        )
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if response.content:
            deserialized = response.json()
        else:
            deserialized = None

        if cls:
            return cls(pipeline_response, cast(Any, deserialized), {})

        return cast(Any, deserialized)


class ReservedWordsClientOperationsMixin(MixinABC):
    @distributed_trace
    def operation_with_content_param(self, content: IO, **kwargs: Any) -> Any:
        """Operation with body param called content. Pass in b'hello, world'.

        :param content: Pass in b'hello, world'.
        :type content: IO
        :return: any
        :rtype: any
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
        _params = kwargs.pop("params", {}) or {}

        content_type = kwargs.pop(
            "content_type", _headers.pop("Content-Type", "application/octet-stream")
        )  # type: Optional[str]
        cls = kwargs.pop("cls", None)  # type: ClsType[Any]

        _content = content

        request = build_operation_with_content_param_request(
            content_type=content_type,
            content=_content,
            headers=_headers,
            params=_params,
        )
        request.url = self._client.format_url(request.url)  # type: ignore

        pipeline_response = self._client._pipeline.run(  # type: ignore # pylint: disable=protected-access
            request, stream=False, **kwargs
        )
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if response.content:
            deserialized = response.json()
        else:
            deserialized = None

        if cls:
            return cls(pipeline_response, cast(Any, deserialized), {})

        return cast(Any, deserialized)

    @distributed_trace
    def operation_with_json_param(self, json: Any, **kwargs: Any) -> Any:
        """Operation with body param called 'json'. Pass in {'hello': 'world'}.

        :param json: Pass in {'hello': 'world'}.
        :type json: any
        :return: any
        :rtype: any
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
        _params = kwargs.pop("params", {}) or {}

        content_type = kwargs.pop(
            "content_type", _headers.pop("Content-Type", "application/json")
        )  # type: Optional[str]
        cls = kwargs.pop("cls", None)  # type: ClsType[Any]

        _json = json

        request = build_operation_with_json_param_request(
            content_type=content_type,
            json=_json,
            headers=_headers,
            params=_params,
        )
        request.url = self._client.format_url(request.url)  # type: ignore

        pipeline_response = self._client._pipeline.run(  # type: ignore # pylint: disable=protected-access
            request, stream=False, **kwargs
        )
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if response.content:
            deserialized = response.json()
        else:
            deserialized = None

        if cls:
            return cls(pipeline_response, cast(Any, deserialized), {})

        return cast(Any, deserialized)

    @distributed_trace
    def operation_with_data_param(self, data: Dict[str, Any], **kwargs: Any) -> Any:
        """Operation with urlencoded body param called 'data'.

        :param data: Form-encoded input for data. See the template in our example to find the input
         shape.
        :type data: dict[str, any]
        :return: any
        :rtype: any
        :raises: ~azure.core.exceptions.HttpResponseError

        Example:
            .. code-block:: python

                # form-encoded input template you can fill out and use as your `data` input.
                data = {
                    "data": "str",  # Pass in 'hello'.
                    "world": "str"  # Pass in 'world'.
                }
        """
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
        _params = kwargs.pop("params", {}) or {}

        content_type = kwargs.pop(
            "content_type", _headers.pop("Content-Type", "application/x-www-form-urlencoded")
        )  # type: Optional[str]
        cls = kwargs.pop("cls", None)  # type: ClsType[Any]

        request = build_operation_with_data_param_request(
            content_type=content_type,
            data=data,
            headers=_headers,
            params=_params,
        )
        request.url = self._client.format_url(request.url)  # type: ignore

        pipeline_response = self._client._pipeline.run(  # type: ignore # pylint: disable=protected-access
            request, stream=False, **kwargs
        )
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if response.content:
            deserialized = response.json()
        else:
            deserialized = None

        if cls:
            return cls(pipeline_response, cast(Any, deserialized), {})

        return cast(Any, deserialized)

    @distributed_trace
    def operation_with_files_param(self, files: Dict[str, Any], **kwargs: Any) -> Any:
        """Operation with multipart body param called 'files'.

        :param files: Multipart input for files. See the template in our example to find the input
         shape.
        :type files: dict[str, any]
        :return: any
        :rtype: any
        :raises: ~azure.core.exceptions.HttpResponseError

        Example:
            .. code-block:: python

                # multipart input template you can fill out and use as your `files` input.
                files = {
                    "file_name": "str",  # File name to upload. Pass in 'my.txt'.
                    "files": b'bytes'  # Files to upload. Pass in list of input streams.
                }
        """
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
        _params = kwargs.pop("params", {}) or {}

        content_type = kwargs.pop("content_type", _headers.pop("Content-Type", None))  # type: Optional[str]
        cls = kwargs.pop("cls", None)  # type: ClsType[Any]

        request = build_operation_with_files_param_request(
            content_type=content_type,
            files=files,
            headers=_headers,
            params=_params,
        )
        request.url = self._client.format_url(request.url)  # type: ignore

        pipeline_response = self._client._pipeline.run(  # type: ignore # pylint: disable=protected-access
            request, stream=False, **kwargs
        )
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if response.content:
            deserialized = response.json()
        else:
            deserialized = None

        if cls:
            return cls(pipeline_response, cast(Any, deserialized), {})

        return cast(Any, deserialized)

    @distributed_trace
    def operation_with_url(
        self, url: str, *, header_parameters: str, query_parameters: Optional[List[str]] = None, **kwargs: Any
    ) -> Any:
        """Operation with path format argument URL, header param headerParameters, and query param
        queryParameters.

        :param url: Pass in 'foo'.
        :type url: str
        :keyword header_parameters: Header arg that uses same name as headerParameters in generated
         code. Pass in 'x-ms-header' to pass.
        :paramtype header_parameters: str
        :keyword query_parameters: Query args that uses same name as queryParameters in generated code.
         Pass in ['one', 'two'] to pass test. Default value is None.
        :paramtype query_parameters: list[str]
        :return: any
        :rtype: any
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = kwargs.pop("headers", {}) or {}
        _params = kwargs.pop("params", {}) or {}

        cls = kwargs.pop("cls", None)  # type: ClsType[Any]

        request = build_operation_with_url_request(
            url=url,
            header_parameters=header_parameters,
            query_parameters=query_parameters,
            headers=_headers,
            params=_params,
        )
        request.url = self._client.format_url(request.url)  # type: ignore

        pipeline_response = self._client._pipeline.run(  # type: ignore # pylint: disable=protected-access
            request, stream=False, **kwargs
        )
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if response.content:
            deserialized = response.json()
        else:
            deserialized = None

        if cls:
            return cls(pipeline_response, cast(Any, deserialized), {})

        return cast(Any, deserialized)
