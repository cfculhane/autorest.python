# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from typing import Any, Optional

from azure.core.rest import HttpRequest
from msrest import Serializer

_SERIALIZER = Serializer()


def build_get200_model204_no_model_default_error200_valid_request(**kwargs: Any) -> HttpRequest:
    """Send a 200 response with valid payload: {'statusCode': '200'}.

    See https://aka.ms/azsdk/python/llcwiki for how to incorporate this request builder into your code flow.

    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's `send_request` method.
     See https://aka.ms/azsdk/python/llcwiki for how to incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest

    Example:
        .. code-block:: python


            # response body for status code(s): 200
            response_body == {
                "statusCode": "str (optional)"
            }

    """
    accept = "application/json"

    # Construct URL
    url = kwargs.pop("template_url", "/http/payloads/200/A/204/none/default/Error/response/200/valid")

    # Construct headers
    header_parameters = kwargs.pop("headers", {})  # type: Dict[str, Any]
    header_parameters["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="GET", url=url, headers=header_parameters, **kwargs)


def build_get200_model204_no_model_default_error204_valid_request(**kwargs: Any) -> HttpRequest:
    """Send a 204 response with no payload.

    See https://aka.ms/azsdk/python/llcwiki for how to incorporate this request builder into your code flow.

    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's `send_request` method.
     See https://aka.ms/azsdk/python/llcwiki for how to incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest

    Example:
        .. code-block:: python


            # response body for status code(s): 200
            response_body == {
                "statusCode": "str (optional)"
            }

    """
    accept = "application/json"

    # Construct URL
    url = kwargs.pop("template_url", "/http/payloads/200/A/204/none/default/Error/response/204/none")

    # Construct headers
    header_parameters = kwargs.pop("headers", {})  # type: Dict[str, Any]
    header_parameters["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="GET", url=url, headers=header_parameters, **kwargs)


def build_get200_model204_no_model_default_error201_invalid_request(**kwargs: Any) -> HttpRequest:
    """Send a 201 response with valid payload: {'statusCode': '201'}.

    See https://aka.ms/azsdk/python/llcwiki for how to incorporate this request builder into your code flow.

    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's `send_request` method.
     See https://aka.ms/azsdk/python/llcwiki for how to incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest

    Example:
        .. code-block:: python


            # response body for status code(s): 200
            response_body == {
                "statusCode": "str (optional)"
            }

    """
    accept = "application/json"

    # Construct URL
    url = kwargs.pop("template_url", "/http/payloads/200/A/204/none/default/Error/response/201/valid")

    # Construct headers
    header_parameters = kwargs.pop("headers", {})  # type: Dict[str, Any]
    header_parameters["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="GET", url=url, headers=header_parameters, **kwargs)


def build_get200_model204_no_model_default_error202_none_request(**kwargs: Any) -> HttpRequest:
    """Send a 202 response with no payload:.

    See https://aka.ms/azsdk/python/llcwiki for how to incorporate this request builder into your code flow.

    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's `send_request` method.
     See https://aka.ms/azsdk/python/llcwiki for how to incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest

    Example:
        .. code-block:: python


            # response body for status code(s): 200
            response_body == {
                "statusCode": "str (optional)"
            }

    """
    accept = "application/json"

    # Construct URL
    url = kwargs.pop("template_url", "/http/payloads/200/A/204/none/default/Error/response/202/none")

    # Construct headers
    header_parameters = kwargs.pop("headers", {})  # type: Dict[str, Any]
    header_parameters["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="GET", url=url, headers=header_parameters, **kwargs)


def build_get200_model204_no_model_default_error400_valid_request(**kwargs: Any) -> HttpRequest:
    """Send a 400 response with valid error payload: {'status': 400, 'message': 'client error'}.

    See https://aka.ms/azsdk/python/llcwiki for how to incorporate this request builder into your code flow.

    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's `send_request` method.
     See https://aka.ms/azsdk/python/llcwiki for how to incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest

    Example:
        .. code-block:: python


            # response body for status code(s): 200
            response_body == {
                "statusCode": "str (optional)"
            }

    """
    accept = "application/json"

    # Construct URL
    url = kwargs.pop("template_url", "/http/payloads/200/A/204/none/default/Error/response/400/valid")

    # Construct headers
    header_parameters = kwargs.pop("headers", {})  # type: Dict[str, Any]
    header_parameters["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="GET", url=url, headers=header_parameters, **kwargs)


def build_get200_model201_model_default_error200_valid_request(**kwargs: Any) -> HttpRequest:
    """Send a 200 response with valid payload: {'statusCode': '200'}.

    See https://aka.ms/azsdk/python/llcwiki for how to incorporate this request builder into your code flow.

    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's `send_request` method.
     See https://aka.ms/azsdk/python/llcwiki for how to incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest

    Example:
        .. code-block:: python


            # response body for status code(s): 200
            response_body == {
                "statusCode": "str (optional)"
            }
            # response body for status code(s): 201
            response_body == {
                "statusCode": "str (optional)",
                "textStatusCode": "str (optional)"
            }

    """
    accept = "application/json"

    # Construct URL
    url = kwargs.pop("template_url", "/http/payloads/200/A/201/B/default/Error/response/200/valid")

    # Construct headers
    header_parameters = kwargs.pop("headers", {})  # type: Dict[str, Any]
    header_parameters["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="GET", url=url, headers=header_parameters, **kwargs)


def build_get200_model201_model_default_error201_valid_request(**kwargs: Any) -> HttpRequest:
    """Send a 201 response with valid payload: {'statusCode': '201', 'textStatusCode': 'Created'}.

    See https://aka.ms/azsdk/python/llcwiki for how to incorporate this request builder into your code flow.

    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's `send_request` method.
     See https://aka.ms/azsdk/python/llcwiki for how to incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest

    Example:
        .. code-block:: python


            # response body for status code(s): 200
            response_body == {
                "statusCode": "str (optional)"
            }
            # response body for status code(s): 201
            response_body == {
                "statusCode": "str (optional)",
                "textStatusCode": "str (optional)"
            }

    """
    accept = "application/json"

    # Construct URL
    url = kwargs.pop("template_url", "/http/payloads/200/A/201/B/default/Error/response/201/valid")

    # Construct headers
    header_parameters = kwargs.pop("headers", {})  # type: Dict[str, Any]
    header_parameters["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="GET", url=url, headers=header_parameters, **kwargs)


def build_get200_model201_model_default_error400_valid_request(**kwargs: Any) -> HttpRequest:
    """Send a 400 response with valid payload: {'code': '400', 'message': 'client error'}.

    See https://aka.ms/azsdk/python/llcwiki for how to incorporate this request builder into your code flow.

    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's `send_request` method.
     See https://aka.ms/azsdk/python/llcwiki for how to incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest

    Example:
        .. code-block:: python


            # response body for status code(s): 200
            response_body == {
                "statusCode": "str (optional)"
            }
            # response body for status code(s): 201
            response_body == {
                "statusCode": "str (optional)",
                "textStatusCode": "str (optional)"
            }

    """
    accept = "application/json"

    # Construct URL
    url = kwargs.pop("template_url", "/http/payloads/200/A/201/B/default/Error/response/400/valid")

    # Construct headers
    header_parameters = kwargs.pop("headers", {})  # type: Dict[str, Any]
    header_parameters["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="GET", url=url, headers=header_parameters, **kwargs)


def build_get200_model_a201_model_c404_model_d_default_error200_valid_request(**kwargs: Any) -> HttpRequest:
    """Send a 200 response with valid payload: {'statusCode': '200'}.

    See https://aka.ms/azsdk/python/llcwiki for how to incorporate this request builder into your code flow.

    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's `send_request` method.
     See https://aka.ms/azsdk/python/llcwiki for how to incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest

    Example:
        .. code-block:: python


            # response body for status code(s): 200
            response_body == {
                "statusCode": "str (optional)"
            }
            # response body for status code(s): 201
            response_body == {
                "httpCode": "str (optional)"
            }
            # response body for status code(s): 404
            response_body == {
                "httpStatusCode": "str (optional)"
            }

    """
    accept = "application/json"

    # Construct URL
    url = kwargs.pop("template_url", "/http/payloads/200/A/201/C/404/D/default/Error/response/200/valid")

    # Construct headers
    header_parameters = kwargs.pop("headers", {})  # type: Dict[str, Any]
    header_parameters["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="GET", url=url, headers=header_parameters, **kwargs)


def build_get200_model_a201_model_c404_model_d_default_error201_valid_request(**kwargs: Any) -> HttpRequest:
    """Send a 200 response with valid payload: {'httpCode': '201'}.

    See https://aka.ms/azsdk/python/llcwiki for how to incorporate this request builder into your code flow.

    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's `send_request` method.
     See https://aka.ms/azsdk/python/llcwiki for how to incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest

    Example:
        .. code-block:: python


            # response body for status code(s): 200
            response_body == {
                "statusCode": "str (optional)"
            }
            # response body for status code(s): 201
            response_body == {
                "httpCode": "str (optional)"
            }
            # response body for status code(s): 404
            response_body == {
                "httpStatusCode": "str (optional)"
            }

    """
    accept = "application/json"

    # Construct URL
    url = kwargs.pop("template_url", "/http/payloads/200/A/201/C/404/D/default/Error/response/201/valid")

    # Construct headers
    header_parameters = kwargs.pop("headers", {})  # type: Dict[str, Any]
    header_parameters["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="GET", url=url, headers=header_parameters, **kwargs)


def build_get200_model_a201_model_c404_model_d_default_error404_valid_request(**kwargs: Any) -> HttpRequest:
    """Send a 200 response with valid payload: {'httpStatusCode': '404'}.

    See https://aka.ms/azsdk/python/llcwiki for how to incorporate this request builder into your code flow.

    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's `send_request` method.
     See https://aka.ms/azsdk/python/llcwiki for how to incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest

    Example:
        .. code-block:: python


            # response body for status code(s): 200
            response_body == {
                "statusCode": "str (optional)"
            }
            # response body for status code(s): 201
            response_body == {
                "httpCode": "str (optional)"
            }
            # response body for status code(s): 404
            response_body == {
                "httpStatusCode": "str (optional)"
            }

    """
    accept = "application/json"

    # Construct URL
    url = kwargs.pop("template_url", "/http/payloads/200/A/201/C/404/D/default/Error/response/404/valid")

    # Construct headers
    header_parameters = kwargs.pop("headers", {})  # type: Dict[str, Any]
    header_parameters["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="GET", url=url, headers=header_parameters, **kwargs)


def build_get200_model_a201_model_c404_model_d_default_error400_valid_request(**kwargs: Any) -> HttpRequest:
    """Send a 400 response with valid payload: {'code': '400', 'message': 'client error'}.

    See https://aka.ms/azsdk/python/llcwiki for how to incorporate this request builder into your code flow.

    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's `send_request` method.
     See https://aka.ms/azsdk/python/llcwiki for how to incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest

    Example:
        .. code-block:: python


            # response body for status code(s): 200
            response_body == {
                "statusCode": "str (optional)"
            }
            # response body for status code(s): 201
            response_body == {
                "httpCode": "str (optional)"
            }
            # response body for status code(s): 404
            response_body == {
                "httpStatusCode": "str (optional)"
            }

    """
    accept = "application/json"

    # Construct URL
    url = kwargs.pop("template_url", "/http/payloads/200/A/201/C/404/D/default/Error/response/400/valid")

    # Construct headers
    header_parameters = kwargs.pop("headers", {})  # type: Dict[str, Any]
    header_parameters["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="GET", url=url, headers=header_parameters, **kwargs)


def build_get202_none204_none_default_error202_none_request(**kwargs: Any) -> HttpRequest:
    """Send a 202 response with no payload.

    See https://aka.ms/azsdk/python/llcwiki for how to incorporate this request builder into your code flow.

    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's `send_request` method.
     See https://aka.ms/azsdk/python/llcwiki for how to incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest
    """
    accept = "application/json"

    # Construct URL
    url = kwargs.pop("template_url", "/http/payloads/202/none/204/none/default/Error/response/202/none")

    # Construct headers
    header_parameters = kwargs.pop("headers", {})  # type: Dict[str, Any]
    header_parameters["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="GET", url=url, headers=header_parameters, **kwargs)


def build_get202_none204_none_default_error204_none_request(**kwargs: Any) -> HttpRequest:
    """Send a 204 response with no payload.

    See https://aka.ms/azsdk/python/llcwiki for how to incorporate this request builder into your code flow.

    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's `send_request` method.
     See https://aka.ms/azsdk/python/llcwiki for how to incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest
    """
    accept = "application/json"

    # Construct URL
    url = kwargs.pop("template_url", "/http/payloads/202/none/204/none/default/Error/response/204/none")

    # Construct headers
    header_parameters = kwargs.pop("headers", {})  # type: Dict[str, Any]
    header_parameters["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="GET", url=url, headers=header_parameters, **kwargs)


def build_get202_none204_none_default_error400_valid_request(**kwargs: Any) -> HttpRequest:
    """Send a 400 response with valid payload: {'code': '400', 'message': 'client error'}.

    See https://aka.ms/azsdk/python/llcwiki for how to incorporate this request builder into your code flow.

    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's `send_request` method.
     See https://aka.ms/azsdk/python/llcwiki for how to incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest
    """
    accept = "application/json"

    # Construct URL
    url = kwargs.pop("template_url", "/http/payloads/202/none/204/none/default/Error/response/400/valid")

    # Construct headers
    header_parameters = kwargs.pop("headers", {})  # type: Dict[str, Any]
    header_parameters["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="GET", url=url, headers=header_parameters, **kwargs)


def build_get202_none204_none_default_none202_invalid_request(**kwargs: Any) -> HttpRequest:
    """Send a 202 response with an unexpected payload {'property': 'value'}.

    See https://aka.ms/azsdk/python/llcwiki for how to incorporate this request builder into your code flow.

    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's `send_request` method.
     See https://aka.ms/azsdk/python/llcwiki for how to incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest
    """

    # Construct URL
    url = kwargs.pop("template_url", "/http/payloads/202/none/204/none/default/none/response/202/invalid")

    return HttpRequest(method="GET", url=url, **kwargs)


def build_get202_none204_none_default_none204_none_request(**kwargs: Any) -> HttpRequest:
    """Send a 204 response with no payload.

    See https://aka.ms/azsdk/python/llcwiki for how to incorporate this request builder into your code flow.

    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's `send_request` method.
     See https://aka.ms/azsdk/python/llcwiki for how to incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest
    """

    # Construct URL
    url = kwargs.pop("template_url", "/http/payloads/202/none/204/none/default/none/response/204/none")

    return HttpRequest(method="GET", url=url, **kwargs)


def build_get202_none204_none_default_none400_none_request(**kwargs: Any) -> HttpRequest:
    """Send a 400 response with no payload.

    See https://aka.ms/azsdk/python/llcwiki for how to incorporate this request builder into your code flow.

    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's `send_request` method.
     See https://aka.ms/azsdk/python/llcwiki for how to incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest
    """

    # Construct URL
    url = kwargs.pop("template_url", "/http/payloads/202/none/204/none/default/none/response/400/none")

    return HttpRequest(method="GET", url=url, **kwargs)


def build_get202_none204_none_default_none400_invalid_request(**kwargs: Any) -> HttpRequest:
    """Send a 400 response with an unexpected payload {'property': 'value'}.

    See https://aka.ms/azsdk/python/llcwiki for how to incorporate this request builder into your code flow.

    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's `send_request` method.
     See https://aka.ms/azsdk/python/llcwiki for how to incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest
    """

    # Construct URL
    url = kwargs.pop("template_url", "/http/payloads/202/none/204/none/default/none/response/400/invalid")

    return HttpRequest(method="GET", url=url, **kwargs)


def build_get_default_model_a200_valid_request(**kwargs: Any) -> HttpRequest:
    """Send a 200 response with valid payload: {'statusCode': '200'}.

    See https://aka.ms/azsdk/python/llcwiki for how to incorporate this request builder into your code flow.

    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's `send_request` method.
     See https://aka.ms/azsdk/python/llcwiki for how to incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest

    Example:
        .. code-block:: python


            # response body for status code(s): 200
            response_body == {
                "statusCode": "str (optional)"
            }

    """
    accept = "application/json"

    # Construct URL
    url = kwargs.pop("template_url", "/http/payloads/default/A/response/200/valid")

    # Construct headers
    header_parameters = kwargs.pop("headers", {})  # type: Dict[str, Any]
    header_parameters["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="GET", url=url, headers=header_parameters, **kwargs)


def build_get_default_model_a200_none_request(**kwargs: Any) -> HttpRequest:
    """Send a 200 response with no payload.

    See https://aka.ms/azsdk/python/llcwiki for how to incorporate this request builder into your code flow.

    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's `send_request` method.
     See https://aka.ms/azsdk/python/llcwiki for how to incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest

    Example:
        .. code-block:: python


            # response body for status code(s): 200
            response_body == {
                "statusCode": "str (optional)"
            }

    """
    accept = "application/json"

    # Construct URL
    url = kwargs.pop("template_url", "/http/payloads/default/A/response/200/none")

    # Construct headers
    header_parameters = kwargs.pop("headers", {})  # type: Dict[str, Any]
    header_parameters["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="GET", url=url, headers=header_parameters, **kwargs)


def build_get_default_model_a400_valid_request(**kwargs: Any) -> HttpRequest:
    """Send a 400 response with valid payload: {'statusCode': '400'}.

    See https://aka.ms/azsdk/python/llcwiki for how to incorporate this request builder into your code flow.

    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's `send_request` method.
     See https://aka.ms/azsdk/python/llcwiki for how to incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest
    """
    accept = "application/json"

    # Construct URL
    url = kwargs.pop("template_url", "/http/payloads/default/A/response/400/valid")

    # Construct headers
    header_parameters = kwargs.pop("headers", {})  # type: Dict[str, Any]
    header_parameters["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="GET", url=url, headers=header_parameters, **kwargs)


def build_get_default_model_a400_none_request(**kwargs: Any) -> HttpRequest:
    """Send a 400 response with no payload.

    See https://aka.ms/azsdk/python/llcwiki for how to incorporate this request builder into your code flow.

    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's `send_request` method.
     See https://aka.ms/azsdk/python/llcwiki for how to incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest
    """
    accept = "application/json"

    # Construct URL
    url = kwargs.pop("template_url", "/http/payloads/default/A/response/400/none")

    # Construct headers
    header_parameters = kwargs.pop("headers", {})  # type: Dict[str, Any]
    header_parameters["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="GET", url=url, headers=header_parameters, **kwargs)


def build_get_default_none200_invalid_request(**kwargs: Any) -> HttpRequest:
    """Send a 200 response with invalid payload: {'statusCode': '200'}.

    See https://aka.ms/azsdk/python/llcwiki for how to incorporate this request builder into your code flow.

    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's `send_request` method.
     See https://aka.ms/azsdk/python/llcwiki for how to incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest
    """

    # Construct URL
    url = kwargs.pop("template_url", "/http/payloads/default/none/response/200/invalid")

    return HttpRequest(method="GET", url=url, **kwargs)


def build_get_default_none200_none_request(**kwargs: Any) -> HttpRequest:
    """Send a 200 response with no payload.

    See https://aka.ms/azsdk/python/llcwiki for how to incorporate this request builder into your code flow.

    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's `send_request` method.
     See https://aka.ms/azsdk/python/llcwiki for how to incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest
    """

    # Construct URL
    url = kwargs.pop("template_url", "/http/payloads/default/none/response/200/none")

    return HttpRequest(method="GET", url=url, **kwargs)


def build_get_default_none400_invalid_request(**kwargs: Any) -> HttpRequest:
    """Send a 400 response with valid payload: {'statusCode': '400'}.

    See https://aka.ms/azsdk/python/llcwiki for how to incorporate this request builder into your code flow.

    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's `send_request` method.
     See https://aka.ms/azsdk/python/llcwiki for how to incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest
    """

    # Construct URL
    url = kwargs.pop("template_url", "/http/payloads/default/none/response/400/invalid")

    return HttpRequest(method="GET", url=url, **kwargs)


def build_get_default_none400_none_request(**kwargs: Any) -> HttpRequest:
    """Send a 400 response with no payload.

    See https://aka.ms/azsdk/python/llcwiki for how to incorporate this request builder into your code flow.

    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's `send_request` method.
     See https://aka.ms/azsdk/python/llcwiki for how to incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest
    """

    # Construct URL
    url = kwargs.pop("template_url", "/http/payloads/default/none/response/400/none")

    return HttpRequest(method="GET", url=url, **kwargs)


def build_get200_model_a200_none_request(**kwargs: Any) -> HttpRequest:
    """Send a 200 response with no payload, when a payload is expected - client should return a null
    object of thde type for model A.

    See https://aka.ms/azsdk/python/llcwiki for how to incorporate this request builder into your code flow.

    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's `send_request` method.
     See https://aka.ms/azsdk/python/llcwiki for how to incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest

    Example:
        .. code-block:: python


            # response body for status code(s): 200
            response_body == {
                "statusCode": "str (optional)"
            }

    """
    accept = "application/json"

    # Construct URL
    url = kwargs.pop("template_url", "/http/payloads/200/A/response/200/none")

    # Construct headers
    header_parameters = kwargs.pop("headers", {})  # type: Dict[str, Any]
    header_parameters["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="GET", url=url, headers=header_parameters, **kwargs)


def build_get200_model_a200_valid_request(**kwargs: Any) -> HttpRequest:
    """Send a 200 response with payload {'statusCode': '200'}.

    See https://aka.ms/azsdk/python/llcwiki for how to incorporate this request builder into your code flow.

    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's `send_request` method.
     See https://aka.ms/azsdk/python/llcwiki for how to incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest

    Example:
        .. code-block:: python


            # response body for status code(s): 200
            response_body == {
                "statusCode": "str (optional)"
            }

    """
    accept = "application/json"

    # Construct URL
    url = kwargs.pop("template_url", "/http/payloads/200/A/response/200/valid")

    # Construct headers
    header_parameters = kwargs.pop("headers", {})  # type: Dict[str, Any]
    header_parameters["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="GET", url=url, headers=header_parameters, **kwargs)


def build_get200_model_a200_invalid_request(**kwargs: Any) -> HttpRequest:
    """Send a 200 response with invalid payload {'statusCodeInvalid': '200'}.

    See https://aka.ms/azsdk/python/llcwiki for how to incorporate this request builder into your code flow.

    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's `send_request` method.
     See https://aka.ms/azsdk/python/llcwiki for how to incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest

    Example:
        .. code-block:: python


            # response body for status code(s): 200
            response_body == {
                "statusCode": "str (optional)"
            }

    """
    accept = "application/json"

    # Construct URL
    url = kwargs.pop("template_url", "/http/payloads/200/A/response/200/invalid")

    # Construct headers
    header_parameters = kwargs.pop("headers", {})  # type: Dict[str, Any]
    header_parameters["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="GET", url=url, headers=header_parameters, **kwargs)


def build_get200_model_a400_none_request(**kwargs: Any) -> HttpRequest:
    """Send a 400 response with no payload client should treat as an http error with no error model.

    See https://aka.ms/azsdk/python/llcwiki for how to incorporate this request builder into your code flow.

    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's `send_request` method.
     See https://aka.ms/azsdk/python/llcwiki for how to incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest

    Example:
        .. code-block:: python


            # response body for status code(s): 200
            response_body == {
                "statusCode": "str (optional)"
            }

    """
    accept = "application/json"

    # Construct URL
    url = kwargs.pop("template_url", "/http/payloads/200/A/response/400/none")

    # Construct headers
    header_parameters = kwargs.pop("headers", {})  # type: Dict[str, Any]
    header_parameters["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="GET", url=url, headers=header_parameters, **kwargs)


def build_get200_model_a400_valid_request(**kwargs: Any) -> HttpRequest:
    """Send a 200 response with payload {'statusCode': '400'}.

    See https://aka.ms/azsdk/python/llcwiki for how to incorporate this request builder into your code flow.

    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's `send_request` method.
     See https://aka.ms/azsdk/python/llcwiki for how to incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest

    Example:
        .. code-block:: python


            # response body for status code(s): 200
            response_body == {
                "statusCode": "str (optional)"
            }

    """
    accept = "application/json"

    # Construct URL
    url = kwargs.pop("template_url", "/http/payloads/200/A/response/400/valid")

    # Construct headers
    header_parameters = kwargs.pop("headers", {})  # type: Dict[str, Any]
    header_parameters["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="GET", url=url, headers=header_parameters, **kwargs)


def build_get200_model_a400_invalid_request(**kwargs: Any) -> HttpRequest:
    """Send a 200 response with invalid payload {'statusCodeInvalid': '400'}.

    See https://aka.ms/azsdk/python/llcwiki for how to incorporate this request builder into your code flow.

    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's `send_request` method.
     See https://aka.ms/azsdk/python/llcwiki for how to incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest

    Example:
        .. code-block:: python


            # response body for status code(s): 200
            response_body == {
                "statusCode": "str (optional)"
            }

    """
    accept = "application/json"

    # Construct URL
    url = kwargs.pop("template_url", "/http/payloads/200/A/response/400/invalid")

    # Construct headers
    header_parameters = kwargs.pop("headers", {})  # type: Dict[str, Any]
    header_parameters["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="GET", url=url, headers=header_parameters, **kwargs)


def build_get200_model_a202_valid_request(**kwargs: Any) -> HttpRequest:
    """Send a 202 response with payload {'statusCode': '202'}.

    See https://aka.ms/azsdk/python/llcwiki for how to incorporate this request builder into your code flow.

    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's `send_request` method.
     See https://aka.ms/azsdk/python/llcwiki for how to incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest

    Example:
        .. code-block:: python


            # response body for status code(s): 200
            response_body == {
                "statusCode": "str (optional)"
            }

    """
    accept = "application/json"

    # Construct URL
    url = kwargs.pop("template_url", "/http/payloads/200/A/response/202/valid")

    # Construct headers
    header_parameters = kwargs.pop("headers", {})  # type: Dict[str, Any]
    header_parameters["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="GET", url=url, headers=header_parameters, **kwargs)
