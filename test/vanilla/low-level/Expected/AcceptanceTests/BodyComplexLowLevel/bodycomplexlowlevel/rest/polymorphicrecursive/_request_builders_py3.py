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
    """Get complex types that are polymorphic and have recursive references.

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
                "length": 0.0,  # Required.
                "siblings": [
                    ...
                ],
                "species": "str",  # Optional.
                fishtype: fishtype
            }
    """

    _headers = kwargs.pop("headers", {}) or {}  # type: Dict[str, Any]

    accept = _get_from_dict(_headers, "Accept") or "application/json"

    # Construct URL
    url = "/complex/polymorphicrecursive/valid"

    # Construct headers
    _headers["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="GET", url=url, headers=_headers, **kwargs)


def build_put_valid_request(*, json: JSONType = None, content: Any = None, **kwargs: Any) -> HttpRequest:
    """Put complex types that are polymorphic and have recursive references.

    See https://aka.ms/azsdk/python/protocol/quickstart for how to incorporate this request builder
    into your code flow.

    :keyword json: Pass in a JSON-serializable object (usually a dictionary). See the template in
     our example to find the input shape. Please put a salmon that looks like this:
     {
         "fishtype": "salmon",
         "species": "king",
         "length": 1,
         "age": 1,
         "location": "alaska",
         "iswild": true,
         "siblings": [
             {
                 "fishtype": "shark",
                 "species": "predator",
                 "length": 20,
                 "age": 6,
                 "siblings": [
                     {
                         "fishtype": "salmon",
                         "species": "coho",
                         "length": 2,
                         "age": 2,
                         "location": "atlantic",
                         "iswild": true,
                         "siblings": [
                             {
                                 "fishtype": "shark",
                                 "species": "predator",
                                 "length": 20,
                                 "age": 6
                             },
                             {
                                 "fishtype": "sawshark",
                                 "species": "dangerous",
                                 "length": 10,
                                 "age": 105
                             }
                         ]
                     },
                     {
                         "fishtype": "sawshark",
                         "species": "dangerous",
                         "length": 10,
                         "age": 105
                     }
                 ]
             },
             {
                 "fishtype": "sawshark",
                 "species": "dangerous",
                 "length": 10,
                 "age": 105
             }
         ]
     }.
    :paramtype json: JSONType
    :keyword content: Pass in binary content you want in the body of the request (typically bytes,
     a byte iterator, or stream input). Please put a salmon that looks like this:
     {
         "fishtype": "salmon",
         "species": "king",
         "length": 1,
         "age": 1,
         "location": "alaska",
         "iswild": true,
         "siblings": [
             {
                 "fishtype": "shark",
                 "species": "predator",
                 "length": 20,
                 "age": 6,
                 "siblings": [
                     {
                         "fishtype": "salmon",
                         "species": "coho",
                         "length": 2,
                         "age": 2,
                         "location": "atlantic",
                         "iswild": true,
                         "siblings": [
                             {
                                 "fishtype": "shark",
                                 "species": "predator",
                                 "length": 20,
                                 "age": 6
                             },
                             {
                                 "fishtype": "sawshark",
                                 "species": "dangerous",
                                 "length": 10,
                                 "age": 105
                             }
                         ]
                     },
                     {
                         "fishtype": "sawshark",
                         "species": "dangerous",
                         "length": 10,
                         "age": 105
                     }
                 ]
             },
             {
                 "fishtype": "sawshark",
                 "species": "dangerous",
                 "length": 10,
                 "age": 105
             }
         ]
     }.
    :paramtype content: any
    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's
     `send_request` method. See https://aka.ms/azsdk/python/protocol/quickstart for how to
     incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest

    Example:
        .. code-block:: python

            fishtype = 'Salmon' or 'Shark'

            # JSON input template you can fill out and use as your body input.
            json = {
                "length": 0.0,  # Required.
                "siblings": [
                    ...
                ],
                "species": "str",  # Optional.
                fishtype: fishtype
            }
    """

    _headers = kwargs.pop("headers", {}) or {}  # type: Dict[str, Any]

    content_type = kwargs.pop("content_type", _get_from_dict(_headers, "Content-Type") or None)  # type: Optional[str]
    accept = _get_from_dict(_headers, "Accept") or "application/json"

    # Construct URL
    url = "/complex/polymorphicrecursive/valid"

    # Construct headers
    if content_type is not None:
        _headers["Content-Type"] = _SERIALIZER.header("content_type", content_type, "str")
    _headers["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="PUT", url=url, headers=_headers, json=json, content=content, **kwargs)
