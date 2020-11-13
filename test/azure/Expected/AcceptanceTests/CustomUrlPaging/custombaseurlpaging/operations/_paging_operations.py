# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
import functools
from typing import TYPE_CHECKING
import warnings

from azure.core.exceptions import ClientAuthenticationError, HttpResponseError, ResourceExistsError, ResourceNotFoundError, map_error
from azure.core.paging import ItemPaged
from azure.core.paging_method import BasicPagingMethod, DifferentNextOperationPagingMethod
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import HttpRequest, HttpResponse
from azure.core.tracing.decorator import distributed_trace
from azure.mgmt.core.exceptions import ARMErrorFormat

from .. import models as _models

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from typing import Any, Callable, Dict, Generic, Iterable, Optional, TypeVar

    T = TypeVar('T')
    ClsType = Optional[Callable[[PipelineResponse[HttpRequest, HttpResponse], T, Dict[str, Any]], Any]]

class PagingOperations(object):
    """PagingOperations operations.

    You should not instantiate this class directly. Instead, you should create a Client instance that
    instantiates it for you and attaches it as an attribute.

    :ivar models: Alias to model classes used in this operation group.
    :type models: ~custombaseurlpaging.models
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

    def _get_pages_partial_url_initial(
        self,
        account_name,  # type: str
        **kwargs  # type: Any
    ):
        # type: (...) -> HttpRequest
        accept = "application/json"

        # Construct URL
        url = self._get_pages_partial_url_initial.metadata['url']  # type: ignore
        path_format_arguments = {
            'accountName': self._serialize.url("account_name", account_name, 'str', skip_quote=True),
            'host': self._serialize.url("self._config.host", self._config.host, 'str', skip_quote=True),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Accept'] = self._serialize.header("accept", accept, 'str')

        request = self._client.get(url, query_parameters, header_parameters)
        return request
    _get_pages_partial_url_initial.metadata = {'url': '/paging/customurl/partialnextlink'}  # type: ignore

    @distributed_trace
    def get_pages_partial_url(
        self,
        account_name,  # type: str
        **kwargs  # type: Any
    ):
        # type: (...) -> Iterable["_models.ProductResult"]
        """A paging operation that combines custom url, paging and partial URL and expect to concat after
        host.

        :param account_name: Account Name.
        :type account_name: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :keyword paging_method: The paging strategy to adopt for making requests and exposing metadata.
         Default is BasicPagingMethod.
        :paramtype paging_method: ~azure.core.paging_method.PagingMethod
        :return: An iterator like instance of either ProductResult or the result of cls(response)
        :rtype: ~azure.core.paging.ItemPaged[~custombaseurlpaging.models.ProductResult]
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        def deserialize_output(pipeline_response):
            return self._deserialize('ProductResult', pipeline_response)

        path_format_arguments = {
            'accountName': self._serialize.url("account_name", account_name, 'str', skip_quote=True),
            'host': self._serialize.url("self._config.host", self._config.host, 'str', skip_quote=True),
        }

        _initial_request = self._get_pages_partial_url_initial(
            account_name=account_name,
        )
        return ItemPaged(
            paging_method = kwargs.pop("paging_method", BasicPagingMethod()),
            client=self._client,
            deserialize_output=deserialize_output,
            next_link_name='next_link',
            initial_request=_initial_request,
            path_format_arguments=path_format_arguments,
            item_name='values',
            _cls=kwargs.pop("cls", None),
            **kwargs,
        )


    def _get_pages_partial_url_operation_initial(
        self,
        account_name,  # type: str
        **kwargs  # type: Any
    ):
        # type: (...) -> HttpRequest
        accept = "application/json"

        # Construct URL
        url = self._get_pages_partial_url_operation_initial.metadata['url']  # type: ignore
        path_format_arguments = {
            'accountName': self._serialize.url("account_name", account_name, 'str', skip_quote=True),
            'host': self._serialize.url("self._config.host", self._config.host, 'str', skip_quote=True),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Accept'] = self._serialize.header("accept", accept, 'str')

        request = self._client.get(url, query_parameters, header_parameters)
        return request
    _get_pages_partial_url_operation_initial.metadata = {'url': '/paging/customurl/partialnextlinkop'}  # type: ignore

    def _get_pages_partial_url_operation_next(
        self,
        next_link,  # type: str
        account_name,  # type: str
        **kwargs  # type: Any
    ):
        # type: (...) -> HttpRequest
        accept = "application/json"

        # Construct URL
        url = self._get_pages_partial_url_operation_next.metadata['url']  # type: ignore
        path_format_arguments = {
            'nextLink': self._serialize.url("next_link", next_link, 'str', skip_quote=True),
            'accountName': self._serialize.url("account_name", account_name, 'str', skip_quote=True),
            'host': self._serialize.url("self._config.host", self._config.host, 'str', skip_quote=True),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Accept'] = self._serialize.header("accept", accept, 'str')

        request = self._client.get(url, query_parameters, header_parameters)
        return request
    _get_pages_partial_url_operation_next.metadata = {'url': '/paging/customurl/{nextLink}'}  # type: ignore

    @distributed_trace
    def get_pages_partial_url_operation(
        self,
        account_name,  # type: str
        **kwargs  # type: Any
    ):
        # type: (...) -> Iterable["_models.ProductResult"]
        """A paging operation that combines custom url, paging and partial URL with next operation.

        :param account_name: Account Name.
        :type account_name: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :keyword paging_method: The paging strategy to adopt for making requests and exposing metadata.
         Default is DifferentNextOperationPagingMethod.
        :paramtype paging_method: ~azure.core.paging_method.PagingMethod
        :return: An iterator like instance of either ProductResult or the result of cls(response)
        :rtype: ~azure.core.paging.ItemPaged[~custombaseurlpaging.models.ProductResult]
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        def deserialize_output(pipeline_response):
            return self._deserialize('ProductResult', pipeline_response)

        _initial_request = self._get_pages_partial_url_operation_initial(
            account_name=account_name,
        )
        _next_request_partial = functools.partial(
            self._get_pages_partial_url_operation_next,
            account_name=account_name,
        )
        return ItemPaged(
            paging_method = kwargs.pop("paging_method", DifferentNextOperationPagingMethod()),
            client=self._client,
            deserialize_output=deserialize_output,
            next_link_name='next_link',
            prepare_next_request=_next_request_partial,
            initial_request=_initial_request,
            item_name='values',
            _cls=kwargs.pop("cls", None),
            **kwargs,
        )

