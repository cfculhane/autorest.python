# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from typing import Any, AsyncIterable, Callable, Dict, Generic, Optional, TypeVar
import warnings

from azure.core.async_paging import AsyncItemPaged, AsyncList
from azure.core.async_paging_method import AsyncBasicPagingMethod
from azure.core.exceptions import ClientAuthenticationError, HttpResponseError, ResourceExistsError, ResourceNotFoundError, map_error
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import AsyncHttpResponse, HttpRequest

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
        :keyword paging_method: The paging strategy to adopt for making requests and exposing metadata.
         Default is AsyncBasicPagingMethod.
        :paramtype paging_method: ~azure.core.async_paging_method.AsyncPagingMethod
        :return: An iterator like instance of either PagingResult or the result of cls(response)
        :rtype: ~azure.core.async_paging.AsyncItemPaged[~multiapidataplane.v3.models.PagingResult]
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        def deserialize_output(pipeline_response):
            return self._deserialize('PagingResult', pipeline_response)

        _initial_request = self._test_paging_initial()
        return AsyncItemPaged(
            paging_method = kwargs.pop("paging_method", AsyncBasicPagingMethod()),
            client=self._client,
            deserialize_output=deserialize_output,
            next_link_name='next_link',
            initial_request=_initial_request,
            item_name='values',
            _cls=kwargs.pop("cls", None),
            **kwargs,
        )

