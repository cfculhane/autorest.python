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

from azure.core.exceptions import (
    ClientAuthenticationError,
    HttpResponseError,
    ResourceExistsError,
    ResourceNotFoundError,
    map_error,
)
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import HttpResponse
from azure.core.rest import HttpRequest
from azure.core.tracing.decorator import distributed_trace
from msrest import Serializer

from .. import models as _models
from .._vendor import _convert_request, _get_from_dict

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from typing import Any, Callable, Dict, Generic, Optional, TypeVar

    T = TypeVar("T")
    ClsType = Optional[Callable[[PipelineResponse[HttpRequest, HttpResponse], T, Dict[str, Any]], Any]]

_SERIALIZER = Serializer()
_SERIALIZER.client_side_validation = False
# fmt: off

def build_get_report_request(
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    _headers = kwargs.pop("headers", {}) or {}  # type: Dict[str, Any]
    _params = kwargs.pop("params", {}) or {}  # type: Dict[str, Any]

    qualifier = kwargs.pop('qualifier', _get_from_dict(_params, 'qualifier') or None)  # type: Optional[str]
    accept = _get_from_dict(_headers, 'Accept') or "application/json"

    # Construct URL
    url = kwargs.pop("template_url", '/report')

    # Construct parameters
    if qualifier is not None:
        _params['qualifier'] = _SERIALIZER.query("qualifier", qualifier, 'str')

    # Construct headers
    _headers['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="GET",
        url=url,
        params=_params,
        headers=_headers,
        **kwargs
    )


def build_get_optional_report_request(
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    _headers = kwargs.pop("headers", {}) or {}  # type: Dict[str, Any]
    _params = kwargs.pop("params", {}) or {}  # type: Dict[str, Any]

    qualifier = kwargs.pop('qualifier', _get_from_dict(_params, 'qualifier') or None)  # type: Optional[str]
    accept = _get_from_dict(_headers, 'Accept') or "application/json"

    # Construct URL
    url = kwargs.pop("template_url", '/report/optional')

    # Construct parameters
    if qualifier is not None:
        _params['qualifier'] = _SERIALIZER.query("qualifier", qualifier, 'str')

    # Construct headers
    _headers['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="GET",
        url=url,
        params=_params,
        headers=_headers,
        **kwargs
    )

# fmt: on
class AutoRestReportServiceOperationsMixin(object):
    @distributed_trace
    def get_report(
        self,
        qualifier=None,  # type: Optional[str]
        **kwargs  # type: Any
    ):
        # type: (...) -> Dict[str, int]
        """Get test coverage report.

        :param qualifier: If specified, qualifies the generated report further (e.g. '2.7' vs '3.5' in
         for Python). The only effect is, that generators that run all tests several times, can
         distinguish the generated reports.
        :type qualifier: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: dict mapping str to int, or the result of cls(response)
        :rtype: dict[str, int]
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop("cls", None)  # type: ClsType[Dict[str, int]]
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = kwargs.pop("headers", {}) or {}  # type: Dict[str, Any]
        _params = kwargs.pop("params", {}) or {}  # type: Dict[str, Any]

        request = build_get_report_request(
            qualifier=qualifier,
            template_url=self.get_report.metadata["url"],
            headers=_headers,
            params=_params,
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)

        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.Error, pipeline_response)
            raise HttpResponseError(response=response, model=error)

        deserialized = self._deserialize("{int}", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    get_report.metadata = {"url": "/report"}  # type: ignore

    @distributed_trace
    def get_optional_report(
        self,
        qualifier=None,  # type: Optional[str]
        **kwargs  # type: Any
    ):
        # type: (...) -> Dict[str, int]
        """Get optional test coverage report.

        :param qualifier: If specified, qualifies the generated report further (e.g. '2.7' vs '3.5' in
         for Python). The only effect is, that generators that run all tests several times, can
         distinguish the generated reports.
        :type qualifier: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: dict mapping str to int, or the result of cls(response)
        :rtype: dict[str, int]
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop("cls", None)  # type: ClsType[Dict[str, int]]
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = kwargs.pop("headers", {}) or {}  # type: Dict[str, Any]
        _params = kwargs.pop("params", {}) or {}  # type: Dict[str, Any]

        request = build_get_optional_report_request(
            qualifier=qualifier,
            template_url=self.get_optional_report.metadata["url"],
            headers=_headers,
            params=_params,
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)

        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.Error, pipeline_response)
            raise HttpResponseError(response=response, model=error)

        deserialized = self._deserialize("{int}", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    get_optional_report.metadata = {"url": "/report/optional"}  # type: ignore
