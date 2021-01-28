# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from typing import Any, Callable, Dict, Generic, Optional, TypeVar
import warnings

from azure.core.exceptions import (
    ClientAuthenticationError,
    HttpResponseError,
    ResourceExistsError,
    ResourceNotFoundError,
    map_error,
)
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import AsyncHttpResponse, HttpRequest
from azure.core.tracing.decorator_async import distributed_trace_async

from ... import models as _models

T = TypeVar("T")
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, AsyncHttpResponse], T, Dict[str, Any]], Any]]


class PolymorphismOperations:
    """PolymorphismOperations async operations.

    You should not instantiate this class directly. Instead, you should create a Client instance that
    instantiates it for you and attaches it as an attribute.

    :ivar models: Alias to model classes used in this operation group.
    :type models: ~bodycomplex.models
    :param client: Client for service requests.
    :param config: Configuration of service client.
    :param serializer: An object model serializer.
    :param deserializer: An object model deserializer.
    """

    models = _models

    def __init__(self, client, config, serializer, deserializer) -> None:
        self._client = client
        self._serialize = serializer
        self._deserialize = deserializer
        self._config = config

    def _get_valid_request(self, **kwargs: Any) -> HttpRequest:
        accept = "application/json"

        # Construct URL
        url = self._get_valid_request.metadata["url"]  # type: ignore

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters["Accept"] = self._serialize.header("accept", accept, "str")

        return self._client.get(url, query_parameters, header_parameters)

    _get_valid_request.metadata = {"url": "/complex/polymorphism/valid"}  # type: ignore

    @distributed_trace_async
    async def get_valid(self, **kwargs: Any) -> "_models.Fish":
        """Get complex types that are polymorphic.

        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: Fish, or the result of cls(response)
        :rtype: ~bodycomplex.models.Fish
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop("cls", None)  # type: ClsType["_models.Fish"]
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}))

        request = self._get_valid_request(**kwargs)

        kwargs.pop("content_type", None)

        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.Error, response)
            raise HttpResponseError(response=response, model=error)

        deserialized = self._deserialize("Fish", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    get_valid.metadata = {"url": "/complex/polymorphism/valid"}  # type: ignore

    def _put_valid_request(self, body: "_models.Fish", **kwargs: Any) -> HttpRequest:
        content_type = kwargs.pop("content_type", "application/json")
        accept = "application/json"

        # Construct URL
        url = self._put_valid_request.metadata["url"]  # type: ignore

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters["Content-Type"] = self._serialize.header("content_type", content_type, "str")
        header_parameters["Accept"] = self._serialize.header("accept", accept, "str")

        body_content_kwargs = {}  # type: Dict[str, Any]
        body_content = self._serialize.body(body, "Fish")
        body_content_kwargs["content"] = body_content
        return self._client.put(url, query_parameters, header_parameters, **body_content_kwargs)

    _put_valid_request.metadata = {"url": "/complex/polymorphism/valid"}  # type: ignore

    @distributed_trace_async
    async def put_valid(self, complex_body: "_models.Fish", **kwargs: Any) -> None:
        """Put complex types that are polymorphic.

        :param complex_body: Please put a salmon that looks like this:
         {
                 'fishtype':'Salmon',
                 'location':'alaska',
                 'iswild':true,
                 'species':'king',
                 'length':1.0,
                 'siblings':[
                   {
                     'fishtype':'Shark',
                     'age':6,
                     'birthday': '2012-01-05T01:00:00Z',
                     'length':20.0,
                     'species':'predator',
                   },
                   {
                     'fishtype':'Sawshark',
                     'age':105,
                     'birthday': '1900-01-05T01:00:00Z',
                     'length':10.0,
                     'picture': new Buffer([255, 255, 255, 255, 254]).toString('base64'),
                     'species':'dangerous',
                   },
                   {
                     'fishtype': 'goblin',
                     'age': 1,
                     'birthday': '2015-08-08T00:00:00Z',
                     'length': 30.0,
                     'species': 'scary',
                     'jawsize': 5
                   }
                 ]
               };.
        :type complex_body: ~bodycomplex.models.Fish
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None, or the result of cls(response)
        :rtype: None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop("cls", None)  # type: ClsType[None]
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}))

        _body = complex_body
        request = self._put_valid_request(body=_body, **kwargs)
        kwargs.pop("content_type", None)

        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.Error, response)
            raise HttpResponseError(response=response, model=error)

        if cls:
            return cls(pipeline_response, None, {})

    put_valid.metadata = {"url": "/complex/polymorphism/valid"}  # type: ignore

    def _get_dot_syntax_request(self, **kwargs: Any) -> HttpRequest:
        accept = "application/json"

        # Construct URL
        url = self._get_dot_syntax_request.metadata["url"]  # type: ignore

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters["Accept"] = self._serialize.header("accept", accept, "str")

        return self._client.get(url, query_parameters, header_parameters)

    _get_dot_syntax_request.metadata = {"url": "/complex/polymorphism/dotsyntax"}  # type: ignore

    @distributed_trace_async
    async def get_dot_syntax(self, **kwargs: Any) -> "_models.DotFish":
        """Get complex types that are polymorphic, JSON key contains a dot.

        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: DotFish, or the result of cls(response)
        :rtype: ~bodycomplex.models.DotFish
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop("cls", None)  # type: ClsType["_models.DotFish"]
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}))

        request = self._get_dot_syntax_request(**kwargs)

        kwargs.pop("content_type", None)

        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.Error, response)
            raise HttpResponseError(response=response, model=error)

        deserialized = self._deserialize("DotFish", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    get_dot_syntax.metadata = {"url": "/complex/polymorphism/dotsyntax"}  # type: ignore

    def _get_composed_with_discriminator_request(self, **kwargs: Any) -> HttpRequest:
        accept = "application/json"

        # Construct URL
        url = self._get_composed_with_discriminator_request.metadata["url"]  # type: ignore

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters["Accept"] = self._serialize.header("accept", accept, "str")

        return self._client.get(url, query_parameters, header_parameters)

    _get_composed_with_discriminator_request.metadata = {"url": "/complex/polymorphism/composedWithDiscriminator"}  # type: ignore

    @distributed_trace_async
    async def get_composed_with_discriminator(self, **kwargs: Any) -> "_models.DotFishMarket":
        """Get complex object composing a polymorphic scalar property and array property with polymorphic
        element type, with discriminator specified. Deserialization must NOT fail and use the
        discriminator type specified on the wire.

        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: DotFishMarket, or the result of cls(response)
        :rtype: ~bodycomplex.models.DotFishMarket
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop("cls", None)  # type: ClsType["_models.DotFishMarket"]
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}))

        request = self._get_composed_with_discriminator_request(**kwargs)

        kwargs.pop("content_type", None)

        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.Error, response)
            raise HttpResponseError(response=response, model=error)

        deserialized = self._deserialize("DotFishMarket", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    get_composed_with_discriminator.metadata = {"url": "/complex/polymorphism/composedWithDiscriminator"}  # type: ignore

    def _get_composed_without_discriminator_request(self, **kwargs: Any) -> HttpRequest:
        accept = "application/json"

        # Construct URL
        url = self._get_composed_without_discriminator_request.metadata["url"]  # type: ignore

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters["Accept"] = self._serialize.header("accept", accept, "str")

        return self._client.get(url, query_parameters, header_parameters)

    _get_composed_without_discriminator_request.metadata = {"url": "/complex/polymorphism/composedWithoutDiscriminator"}  # type: ignore

    @distributed_trace_async
    async def get_composed_without_discriminator(self, **kwargs: Any) -> "_models.DotFishMarket":
        """Get complex object composing a polymorphic scalar property and array property with polymorphic
        element type, without discriminator specified on wire. Deserialization must NOT fail and use
        the explicit type of the property.

        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: DotFishMarket, or the result of cls(response)
        :rtype: ~bodycomplex.models.DotFishMarket
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop("cls", None)  # type: ClsType["_models.DotFishMarket"]
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}))

        request = self._get_composed_without_discriminator_request(**kwargs)

        kwargs.pop("content_type", None)

        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.Error, response)
            raise HttpResponseError(response=response, model=error)

        deserialized = self._deserialize("DotFishMarket", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    get_composed_without_discriminator.metadata = {"url": "/complex/polymorphism/composedWithoutDiscriminator"}  # type: ignore

    def _get_complicated_request(self, **kwargs: Any) -> HttpRequest:
        accept = "application/json"

        # Construct URL
        url = self._get_complicated_request.metadata["url"]  # type: ignore

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters["Accept"] = self._serialize.header("accept", accept, "str")

        return self._client.get(url, query_parameters, header_parameters)

    _get_complicated_request.metadata = {"url": "/complex/polymorphism/complicated"}  # type: ignore

    @distributed_trace_async
    async def get_complicated(self, **kwargs: Any) -> "_models.Salmon":
        """Get complex types that are polymorphic, but not at the root of the hierarchy; also have
        additional properties.

        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: Salmon, or the result of cls(response)
        :rtype: ~bodycomplex.models.Salmon
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop("cls", None)  # type: ClsType["_models.Salmon"]
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}))

        request = self._get_complicated_request(**kwargs)

        kwargs.pop("content_type", None)

        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.Error, response)
            raise HttpResponseError(response=response, model=error)

        deserialized = self._deserialize("Salmon", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    get_complicated.metadata = {"url": "/complex/polymorphism/complicated"}  # type: ignore

    def _put_complicated_request(self, body: "_models.Salmon", **kwargs: Any) -> HttpRequest:
        content_type = kwargs.pop("content_type", "application/json")
        accept = "application/json"

        # Construct URL
        url = self._put_complicated_request.metadata["url"]  # type: ignore

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters["Content-Type"] = self._serialize.header("content_type", content_type, "str")
        header_parameters["Accept"] = self._serialize.header("accept", accept, "str")

        body_content_kwargs = {}  # type: Dict[str, Any]
        body_content = self._serialize.body(body, "Salmon")
        body_content_kwargs["content"] = body_content
        return self._client.put(url, query_parameters, header_parameters, **body_content_kwargs)

    _put_complicated_request.metadata = {"url": "/complex/polymorphism/complicated"}  # type: ignore

    @distributed_trace_async
    async def put_complicated(self, complex_body: "_models.Salmon", **kwargs: Any) -> None:
        """Put complex types that are polymorphic, but not at the root of the hierarchy; also have
        additional properties.

        :param complex_body:
        :type complex_body: ~bodycomplex.models.Salmon
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None, or the result of cls(response)
        :rtype: None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop("cls", None)  # type: ClsType[None]
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}))

        _body = complex_body
        request = self._put_complicated_request(body=_body, **kwargs)
        kwargs.pop("content_type", None)

        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.Error, response)
            raise HttpResponseError(response=response, model=error)

        if cls:
            return cls(pipeline_response, None, {})

    put_complicated.metadata = {"url": "/complex/polymorphism/complicated"}  # type: ignore

    def _put_missing_discriminator_request(self, body: "_models.Salmon", **kwargs: Any) -> HttpRequest:
        content_type = kwargs.pop("content_type", "application/json")
        accept = "application/json"

        # Construct URL
        url = self._put_missing_discriminator_request.metadata["url"]  # type: ignore

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters["Content-Type"] = self._serialize.header("content_type", content_type, "str")
        header_parameters["Accept"] = self._serialize.header("accept", accept, "str")

        body_content_kwargs = {}  # type: Dict[str, Any]
        body_content = self._serialize.body(body, "Salmon")
        body_content_kwargs["content"] = body_content
        return self._client.put(url, query_parameters, header_parameters, **body_content_kwargs)

    _put_missing_discriminator_request.metadata = {"url": "/complex/polymorphism/missingdiscriminator"}  # type: ignore

    @distributed_trace_async
    async def put_missing_discriminator(self, complex_body: "_models.Salmon", **kwargs: Any) -> "_models.Salmon":
        """Put complex types that are polymorphic, omitting the discriminator.

        :param complex_body:
        :type complex_body: ~bodycomplex.models.Salmon
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: Salmon, or the result of cls(response)
        :rtype: ~bodycomplex.models.Salmon
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop("cls", None)  # type: ClsType["_models.Salmon"]
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}))

        _body = complex_body
        request = self._put_missing_discriminator_request(body=_body, **kwargs)
        kwargs.pop("content_type", None)

        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.Error, response)
            raise HttpResponseError(response=response, model=error)

        deserialized = self._deserialize("Salmon", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    put_missing_discriminator.metadata = {"url": "/complex/polymorphism/missingdiscriminator"}  # type: ignore

    def _put_valid_missing_required_request(self, body: "_models.Fish", **kwargs: Any) -> HttpRequest:
        content_type = kwargs.pop("content_type", "application/json")
        accept = "application/json"

        # Construct URL
        url = self._put_valid_missing_required_request.metadata["url"]  # type: ignore

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters["Content-Type"] = self._serialize.header("content_type", content_type, "str")
        header_parameters["Accept"] = self._serialize.header("accept", accept, "str")

        body_content_kwargs = {}  # type: Dict[str, Any]
        body_content = self._serialize.body(body, "Fish")
        body_content_kwargs["content"] = body_content
        return self._client.put(url, query_parameters, header_parameters, **body_content_kwargs)

    _put_valid_missing_required_request.metadata = {"url": "/complex/polymorphism/missingrequired/invalid"}  # type: ignore

    @distributed_trace_async
    async def put_valid_missing_required(self, complex_body: "_models.Fish", **kwargs: Any) -> None:
        """Put complex types that are polymorphic, attempting to omit required 'birthday' field - the
        request should not be allowed from the client.

        :param complex_body: Please attempt put a sawshark that looks like this, the client should not
         allow this data to be sent:
         {
             "fishtype": "sawshark",
             "species": "snaggle toothed",
             "length": 18.5,
             "age": 2,
             "birthday": "2013-06-01T01:00:00Z",
             "location": "alaska",
             "picture": base64(FF FF FF FF FE),
             "siblings": [
                 {
                     "fishtype": "shark",
                     "species": "predator",
                     "birthday": "2012-01-05T01:00:00Z",
                     "length": 20,
                     "age": 6
                 },
                 {
                     "fishtype": "sawshark",
                     "species": "dangerous",
                     "picture": base64(FF FF FF FF FE),
                     "length": 10,
                     "age": 105
                 }
             ]
         }.
        :type complex_body: ~bodycomplex.models.Fish
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None, or the result of cls(response)
        :rtype: None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop("cls", None)  # type: ClsType[None]
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}))

        _body = complex_body
        request = self._put_valid_missing_required_request(body=_body, **kwargs)
        kwargs.pop("content_type", None)

        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.Error, response)
            raise HttpResponseError(response=response, model=error)

        if cls:
            return cls(pipeline_response, None, {})

    put_valid_missing_required.metadata = {"url": "/complex/polymorphism/missingrequired/invalid"}  # type: ignore
