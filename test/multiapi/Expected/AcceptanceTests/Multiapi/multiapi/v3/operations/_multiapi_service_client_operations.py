# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from typing import TYPE_CHECKING
import warnings

from azure.core.exceptions import ClientAuthenticationError, HttpResponseError, ResourceExistsError, ResourceNotFoundError, map_error
from azure.core.paging import ItemPaged
from azure.core.paging_method import BasicPagingMethod
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import HttpRequest, HttpResponse
from azure.mgmt.core.exceptions import ARMErrorFormat

from .. import models

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from typing import Any, Callable, Dict, Generic, Iterable, Optional, TypeVar

    T = TypeVar('T')
    ClsType = Optional[Callable[[PipelineResponse[HttpRequest, HttpResponse], T, Dict[str, Any]], Any]]

class MultiapiServiceClientOperationsMixin(object):

    def _test_paging_initial(
        self,
        **kwargs  # type: Any
    ):
        # type: (...) -> HttpRequest
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
        **kwargs  # type: Any
    ):
        # type: (...) -> Iterable["models.PagingResult"]
        """Returns ModelThree with optionalProperty 'paged'.

        :keyword callable cls: A custom type or function that will be passed the direct response
        :keyword paging_method: The paging strategy to adopt for making requests and exposing metadata.
         Default is BasicPagingMethod.
        :paramtype paging_method: ~azure.core.paging_method.PagingMethod
        :return: An iterator like instance of either PagingResult or the result of cls(response)
        :rtype: ~azure.core.paging.ItemPaged[~multiapi.v3.models.PagingResult]
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        def deserialize_output(pipeline_response):
            return self._deserialize('PagingResult', pipeline_response)

        _initial_request = self._test_paging_initial()
        return ItemPaged(
            paging_method = kwargs.pop("paging_method", BasicPagingMethod()),
            client=self._client,
            deserialize_output=deserialize_output,
            initial_request=_initial_request,
            item_name='values',
            _cls=kwargs.pop("cls", None),
            **kwargs,
        )
