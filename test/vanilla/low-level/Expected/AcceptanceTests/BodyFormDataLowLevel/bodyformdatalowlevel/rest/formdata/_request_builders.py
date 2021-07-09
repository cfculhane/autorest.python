# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from typing import TYPE_CHECKING

from azure.core.rest import HttpRequest
from msrest import Serializer

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from typing import Any, Dict, IO, List, Optional

_SERIALIZER = Serializer()


def build_upload_file_request(
    **kwargs,  # type: Any
):
    # type: (...) -> HttpRequest
    """Upload file.

    See https://aka.ms/azsdk/python/llcwiki for how to incorporate this request builder into your
    code flow.

    :keyword files: Multipart input for files. See the template in our example to find the input
     shape. File to upload.
    :paramtype files: dict[str, any]
    :keyword data: Pass in dictionary that contains form data to include in the body of the
     request. File to upload.
    :paramtype data: dict[str, any]
    :keyword content: Pass in binary content you want in the body of the request (typically bytes,
     a byte iterator, or stream input). File to upload.
    :paramtype content: any
    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's
     `send_request` method. See https://aka.ms/azsdk/python/protocol/quickstart for how to
     incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest

    Example:
        .. code-block:: python

            # multipart input template you can fill out and use as your `files` input.
            files = {}
    """

    content_type = kwargs.pop("content_type", None)  # type: Optional[str]

    accept = "application/octet-stream, application/json"
    # Construct URL
    url = kwargs.pop("template_url", "/formdata/stream/uploadfile")

    # Construct headers
    header_parameters = kwargs.pop("headers", {})  # type: Dict[str, Any]
    if content_type is not None:
        header_parameters["Content-Type"] = _SERIALIZER.header("content_type", content_type, "str")
    header_parameters["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="POST", url=url, headers=header_parameters, **kwargs)


def build_upload_file_via_body_request(
    **kwargs,  # type: Any
):
    # type: (...) -> HttpRequest
    """Upload file.

    See https://aka.ms/azsdk/python/llcwiki for how to incorporate this request builder into your
    code flow.

    :keyword content: Pass in binary content you want in the body of the request (typically bytes,
     a byte iterator, or stream input). File to upload.
    :paramtype content: any
    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's
     `send_request` method. See https://aka.ms/azsdk/python/protocol/quickstart for how to
     incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest
    """

    content_type = kwargs.pop("content_type", None)  # type: Optional[str]

    accept = "application/octet-stream, application/json"
    # Construct URL
    url = kwargs.pop("template_url", "/formdata/stream/uploadfile")

    # Construct headers
    header_parameters = kwargs.pop("headers", {})  # type: Dict[str, Any]
    if content_type is not None:
        header_parameters["Content-Type"] = _SERIALIZER.header("content_type", content_type, "str")
    header_parameters["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="PUT", url=url, headers=header_parameters, **kwargs)


def build_upload_files_request(
    **kwargs,  # type: Any
):
    # type: (...) -> HttpRequest
    """Upload multiple files.

    See https://aka.ms/azsdk/python/llcwiki for how to incorporate this request builder into your
    code flow.

    :keyword files: Multipart input for files. See the template in our example to find the input
     shape. Files to upload.
    :paramtype files: dict[str, any]
    :keyword data: Pass in dictionary that contains form data to include in the body of the
     request. Files to upload.
    :paramtype data: dict[str, any]
    :keyword content: Pass in binary content you want in the body of the request (typically bytes,
     a byte iterator, or stream input). Files to upload.
    :paramtype content: any
    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's
     `send_request` method. See https://aka.ms/azsdk/python/protocol/quickstart for how to
     incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest

    Example:
        .. code-block:: python

            # multipart input template you can fill out and use as your `files` input.
            files = {}
    """

    content_type = kwargs.pop("content_type", None)  # type: Optional[str]

    accept = "application/octet-stream, application/json"
    # Construct URL
    url = kwargs.pop("template_url", "/formdata/stream/uploadfiles")

    # Construct headers
    header_parameters = kwargs.pop("headers", {})  # type: Dict[str, Any]
    if content_type is not None:
        header_parameters["Content-Type"] = _SERIALIZER.header("content_type", content_type, "str")
    header_parameters["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="POST", url=url, headers=header_parameters, **kwargs)
