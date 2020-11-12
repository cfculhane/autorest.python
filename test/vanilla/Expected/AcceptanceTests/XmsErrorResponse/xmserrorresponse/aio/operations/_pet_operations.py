# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from typing import Any, Callable, Dict, Generic, Optional, TypeVar
import warnings

from azure.core.exceptions import ClientAuthenticationError, HttpResponseError, ResourceExistsError, ResourceNotFoundError, map_error
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import AsyncHttpResponse, HttpRequest
from azure.core.tracing.decorator_async import distributed_trace_async

from ... import models

T = TypeVar('T')
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, AsyncHttpResponse], T, Dict[str, Any]], Any]]

class PetOperations:
    """PetOperations async operations.

    You should not instantiate this class directly. Instead, you should create a Client instance that
    instantiates it for you and attaches it as an attribute.

    :ivar models: Alias to model classes used in this operation group.
    :type models: ~xmserrorresponse.models
    :param client: Client for service requests.
    :param config: Configuration of service client.
    :param serializer: An object model serializer.
    :param deserializer: An object model deserializer.
    """

    models = models

    def __init__(self, client, config, serializer, deserializer) -> None:
        self._client = client
        self._serialize = serializer
        self._deserialize = deserializer
        self._config = config

    @distributed_trace_async
    async def get_pet_by_id(
        self,
        pet_id: str,
        **kwargs
    ) -> Optional["models.Pet"]:
        """Gets pets by id.

        :param pet_id: pet id.
        :type pet_id: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: Pet, or the result of cls(response)
        :rtype: ~xmserrorresponse.models.Pet or None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType[Optional["models.Pet"]]
        error_map = {
            401: ClientAuthenticationError,
            409: ResourceExistsError,
            400: HttpResponseError,
            404: lambda response: ResourceNotFoundError(response=response, model=self._deserialize(models.NotFoundErrorBase, response)),
            501: HttpResponseError,
        }
        error_map.update(kwargs.pop('error_map', {}))
        accept = "application/json"

        # Construct URL
        url = self.get_pet_by_id.metadata['url']  # type: ignore
        path_format_arguments = {
            'petId': self._serialize.url("pet_id", pet_id, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Accept'] = self._serialize.header("accept", accept, 'str')

        request = self._client.get(url, query_parameters, header_parameters)
        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200, 202]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        deserialized = None
        if response.status_code == 200:
            deserialized = self._deserialize('Pet', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized
    get_pet_by_id.metadata = {'url': '/errorStatusCodes/Pets/{petId}/GetPet'}  # type: ignore

    @distributed_trace_async
    async def do_something(
        self,
        what_action: str,
        **kwargs
    ) -> "models.PetAction":
        """Asks pet to do something.

        :param what_action: what action the pet should do.
        :type what_action: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: PetAction, or the result of cls(response)
        :rtype: ~xmserrorresponse.models.PetAction
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["models.PetAction"]
        error_map = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            500: lambda response: HttpResponseError(response=response, model=self._deserialize(models.PetActionError, response)),
        }
        error_map.update(kwargs.pop('error_map', {}))
        accept = "application/json"

        # Construct URL
        url = self.do_something.metadata['url']  # type: ignore
        path_format_arguments = {
            'whatAction': self._serialize.url("what_action", what_action, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Accept'] = self._serialize.header("accept", accept, 'str')

        request = self._client.post(url, query_parameters, header_parameters)
        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize(models.PetActionError, response)
            raise HttpResponseError(response=response, model=error)

        deserialized = self._deserialize('PetAction', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized
    do_something.metadata = {'url': '/errorStatusCodes/Pets/doSomething/{whatAction}'}  # type: ignore

    @distributed_trace_async
    async def has_models_param(
        self,
        models: Optional[str] = "value1",
        **kwargs
    ) -> None:
        """Ensure you can correctly deserialize the returned PetActionError and deserialization doesn't
        conflict with the input param name 'models'.

        :param models: Make sure model deserialization doesn't conflict with this param name, which has
         input name 'models'. Use client default value in call.
        :type models: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None, or the result of cls(response)
        :rtype: None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType[None]
        error_map = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            500: lambda response: HttpResponseError(response=response, model=self._deserialize(models.PetActionError, response)),
        }
        error_map.update(kwargs.pop('error_map', {}))
        accept = "application/json"

        # Construct URL
        url = self.has_models_param.metadata['url']  # type: ignore

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]
        if models is not None:
            query_parameters['models'] = self._serialize.query("models", models, 'str')

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Accept'] = self._serialize.header("accept", accept, 'str')

        request = self._client.post(url, query_parameters, header_parameters)
        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize(models.PetActionError, response)
            raise HttpResponseError(response=response, model=error)

        if cls:
            return cls(pipeline_response, None, {})

    has_models_param.metadata = {'url': '/errorStatusCodes/Pets/hasModelsParam'}  # type: ignore
