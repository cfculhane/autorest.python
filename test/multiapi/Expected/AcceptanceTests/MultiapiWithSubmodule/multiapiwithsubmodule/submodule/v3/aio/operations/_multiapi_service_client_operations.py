# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
import functools
from typing import Any, AsyncIterable, Callable, Dict, Generic, Optional, TypeVar
import warnings

from azure.core.async_paging import AsyncItemPaged, AsyncList
from azure.core.exceptions import ClientAuthenticationError, HttpResponseError, ResourceExistsError, ResourceNotFoundError, map_error
from azure.core.paging import ContinueWithNextLink
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import AsyncHttpResponse, HttpRequest
from azure.mgmt.core.exceptions import ARMErrorFormat

from ... import models as _models

T = TypeVar('T')
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, AsyncHttpResponse], T, Dict[str, Any]], Any]]

class MultiapiServiceClientOperationsMixin:

    def _test_paging_initial(
        self,
        **kwargs
    ) -> HttpRequest:
        accept = "application/json"

        # Construct URL
        url = self._test_paging_initial.metadata['url']  # type: ignore

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Accept'] = self._serialize.header("accept", accept, 'str')

        request = self._client.get(url, query_parameters, header_parameters)
        return request
    _test_paging_initial.metadata = {'url': '/multiapi/paging'}  # type: ignore

    def test_paging(
        self,
        **kwargs
    ) -> AsyncIterable["_models.PagingResult"]:
        """Returns ModelThree with optionalProperty 'paged'.

        :keyword callable cls: A custom type or function that will be passed the direct response
        :keyword paging_method: The paging strategy to adopt for making requests and processing the
         response. Default is ContinueWithNextLink. You can pass in
         either an initialized or uninitialized custom paging method. If you pass in an uninitialized
         paging method, make sure your paging method class can input kwargs, as we will initialize your
         paging method with the parameters we would pass into the default paging method + extra kwargs.
        :paramtype paging_method: ~azure.core.paging.PagingMethod
        :return: An iterator like instance of either PagingResult or the result of cls(response)
        :rtype: ~azure.core.async_paging.AsyncItemPaged[~multiapiwithsubmodule.submodule.v3.models.PagingResult]
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        def deserialize_output(pipeline_response):
            return self._deserialize('PagingResult', pipeline_response)

        _initial_request = self._test_paging_initial(
        )

        paging_method = kwargs.pop("paging_method", ContinueWithNextLink)

        try:
            paging_method = paging_method(**kwargs)
        except:
            pass

        return AsyncItemPaged(
            paging_method=paging_method,
            deserialize_output=deserialize_output,
            client=self._client,
            continuation_token_location='next_link',
            initial_state=_initial_request,
            item_name='values',
            _cls=kwargs.pop("cls", None),
            **kwargs,
        )

    async def test_different_calls(
        self,
        greeting_in_english: str,
        greeting_in_chinese: Optional[str] = None,
        greeting_in_french: Optional[str] = None,
        **kwargs
    ) -> None:
        """Has added parameters across the API versions.

        :param greeting_in_english: pass in 'hello' to pass test.
        :type greeting_in_english: str
        :param greeting_in_chinese: pass in 'nihao' to pass test.
        :type greeting_in_chinese: str
        :param greeting_in_french: pass in 'bonjour' to pass test.
        :type greeting_in_french: str
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
        api_version = "3.0.0"
        accept = "application/json"

        # Construct URL
        url = self.test_different_calls.metadata['url']  # type: ignore

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]
        query_parameters['api-version'] = self._serialize.query("api_version", api_version, 'str')

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['greetingInEnglish'] = self._serialize.header("greeting_in_english", greeting_in_english, 'str')
        if greeting_in_chinese is not None:
            header_parameters['greetingInChinese'] = self._serialize.header("greeting_in_chinese", greeting_in_chinese, 'str')
        if greeting_in_french is not None:
            header_parameters['greetingInFrench'] = self._serialize.header("greeting_in_french", greeting_in_french, 'str')
        header_parameters['Accept'] = self._serialize.header("accept", accept, 'str')

        request = self._client.get(url, query_parameters, header_parameters)
        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize(_models.Error, response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        if cls:
            return cls(pipeline_response, None, {})

    test_different_calls.metadata = {'url': '/multiapi/testDifferentCalls'}  # type: ignore
