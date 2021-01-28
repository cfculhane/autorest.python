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
from azure.core.pipeline.transport import HttpRequest, HttpResponse
from azure.core.tracing.decorator import distributed_trace

from .. import models as _models

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from typing import Any, Callable, Dict, Generic, IO, List, Optional, TypeVar

    T = TypeVar("T")
    ClsType = Optional[Callable[[PipelineResponse[HttpRequest, HttpResponse], T, Dict[str, Any]], Any]]


class FormdataOperations(object):
    """FormdataOperations operations.

    You should not instantiate this class directly. Instead, you should create a Client instance that
    instantiates it for you and attaches it as an attribute.

    :ivar models: Alias to model classes used in this operation group.
    :type models: ~bodyformdata.models
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

    def _upload_file_request(
        self,
        body,  # type: IO
        **kwargs  # type: Any
    ):
        # type: (...) -> HttpRequest
        content_type = kwargs.pop("content_type", "multipart/form-data")
        accept = "application/octet-stream, application/json"

        # Construct URL
        url = self._upload_file_request.metadata["url"]  # type: ignore

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters["Content-Type"] = self._serialize.header("content_type", content_type, "str")
        header_parameters["Accept"] = self._serialize.header("accept", accept, "str")

        body_content_kwargs = {}  # type: Dict[str, Any]
        body_content_kwargs["form_content"] = body

        return self._client.post(url, query_parameters, header_parameters, **body_content_kwargs)

    _upload_file_request.metadata = {"url": "/formdata/stream/uploadfile"}  # type: ignore

    @distributed_trace
    def upload_file(
        self,
        file_content,  # type: IO
        file_name,  # type: str
        **kwargs  # type: Any
    ):
        # type: (...) -> IO
        """Upload file.

        :param file_content: File to upload.
        :type file_content: IO
        :param file_name: File name to upload. Name has to be spelled exactly as written here.
        :type file_name: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: IO, or the result of cls(response)
        :rtype: IO
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop("cls", None)  # type: ClsType[IO]
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}))

        # Construct form data
        _body = {
            "fileContent": file_content,
            "fileName": file_name,
        }
        request = self._upload_file_request(body=_body, **kwargs)
        kwargs.pop("content_type", None)

        pipeline_response = self._client._pipeline.run(request, stream=True, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.Error, response)
            raise HttpResponseError(response=response, model=error)

        deserialized = response.stream_download(self._client._pipeline)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    upload_file.metadata = {"url": "/formdata/stream/uploadfile"}  # type: ignore

    def _upload_file_via_body_request(
        self,
        body,  # type: IO
        **kwargs  # type: Any
    ):
        # type: (...) -> HttpRequest
        content_type = kwargs.pop("content_type", "application/octet-stream")
        accept = "application/octet-stream, application/json"

        # Construct URL
        url = self._upload_file_via_body_request.metadata["url"]  # type: ignore

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters["Content-Type"] = self._serialize.header("content_type", content_type, "str")
        header_parameters["Accept"] = self._serialize.header("accept", accept, "str")

        body_content_kwargs = {}  # type: Dict[str, Any]
        body_content_kwargs["stream_content"] = body

        return self._client.put(url, query_parameters, header_parameters, **body_content_kwargs)

    _upload_file_via_body_request.metadata = {"url": "/formdata/stream/uploadfile"}  # type: ignore

    @distributed_trace
    def upload_file_via_body(
        self,
        file_content,  # type: IO
        **kwargs  # type: Any
    ):
        # type: (...) -> IO
        """Upload file.

        :param file_content: File to upload.
        :type file_content: IO
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: IO, or the result of cls(response)
        :rtype: IO
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop("cls", None)  # type: ClsType[IO]
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}))

        _body = file_content
        request = self._upload_file_via_body_request(body=_body, **kwargs)
        kwargs.pop("content_type", None)

        pipeline_response = self._client._pipeline.run(request, stream=True, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.Error, response)
            raise HttpResponseError(response=response, model=error)

        deserialized = response.stream_download(self._client._pipeline)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    upload_file_via_body.metadata = {"url": "/formdata/stream/uploadfile"}  # type: ignore

    def _upload_files_request(
        self,
        body,  # type: List[IO]
        **kwargs  # type: Any
    ):
        # type: (...) -> HttpRequest
        content_type = kwargs.pop("content_type", "multipart/form-data")
        accept = "application/octet-stream, application/json"

        # Construct URL
        url = self._upload_files_request.metadata["url"]  # type: ignore

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters["Content-Type"] = self._serialize.header("content_type", content_type, "str")
        header_parameters["Accept"] = self._serialize.header("accept", accept, "str")

        body_content_kwargs = {}  # type: Dict[str, Any]
        body_content_kwargs["form_content"] = body

        return self._client.post(url, query_parameters, header_parameters, **body_content_kwargs)

    _upload_files_request.metadata = {"url": "/formdata/stream/uploadfiles"}  # type: ignore

    @distributed_trace
    def upload_files(
        self,
        file_content,  # type: List[IO]
        **kwargs  # type: Any
    ):
        # type: (...) -> IO
        """Upload multiple files.

        :param file_content: Files to upload.
        :type file_content: list[IO]
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: IO, or the result of cls(response)
        :rtype: IO
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop("cls", None)  # type: ClsType[IO]
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}))

        # Construct form data
        _body = {
            "fileContent": file_content,
        }
        request = self._upload_files_request(body=_body, **kwargs)
        kwargs.pop("content_type", None)

        pipeline_response = self._client._pipeline.run(request, stream=True, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.Error, response)
            raise HttpResponseError(response=response, model=error)

        deserialized = response.stream_download(self._client._pipeline)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    upload_files.metadata = {"url": "/formdata/stream/uploadfiles"}  # type: ignore
