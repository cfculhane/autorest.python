# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from typing import Any, Dict, Optional, TypeVar

from azure.core.rest import HttpRequest
from msrest import Serializer

from ..._vendor import _get_from_dict

T = TypeVar("T")
JSONType = Any

_SERIALIZER = Serializer()


def build_get_valid_request(**kwargs: Any) -> HttpRequest:
    """Get complex type {id: 2, name: 'abc', color: 'YELLOW'}.

    See https://aka.ms/azsdk/python/protocol/quickstart for how to incorporate this request builder
    into your code flow.

    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's
     `send_request` method. See https://aka.ms/azsdk/python/protocol/quickstart for how to
     incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest

    Example:
        .. code-block:: python

            # response body for status code(s): 200
            response.json() == {
                "color": "str",  # Optional. Possible values include: "cyan", "Magenta", "YELLOW", "blacK".
                "id": 0,  # Optional. Basic Id.
                "name": "str"  # Optional. Name property with a very long description that does not fit on a single line and a line break.
            }
    """

    _headers = kwargs.pop("headers", {}) or {}  # type: Dict[str, Any]

    accept = _get_from_dict(_headers, "Accept") or "application/json"

    # Construct URL
    url = "/complex/basic/valid"

    # Construct headers
    _headers["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="GET", url=url, headers=_headers, **kwargs)


def build_put_valid_request(*, json: JSONType = None, content: Any = None, **kwargs: Any) -> HttpRequest:
    """Please put {id: 2, name: 'abc', color: 'Magenta'}.

    See https://aka.ms/azsdk/python/protocol/quickstart for how to incorporate this request builder
    into your code flow.

    :keyword api_version: Api Version. The default value is "2016-02-29". Note that overriding this
     default value may result in unsupported behavior.
    :paramtype api_version: str
    :keyword json: Pass in a JSON-serializable object (usually a dictionary). See the template in
     our example to find the input shape. Please put {id: 2, name: 'abc', color: 'Magenta'}.
    :paramtype json: JSONType
    :keyword content: Pass in binary content you want in the body of the request (typically bytes,
     a byte iterator, or stream input). Please put {id: 2, name: 'abc', color: 'Magenta'}.
    :paramtype content: any
    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's
     `send_request` method. See https://aka.ms/azsdk/python/protocol/quickstart for how to
     incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest

    Example:
        .. code-block:: python

            # JSON input template you can fill out and use as your body input.
            json = {
                "color": "str",  # Optional. Possible values include: "cyan", "Magenta", "YELLOW", "blacK".
                "id": 0,  # Optional. Basic Id.
                "name": "str"  # Optional. Name property with a very long description that does not fit on a single line and a line break.
            }
    """

    _headers = kwargs.pop("headers", {}) or {}  # type: Dict[str, Any]
    _params = kwargs.pop("params", {}) or {}  # type: Dict[str, Any]

    api_version = kwargs.pop("api_version", _get_from_dict(_params, "api-version") or "2016-02-29")  # type: str
    content_type = kwargs.pop("content_type", _get_from_dict(_headers, "Content-Type") or None)  # type: Optional[str]
    accept = _get_from_dict(_headers, "Accept") or "application/json"

    # Construct URL
    url = "/complex/basic/valid"

    # Construct parameters
    _params["api-version"] = _SERIALIZER.query("api_version", api_version, "str")

    # Construct headers
    if content_type is not None:
        _headers["Content-Type"] = _SERIALIZER.header("content_type", content_type, "str")
    _headers["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="PUT", url=url, params=_params, headers=_headers, json=json, content=content, **kwargs)


def build_get_invalid_request(**kwargs: Any) -> HttpRequest:
    """Get a basic complex type that is invalid for the local strong type.

    See https://aka.ms/azsdk/python/protocol/quickstart for how to incorporate this request builder
    into your code flow.

    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's
     `send_request` method. See https://aka.ms/azsdk/python/protocol/quickstart for how to
     incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest

    Example:
        .. code-block:: python

            # response body for status code(s): 200
            response.json() == {
                "color": "str",  # Optional. Possible values include: "cyan", "Magenta", "YELLOW", "blacK".
                "id": 0,  # Optional. Basic Id.
                "name": "str"  # Optional. Name property with a very long description that does not fit on a single line and a line break.
            }
    """

    _headers = kwargs.pop("headers", {}) or {}  # type: Dict[str, Any]

    accept = _get_from_dict(_headers, "Accept") or "application/json"

    # Construct URL
    url = "/complex/basic/invalid"

    # Construct headers
    _headers["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="GET", url=url, headers=_headers, **kwargs)


def build_get_empty_request(**kwargs: Any) -> HttpRequest:
    """Get a basic complex type that is empty.

    See https://aka.ms/azsdk/python/protocol/quickstart for how to incorporate this request builder
    into your code flow.

    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's
     `send_request` method. See https://aka.ms/azsdk/python/protocol/quickstart for how to
     incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest

    Example:
        .. code-block:: python

            # response body for status code(s): 200
            response.json() == {
                "color": "str",  # Optional. Possible values include: "cyan", "Magenta", "YELLOW", "blacK".
                "id": 0,  # Optional. Basic Id.
                "name": "str"  # Optional. Name property with a very long description that does not fit on a single line and a line break.
            }
    """

    _headers = kwargs.pop("headers", {}) or {}  # type: Dict[str, Any]

    accept = _get_from_dict(_headers, "Accept") or "application/json"

    # Construct URL
    url = "/complex/basic/empty"

    # Construct headers
    _headers["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="GET", url=url, headers=_headers, **kwargs)


def build_get_null_request(**kwargs: Any) -> HttpRequest:
    """Get a basic complex type whose properties are null.

    See https://aka.ms/azsdk/python/protocol/quickstart for how to incorporate this request builder
    into your code flow.

    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's
     `send_request` method. See https://aka.ms/azsdk/python/protocol/quickstart for how to
     incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest

    Example:
        .. code-block:: python

            # response body for status code(s): 200
            response.json() == {
                "color": "str",  # Optional. Possible values include: "cyan", "Magenta", "YELLOW", "blacK".
                "id": 0,  # Optional. Basic Id.
                "name": "str"  # Optional. Name property with a very long description that does not fit on a single line and a line break.
            }
    """

    _headers = kwargs.pop("headers", {}) or {}  # type: Dict[str, Any]

    accept = _get_from_dict(_headers, "Accept") or "application/json"

    # Construct URL
    url = "/complex/basic/null"

    # Construct headers
    _headers["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="GET", url=url, headers=_headers, **kwargs)


def build_get_not_provided_request(**kwargs: Any) -> HttpRequest:
    """Get a basic complex type while the server doesn't provide a response payload.

    See https://aka.ms/azsdk/python/protocol/quickstart for how to incorporate this request builder
    into your code flow.

    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's
     `send_request` method. See https://aka.ms/azsdk/python/protocol/quickstart for how to
     incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest

    Example:
        .. code-block:: python

            # response body for status code(s): 200
            response.json() == {
                "color": "str",  # Optional. Possible values include: "cyan", "Magenta", "YELLOW", "blacK".
                "id": 0,  # Optional. Basic Id.
                "name": "str"  # Optional. Name property with a very long description that does not fit on a single line and a line break.
            }
    """

    _headers = kwargs.pop("headers", {}) or {}  # type: Dict[str, Any]

    accept = _get_from_dict(_headers, "Accept") or "application/json"

    # Construct URL
    url = "/complex/basic/notprovided"

    # Construct headers
    _headers["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="GET", url=url, headers=_headers, **kwargs)
