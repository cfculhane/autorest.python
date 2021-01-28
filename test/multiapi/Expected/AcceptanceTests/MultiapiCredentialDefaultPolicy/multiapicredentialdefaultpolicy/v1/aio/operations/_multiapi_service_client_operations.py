# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from typing import Any, AsyncIterable, Callable, Dict, Generic, Optional, TypeVar, Union
import warnings

from azure.core.async_paging import AsyncItemPaged, AsyncList
from azure.core.exceptions import ClientAuthenticationError, HttpResponseError, ResourceExistsError, ResourceNotFoundError, map_error
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import AsyncHttpResponse, HttpRequest
from azure.core.polling import AsyncLROPoller, AsyncNoPolling, AsyncPollingMethod
from azure.mgmt.core.exceptions import ARMErrorFormat
from azure.mgmt.core.polling.async_arm_polling import AsyncARMPolling

from ... import models as _models

T = TypeVar('T')
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, AsyncHttpResponse], T, Dict[str, Any]], Any]]

class MultiapiServiceClientOperationsMixin:

    def _test_one_request(
        self,
        id: int,
        message: Optional[str] = None,
        **kwargs: Any
    ) -> HttpRequest:
        api_version = "1.0.0"
        accept = "application/json"

        # Construct URL
        url = self._test_one_request.metadata['url']  # type: ignore

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]
        query_parameters['id'] = self._serialize.query("id", id, 'int')
        if message is not None:
            query_parameters['message'] = self._serialize.query("message", message, 'str')
        query_parameters['api-version'] = self._serialize.query("api_version", api_version, 'str')

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Accept'] = self._serialize.header("accept", accept, 'str')

        return self._client.put(url, query_parameters, header_parameters)
    _test_one_request.metadata = {'url': '/multiapi/testOneEndpoint'}  # type: ignore

    async def test_one(
        self,
        id: int,
        message: Optional[str] = None,
        **kwargs: Any
    ) -> None:
        """TestOne should be in an FirstVersionOperationsMixin.

        :param id: An int parameter.
        :type id: int
        :param message: An optional string parameter.
        :type message: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None, or the result of cls(response)
        :rtype: None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType[None]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))

        request = self._test_one_request(
            id=id,
            message=message,
            **kwargs
        )
        kwargs.pop('content_type', None)

        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.Error, response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        if cls:
            return cls(pipeline_response, None, {})

    test_one.metadata = {'url': '/multiapi/testOneEndpoint'}  # type: ignore


    def _test_lro_request(
        self,
        body: Optional["_models.Product"] = None,
        **kwargs: Any
    ) -> HttpRequest:
        content_type = kwargs.pop("content_type", "application/json")
        accept = "application/json"

        # Construct URL
        url = self._test_lro_request.metadata['url']  # type: ignore

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Content-Type'] = self._serialize.header("content_type", content_type, 'str')
        header_parameters['Accept'] = self._serialize.header("accept", accept, 'str')

        body_content_kwargs = {}  # type: Dict[str, Any]
        if body is not None:
            body_content = self._serialize.body(body, 'Product')
        else:
            body_content = None
        body_content_kwargs['content'] = body_content
        return self._client.put(url, query_parameters, header_parameters, **body_content_kwargs)
    _test_lro_request.metadata = {'url': '/multiapi/lro'}  # type: ignore

    async def begin_test_lro(
        self,
        product: Optional["_models.Product"] = None,
        **kwargs: Any
    ) -> AsyncLROPoller["_models.Product"]:
        """Put in whatever shape of Product you want, will return a Product with id equal to 100.

        :param product: Product to put.
        :type product: ~multiapicredentialdefaultpolicy.v1.models.Product
        :keyword callable cls: A custom type or function that will be passed the direct response
        :keyword str continuation_token: A continuation token to restart a poller from a saved state.
        :keyword polling: Pass in True if you'd like the AsyncARMPolling polling method,
         False for no polling, or your own initialized polling object for a personal polling strategy.
        :paramtype polling: bool or ~azure.core.polling.AsyncPollingMethod
        :keyword int polling_interval: Default waiting time between two polls for LRO operations if no Retry-After header is present.
        :return: An instance of AsyncLROPoller that returns either Product or the result of cls(response)
        :rtype: ~azure.core.polling.AsyncLROPoller[~multiapicredentialdefaultpolicy.v1.models.Product]
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        polling = kwargs.pop('polling', True)  # type: Union[bool, AsyncPollingMethod]
        cls = kwargs.pop('cls', None)  # type: ClsType["_models.Product"]
        lro_delay = kwargs.pop(
            'polling_interval',
            self._config.polling_interval
        )
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))
        cont_token = kwargs.pop('continuation_token', None)  # type: Optional[str]
        if cont_token is None:
            body = product
            request = self._test_lro_request(
                body=body,
                **kwargs
            )
            kwargs.pop('content_type', None)
            pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
            response = pipeline_response.http_response
            if response.status_code not in [200, 204]:
                map_error(status_code=response.status_code, response=response, error_map=error_map)
                error = self._deserialize.failsafe_deserialize(_models.Error, response)
                raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)


        def get_long_running_output(pipeline_response):
            deserialized = self._deserialize('Product', pipeline_response)

            if cls:
                return cls(pipeline_response, deserialized, {})
            return deserialized

        if polling is True: polling_method = AsyncARMPolling(lro_delay,  **kwargs)
        elif polling is False: polling_method = AsyncNoPolling()
        else: polling_method = polling
        if cont_token:
            return AsyncLROPoller.from_continuation_token(
                polling_method=polling_method,
                continuation_token=cont_token,
                client=self._client,
                deserialization_callback=get_long_running_output
            )
        else:
            return AsyncLROPoller(self._client, pipeline_response, get_long_running_output, polling_method)
    begin_test_lro.metadata = {'url': '/multiapi/lro'}  # type: ignore


    def _test_lro_and_paging_request(
        self,
        client_request_id: Optional[str] = None,
        _maxresults: Optional[int] = None,
        _timeout: Optional[int] = 30,
        **kwargs: Any
    ) -> HttpRequest:
        accept = "application/json"

        # Construct URL
        url = self._test_lro_and_paging_request.metadata['url']  # type: ignore

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        if client_request_id is not None:
            header_parameters['client-request-id'] = self._serialize.header("client_request_id", client_request_id, 'str')
        if _maxresults is not None:
            header_parameters['maxresults'] = self._serialize.header("maxresults", _maxresults, 'int')
        if _timeout is not None:
            header_parameters['timeout'] = self._serialize.header("timeout", _timeout, 'int')
        header_parameters['Accept'] = self._serialize.header("accept", accept, 'str')

        return self._client.post(url, query_parameters, header_parameters)
    _test_lro_and_paging_request.metadata = {'url': '/multiapi/lroAndPaging'}  # type: ignore

    async def begin_test_lro_and_paging(
        self,
        client_request_id: Optional[str] = None,
        test_lro_and_paging_options: Optional["_models.TestLroAndPagingOptions"] = None,
        **kwargs: Any
    ) -> AsyncLROPoller[AsyncItemPaged["_models.PagingResult"]]:
        """A long-running paging operation that includes a nextLink that has 10 pages.

        :param client_request_id:
        :type client_request_id: str
        :param test_lro_and_paging_options: Parameter group.
        :type test_lro_and_paging_options: ~multiapicredentialdefaultpolicy.v1.models.TestLroAndPagingOptions
        :keyword callable cls: A custom type or function that will be passed the direct response
        :keyword str continuation_token: A continuation token to restart a poller from a saved state.
        :keyword polling: Pass in True if you'd like the AsyncARMPolling polling method,
         False for no polling, or your own initialized polling object for a personal polling strategy.
        :paramtype polling: bool or ~azure.core.polling.AsyncPollingMethod
        :keyword int polling_interval: Default waiting time between two polls for LRO operations if no Retry-After header is present.
        :return: An instance of AsyncLROPoller that returns an iterator like instance of either PagingResult or the result of cls(response)
        :rtype: ~azure.core.polling.AsyncLROPoller[~azure.core.async_paging.AsyncItemPaged[~multiapicredentialdefaultpolicy.v1.models.PagingResult]]
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["_models.PagingResult"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))

        def prepare_request(next_link=None):
            if not next_link:
                
                _maxresults = None
                _timeout = None
                if test_lro_and_paging_options is not None:
                    _maxresults = test_lro_and_paging_options.maxresults
                    _timeout = test_lro_and_paging_options.timeout
                request = self._test_lro_and_paging_request(
                    client_request_id=client_request_id,
                    _maxresults=_maxresults,
                    _timeout=_timeout,
                    **kwargs
                )
            else:
                
                _maxresults = None
                _timeout = None
                if test_lro_and_paging_options is not None:
                    _maxresults = test_lro_and_paging_options.maxresults
                    _timeout = test_lro_and_paging_options.timeout
                request = self._test_lro_and_paging_request(
                    client_request_id=client_request_id,
                    _maxresults=_maxresults,
                    _timeout=_timeout,
                    **kwargs
                )
                # little hacky, but this code will soon be replaced with code that won't need the hack
                request.method = "get"
                request.url = self._client.format_url(next_link)
            return request

        async def extract_data(pipeline_response):
            deserialized = self._deserialize('PagingResult', pipeline_response)
            list_of_elem = deserialized.values
            if cls:
                list_of_elem = cls(list_of_elem)
            return deserialized.next_link or None, AsyncList(list_of_elem)

        async def get_next(next_link=None):
            request = prepare_request(next_link)

            pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
            response = pipeline_response.http_response

            if response.status_code not in [200]:
                map_error(status_code=response.status_code, response=response, error_map=error_map)
                raise HttpResponseError(response=response, error_format=ARMErrorFormat)

            return pipeline_response

        polling = kwargs.pop('polling', True)  # type: Union[bool, AsyncPollingMethod]
        cls = kwargs.pop('cls', None)  # type: ClsType["_models.PagingResult"]
        lro_delay = kwargs.pop(
            'polling_interval',
            self._config.polling_interval
        )
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))
        cont_token = kwargs.pop('continuation_token', None)  # type: Optional[str]
        if cont_token is None:
            
            _maxresults = None
            _timeout = None
            if test_lro_and_paging_options is not None:
                _maxresults = test_lro_and_paging_options.maxresults
                _timeout = test_lro_and_paging_options.timeout
            request = self._test_lro_and_paging_request(
                client_request_id=client_request_id,
                _maxresults=_maxresults,
                _timeout=_timeout,
                **kwargs
            )
            kwargs.pop('content_type', None)
            pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
            response = pipeline_response.http_response
            if response.status_code not in [200]:
                map_error(status_code=response.status_code, response=response, error_map=error_map)
                raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        def get_long_running_output(pipeline_response):
            async def internal_get_next(next_link=None):
                if next_link is None:
                    return pipeline_response
                else:
                    return await get_next(next_link)

            return AsyncItemPaged(
                internal_get_next, extract_data
            )
        if polling is True: polling_method = AsyncARMPolling(lro_delay,  **kwargs)
        elif polling is False: polling_method = AsyncNoPolling()
        else: polling_method = polling
        if cont_token:
            return AsyncLROPoller.from_continuation_token(
                polling_method=polling_method,
                continuation_token=cont_token,
                client=self._client,
                deserialization_callback=get_long_running_output
            )
        else:
            return AsyncLROPoller(self._client, pipeline_response, get_long_running_output, polling_method)
    begin_test_lro_and_paging.metadata = {'url': '/multiapi/lroAndPaging'}  # type: ignore


    def _test_different_calls_request(
        self,
        greeting_in_english: str,
        **kwargs: Any
    ) -> HttpRequest:
        api_version = "1.0.0"
        accept = "application/json"

        # Construct URL
        url = self._test_different_calls_request.metadata['url']  # type: ignore

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]
        query_parameters['api-version'] = self._serialize.query("api_version", api_version, 'str')

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['greetingInEnglish'] = self._serialize.header("greeting_in_english", greeting_in_english, 'str')
        header_parameters['Accept'] = self._serialize.header("accept", accept, 'str')

        return self._client.get(url, query_parameters, header_parameters)
    _test_different_calls_request.metadata = {'url': '/multiapi/testDifferentCalls'}  # type: ignore

    async def test_different_calls(
        self,
        greeting_in_english: str,
        **kwargs: Any
    ) -> None:
        """Has added parameters across the API versions.

        :param greeting_in_english: pass in 'hello' to pass test.
        :type greeting_in_english: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None, or the result of cls(response)
        :rtype: None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType[None]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))

        request = self._test_different_calls_request(
            greeting_in_english=greeting_in_english,
            **kwargs
        )
        kwargs.pop('content_type', None)

        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.Error, response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        if cls:
            return cls(pipeline_response, None, {})

    test_different_calls.metadata = {'url': '/multiapi/testDifferentCalls'}  # type: ignore

