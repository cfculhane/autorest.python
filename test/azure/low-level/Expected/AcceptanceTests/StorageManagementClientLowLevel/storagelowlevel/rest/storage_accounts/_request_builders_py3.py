# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from typing import Any, Optional, Union

from azure.core.pipeline.transport._base import _format_url_section
from azure.core.rest import HttpRequest
from msrest import Serializer

_SERIALIZER = Serializer()


def build_check_name_availability_request(
    subscription_id: str, *, json: Any = None, content: Any = None, **kwargs: Any
) -> HttpRequest:
    """Checks that account name is valid and is not in use.

    See https://aka.ms/azsdk/python/llcwiki for how to incorporate this request builder into your
    code flow.

    :param subscription_id: Gets subscription credentials which uniquely identify Microsoft Azure
     subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :keyword json: Pass in a JSON-serializable object (usually a dictionary). See the template in
     our example to find the input shape. The name of the storage account within the specified
     resource group. Storage account names must be between 3 and 24 characters in length and use
     numbers and lower-case letters only.
    :paramtype json: Any
    :keyword content: Pass in binary content you want in the body of the request (typically bytes,
     a byte iterator, or stream input). The name of the storage account within the specified
     resource group. Storage account names must be between 3 and 24 characters in length and use
     numbers and lower-case letters only.
    :paramtype content: Any
    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's
     `send_request` method. See https://aka.ms/azsdk/python/protocol/quickstart for how to
     incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest

    Example:
        .. code-block:: python

            # JSON input template you can fill out and use as your `json` input.
            json = {
                "name": "str",
                "type": "str (optional). Default value is \"Microsoft.Storage/storageAccounts\""
            }

            # response body for status code(s): 200
            response.json() == {
                "message": "str (optional)",
                "nameAvailable": "bool (optional)",
                "reason": "str (optional)"
            }
    """

    content_type = kwargs.pop("content_type", None)  # type: Optional[str]

    api_version = "2015-05-01-preview"
    accept = "application/json, text/json"

    # Construct URL
    url = kwargs.pop(
        "template_url", "/subscriptions/{subscriptionId}/providers/Microsoft.Storage/checkNameAvailability"
    )
    path_format_arguments = {
        "subscriptionId": _SERIALIZER.url("subscription_id", subscription_id, "str"),
    }
    url = _format_url_section(url, **path_format_arguments)

    # Construct parameters
    query_parameters = kwargs.pop("params", {})  # type: Dict[str, Any]
    query_parameters["api-version"] = _SERIALIZER.query("api_version", api_version, "str")

    # Construct headers
    header_parameters = kwargs.pop("headers", {})  # type: Dict[str, Any]
    if content_type is not None:
        header_parameters["Content-Type"] = _SERIALIZER.header("content_type", content_type, "str")
    header_parameters["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(
        method="POST", url=url, params=query_parameters, headers=header_parameters, json=json, content=content, **kwargs
    )


def build_create_request(
    resource_group_name: str,
    account_name: str,
    subscription_id: str,
    *,
    json: Any = None,
    content: Any = None,
    **kwargs: Any
) -> HttpRequest:
    """Asynchronously creates a new storage account with the specified parameters. Existing accounts
    cannot be updated with this API and should instead use the Update Storage Account API. If an
    account is already created and subsequent PUT request is issued with exact same set of
    properties, then HTTP 200 would be returned.

    See https://aka.ms/azsdk/python/llcwiki for how to incorporate this request builder into your
    code flow.

    :param resource_group_name: The name of the resource group within the user’s subscription.
    :type resource_group_name: str
    :param account_name: The name of the storage account within the specified resource group.
     Storage account names must be between 3 and 24 characters in length and use numbers and
     lower-case letters only.
    :type account_name: str
    :param subscription_id: Gets subscription credentials which uniquely identify Microsoft Azure
     subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :keyword json: Pass in a JSON-serializable object (usually a dictionary). See the template in
     our example to find the input shape. The parameters to provide for the created account.
    :paramtype json: Any
    :keyword content: Pass in binary content you want in the body of the request (typically bytes,
     a byte iterator, or stream input). The parameters to provide for the created account.
    :paramtype content: Any
    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's
     `send_request` method. See https://aka.ms/azsdk/python/protocol/quickstart for how to
     incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest

    Example:
        .. code-block:: python

            # JSON input template you can fill out and use as your `json` input.
            json = {
                "accountType": "str (optional)"
            }

            # response body for status code(s): 200
            response.json() == {
                "accountType": "str (optional)",
                "creationTime": "datetime (optional)",
                "customDomain": {
                    "name": "str (optional)",
                    "useSubDomain": "bool (optional)"
                },
                "lastGeoFailoverTime": "datetime (optional)",
                "primaryEndpoints": {
                    "FooPoint": {
                        "Bar.Point": {
                            "RecursivePoint": "..."
                        }
                    },
                    "blob": "str (optional)",
                    "dummyEndPoint": "...",
                    "queue": "str (optional)",
                    "table": "str (optional)"
                },
                "primaryLocation": "str (optional)",
                "provisioningState": "str (optional)",
                "secondaryEndpoints": "...",
                "secondaryLocation": "str (optional)",
                "statusOfPrimary": "str (optional)",
                "statusOfSecondary": "str (optional)"
            }
    """

    content_type = kwargs.pop("content_type", None)  # type: Optional[str]

    api_version = "2015-05-01-preview"
    accept = "application/json, text/json"

    # Construct URL
    url = kwargs.pop(
        "template_url",
        "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Storage/storageAccounts/{accountName}",
    )
    path_format_arguments = {
        "resourceGroupName": _SERIALIZER.url("resource_group_name", resource_group_name, "str"),
        "accountName": _SERIALIZER.url("account_name", account_name, "str"),
        "subscriptionId": _SERIALIZER.url("subscription_id", subscription_id, "str"),
    }
    url = _format_url_section(url, **path_format_arguments)

    # Construct parameters
    query_parameters = kwargs.pop("params", {})  # type: Dict[str, Any]
    query_parameters["api-version"] = _SERIALIZER.query("api_version", api_version, "str")

    # Construct headers
    header_parameters = kwargs.pop("headers", {})  # type: Dict[str, Any]
    if content_type is not None:
        header_parameters["Content-Type"] = _SERIALIZER.header("content_type", content_type, "str")
    header_parameters["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(
        method="PUT", url=url, params=query_parameters, headers=header_parameters, json=json, content=content, **kwargs
    )


def build_delete_request(
    resource_group_name: str, account_name: str, subscription_id: str, **kwargs: Any
) -> HttpRequest:
    """Deletes a storage account in Microsoft Azure.

    See https://aka.ms/azsdk/python/llcwiki for how to incorporate this request builder into your
    code flow.

    :param resource_group_name: The name of the resource group within the user’s subscription.
    :type resource_group_name: str
    :param account_name: The name of the storage account within the specified resource group.
     Storage account names must be between 3 and 24 characters in length and use numbers and
     lower-case letters only.
    :type account_name: str
    :param subscription_id: Gets subscription credentials which uniquely identify Microsoft Azure
     subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's
     `send_request` method. See https://aka.ms/azsdk/python/protocol/quickstart for how to
     incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest
    """

    api_version = "2015-05-01-preview"

    # Construct URL
    url = kwargs.pop(
        "template_url",
        "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Storage/storageAccounts/{accountName}",
    )
    path_format_arguments = {
        "resourceGroupName": _SERIALIZER.url("resource_group_name", resource_group_name, "str"),
        "accountName": _SERIALIZER.url("account_name", account_name, "str"),
        "subscriptionId": _SERIALIZER.url("subscription_id", subscription_id, "str"),
    }
    url = _format_url_section(url, **path_format_arguments)

    # Construct parameters
    query_parameters = kwargs.pop("params", {})  # type: Dict[str, Any]
    query_parameters["api-version"] = _SERIALIZER.query("api_version", api_version, "str")

    return HttpRequest(method="DELETE", url=url, params=query_parameters, **kwargs)


def build_get_properties_request(
    resource_group_name: str, account_name: str, subscription_id: str, **kwargs: Any
) -> HttpRequest:
    """Returns the properties for the specified storage account including but not limited to name,
    account type, location, and account status. The ListKeys operation should be used to retrieve
    storage keys.

    See https://aka.ms/azsdk/python/llcwiki for how to incorporate this request builder into your
    code flow.

    :param resource_group_name: The name of the resource group within the user’s subscription.
    :type resource_group_name: str
    :param account_name: The name of the storage account within the specified resource group.
     Storage account names must be between 3 and 24 characters in length and use numbers and
     lower-case letters only.
    :type account_name: str
    :param subscription_id: Gets subscription credentials which uniquely identify Microsoft Azure
     subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's
     `send_request` method. See https://aka.ms/azsdk/python/protocol/quickstart for how to
     incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest

    Example:
        .. code-block:: python

            # response body for status code(s): 200
            response.json() == {
                "accountType": "str (optional)",
                "creationTime": "datetime (optional)",
                "customDomain": {
                    "name": "str (optional)",
                    "useSubDomain": "bool (optional)"
                },
                "lastGeoFailoverTime": "datetime (optional)",
                "primaryEndpoints": {
                    "FooPoint": {
                        "Bar.Point": {
                            "RecursivePoint": "..."
                        }
                    },
                    "blob": "str (optional)",
                    "dummyEndPoint": "...",
                    "queue": "str (optional)",
                    "table": "str (optional)"
                },
                "primaryLocation": "str (optional)",
                "provisioningState": "str (optional)",
                "secondaryEndpoints": "...",
                "secondaryLocation": "str (optional)",
                "statusOfPrimary": "str (optional)",
                "statusOfSecondary": "str (optional)"
            }
    """

    api_version = "2015-05-01-preview"
    accept = "application/json, text/json"

    # Construct URL
    url = kwargs.pop(
        "template_url",
        "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Storage/storageAccounts/{accountName}",
    )
    path_format_arguments = {
        "resourceGroupName": _SERIALIZER.url("resource_group_name", resource_group_name, "str"),
        "accountName": _SERIALIZER.url("account_name", account_name, "str"),
        "subscriptionId": _SERIALIZER.url("subscription_id", subscription_id, "str"),
    }
    url = _format_url_section(url, **path_format_arguments)

    # Construct parameters
    query_parameters = kwargs.pop("params", {})  # type: Dict[str, Any]
    query_parameters["api-version"] = _SERIALIZER.query("api_version", api_version, "str")

    # Construct headers
    header_parameters = kwargs.pop("headers", {})  # type: Dict[str, Any]
    header_parameters["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="GET", url=url, params=query_parameters, headers=header_parameters, **kwargs)


def build_update_request(
    resource_group_name: str,
    account_name: str,
    subscription_id: str,
    *,
    json: Any = None,
    content: Any = None,
    **kwargs: Any
) -> HttpRequest:
    """Updates the account type or tags for a storage account. It can also be used to add a custom
    domain (note that custom domains cannot be added via the Create operation). Only one custom
    domain is supported per storage account. This API can only be used to update one of tags,
    accountType, or customDomain per call. To update multiple of these properties, call the API
    multiple times with one change per call. This call does not change the storage keys for the
    account. If you want to change storage account keys, use the RegenerateKey operation. The
    location and name of the storage account cannot be changed after creation.

    See https://aka.ms/azsdk/python/llcwiki for how to incorporate this request builder into your
    code flow.

    :param resource_group_name: The name of the resource group within the user’s subscription.
    :type resource_group_name: str
    :param account_name: The name of the storage account within the specified resource group.
     Storage account names must be between 3 and 24 characters in length and use numbers and
     lower-case letters only.
    :type account_name: str
    :param subscription_id: Gets subscription credentials which uniquely identify Microsoft Azure
     subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :keyword json: Pass in a JSON-serializable object (usually a dictionary). See the template in
     our example to find the input shape. The parameters to update on the account. Note that only
     one property can be changed at a time using this API.
    :paramtype json: Any
    :keyword content: Pass in binary content you want in the body of the request (typically bytes,
     a byte iterator, or stream input). The parameters to update on the account. Note that only one
     property can be changed at a time using this API.
    :paramtype content: Any
    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's
     `send_request` method. See https://aka.ms/azsdk/python/protocol/quickstart for how to
     incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest

    Example:
        .. code-block:: python

            # JSON input template you can fill out and use as your `json` input.
            json = {
                "accountType": "str (optional)",
                "customDomain": {
                    "name": "str (optional)",
                    "useSubDomain": "bool (optional)"
                }
            }

            # response body for status code(s): 200
            response.json() == {
                "accountType": "str (optional)",
                "creationTime": "datetime (optional)",
                "customDomain": {
                    "name": "str (optional)",
                    "useSubDomain": "bool (optional)"
                },
                "lastGeoFailoverTime": "datetime (optional)",
                "primaryEndpoints": {
                    "FooPoint": {
                        "Bar.Point": {
                            "RecursivePoint": "..."
                        }
                    },
                    "blob": "str (optional)",
                    "dummyEndPoint": "...",
                    "queue": "str (optional)",
                    "table": "str (optional)"
                },
                "primaryLocation": "str (optional)",
                "provisioningState": "str (optional)",
                "secondaryEndpoints": "...",
                "secondaryLocation": "str (optional)",
                "statusOfPrimary": "str (optional)",
                "statusOfSecondary": "str (optional)"
            }
    """

    content_type = kwargs.pop("content_type", None)  # type: Optional[str]

    api_version = "2015-05-01-preview"
    accept = "application/json, text/json"

    # Construct URL
    url = kwargs.pop(
        "template_url",
        "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Storage/storageAccounts/{accountName}",
    )
    path_format_arguments = {
        "resourceGroupName": _SERIALIZER.url("resource_group_name", resource_group_name, "str"),
        "accountName": _SERIALIZER.url("account_name", account_name, "str"),
        "subscriptionId": _SERIALIZER.url("subscription_id", subscription_id, "str"),
    }
    url = _format_url_section(url, **path_format_arguments)

    # Construct parameters
    query_parameters = kwargs.pop("params", {})  # type: Dict[str, Any]
    query_parameters["api-version"] = _SERIALIZER.query("api_version", api_version, "str")

    # Construct headers
    header_parameters = kwargs.pop("headers", {})  # type: Dict[str, Any]
    if content_type is not None:
        header_parameters["Content-Type"] = _SERIALIZER.header("content_type", content_type, "str")
    header_parameters["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(
        method="PATCH",
        url=url,
        params=query_parameters,
        headers=header_parameters,
        json=json,
        content=content,
        **kwargs
    )


def build_list_keys_request(
    resource_group_name: str, account_name: str, subscription_id: str, **kwargs: Any
) -> HttpRequest:
    """Lists the access keys for the specified storage account.

    See https://aka.ms/azsdk/python/llcwiki for how to incorporate this request builder into your
    code flow.

    :param resource_group_name: The name of the resource group within the user’s subscription.
    :type resource_group_name: str
    :param account_name: The name of the storage account.
    :type account_name: str
    :param subscription_id: Gets subscription credentials which uniquely identify Microsoft Azure
     subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's
     `send_request` method. See https://aka.ms/azsdk/python/protocol/quickstart for how to
     incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest

    Example:
        .. code-block:: python

            # response body for status code(s): 200
            response.json() == {
                "key1": "str (optional)",
                "key2": "str (optional)"
            }
    """

    api_version = "2015-05-01-preview"
    accept = "application/json, text/json"

    # Construct URL
    url = kwargs.pop(
        "template_url",
        "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Storage/storageAccounts/{accountName}/listKeys",
    )
    path_format_arguments = {
        "resourceGroupName": _SERIALIZER.url("resource_group_name", resource_group_name, "str"),
        "accountName": _SERIALIZER.url("account_name", account_name, "str"),
        "subscriptionId": _SERIALIZER.url("subscription_id", subscription_id, "str"),
    }
    url = _format_url_section(url, **path_format_arguments)

    # Construct parameters
    query_parameters = kwargs.pop("params", {})  # type: Dict[str, Any]
    query_parameters["api-version"] = _SERIALIZER.query("api_version", api_version, "str")

    # Construct headers
    header_parameters = kwargs.pop("headers", {})  # type: Dict[str, Any]
    header_parameters["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="POST", url=url, params=query_parameters, headers=header_parameters, **kwargs)


def build_list_request(subscription_id: str, **kwargs: Any) -> HttpRequest:
    """Lists all the storage accounts available under the subscription. Note that storage keys are not
    returned; use the ListKeys operation for this.

    See https://aka.ms/azsdk/python/llcwiki for how to incorporate this request builder into your
    code flow.

    :param subscription_id: Gets subscription credentials which uniquely identify Microsoft Azure
     subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's
     `send_request` method. See https://aka.ms/azsdk/python/protocol/quickstart for how to
     incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest

    Example:
        .. code-block:: python

            # response body for status code(s): 200
            response.json() == {
                "nextLink": "str (optional)",
                "value": [
                    {
                        "accountType": "str (optional)",
                        "creationTime": "datetime (optional)",
                        "customDomain": {
                            "name": "str (optional)",
                            "useSubDomain": "bool (optional)"
                        },
                        "lastGeoFailoverTime": "datetime (optional)",
                        "primaryEndpoints": {
                            "FooPoint": {
                                "Bar.Point": {
                                    "RecursivePoint": "..."
                                }
                            },
                            "blob": "str (optional)",
                            "dummyEndPoint": "...",
                            "queue": "str (optional)",
                            "table": "str (optional)"
                        },
                        "primaryLocation": "str (optional)",
                        "provisioningState": "str (optional)",
                        "secondaryEndpoints": "...",
                        "secondaryLocation": "str (optional)",
                        "statusOfPrimary": "str (optional)",
                        "statusOfSecondary": "str (optional)"
                    }
                ]
            }
    """

    api_version = "2015-05-01-preview"
    accept = "application/json, text/json"

    # Construct URL
    url = kwargs.pop("template_url", "/subscriptions/{subscriptionId}/providers/Microsoft.Storage/storageAccounts")
    path_format_arguments = {
        "subscriptionId": _SERIALIZER.url("subscription_id", subscription_id, "str"),
    }
    url = _format_url_section(url, **path_format_arguments)

    # Construct parameters
    query_parameters = kwargs.pop("params", {})  # type: Dict[str, Any]
    query_parameters["api-version"] = _SERIALIZER.query("api_version", api_version, "str")

    # Construct headers
    header_parameters = kwargs.pop("headers", {})  # type: Dict[str, Any]
    header_parameters["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="GET", url=url, params=query_parameters, headers=header_parameters, **kwargs)


def build_list_by_resource_group_request(resource_group_name: str, subscription_id: str, **kwargs: Any) -> HttpRequest:
    """Lists all the storage accounts available under the given resource group. Note that storage keys
    are not returned; use the ListKeys operation for this.

    See https://aka.ms/azsdk/python/llcwiki for how to incorporate this request builder into your
    code flow.

    :param resource_group_name: The name of the resource group within the user’s subscription.
    :type resource_group_name: str
    :param subscription_id: Gets subscription credentials which uniquely identify Microsoft Azure
     subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's
     `send_request` method. See https://aka.ms/azsdk/python/protocol/quickstart for how to
     incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest

    Example:
        .. code-block:: python

            # response body for status code(s): 200
            response.json() == {
                "nextLink": "str (optional)",
                "value": [
                    {
                        "accountType": "str (optional)",
                        "creationTime": "datetime (optional)",
                        "customDomain": {
                            "name": "str (optional)",
                            "useSubDomain": "bool (optional)"
                        },
                        "lastGeoFailoverTime": "datetime (optional)",
                        "primaryEndpoints": {
                            "FooPoint": {
                                "Bar.Point": {
                                    "RecursivePoint": "..."
                                }
                            },
                            "blob": "str (optional)",
                            "dummyEndPoint": "...",
                            "queue": "str (optional)",
                            "table": "str (optional)"
                        },
                        "primaryLocation": "str (optional)",
                        "provisioningState": "str (optional)",
                        "secondaryEndpoints": "...",
                        "secondaryLocation": "str (optional)",
                        "statusOfPrimary": "str (optional)",
                        "statusOfSecondary": "str (optional)"
                    }
                ]
            }
    """

    api_version = "2015-05-01-preview"
    accept = "application/json, text/json"

    # Construct URL
    url = kwargs.pop(
        "template_url",
        "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Storage/storageAccounts",
    )
    path_format_arguments = {
        "resourceGroupName": _SERIALIZER.url("resource_group_name", resource_group_name, "str"),
        "subscriptionId": _SERIALIZER.url("subscription_id", subscription_id, "str"),
    }
    url = _format_url_section(url, **path_format_arguments)

    # Construct parameters
    query_parameters = kwargs.pop("params", {})  # type: Dict[str, Any]
    query_parameters["api-version"] = _SERIALIZER.query("api_version", api_version, "str")

    # Construct headers
    header_parameters = kwargs.pop("headers", {})  # type: Dict[str, Any]
    header_parameters["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="GET", url=url, params=query_parameters, headers=header_parameters, **kwargs)


def build_regenerate_key_request(
    resource_group_name: str,
    account_name: str,
    subscription_id: str,
    *,
    json: Any = None,
    content: Any = None,
    **kwargs: Any
) -> HttpRequest:
    """Regenerates the access keys for the specified storage account.

    See https://aka.ms/azsdk/python/llcwiki for how to incorporate this request builder into your
    code flow.

    :param resource_group_name: The name of the resource group within the user’s subscription.
    :type resource_group_name: str
    :param account_name: The name of the storage account within the specified resource group.
     Storage account names must be between 3 and 24 characters in length and use numbers and
     lower-case letters only.
    :type account_name: str
    :param subscription_id: Gets subscription credentials which uniquely identify Microsoft Azure
     subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :keyword json: Pass in a JSON-serializable object (usually a dictionary). See the template in
     our example to find the input shape. Specifies name of the key which should be regenerated.
    :paramtype json: Any
    :keyword content: Pass in binary content you want in the body of the request (typically bytes,
     a byte iterator, or stream input). Specifies name of the key which should be regenerated.
    :paramtype content: Any
    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's
     `send_request` method. See https://aka.ms/azsdk/python/protocol/quickstart for how to
     incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest

    Example:
        .. code-block:: python

            # JSON input template you can fill out and use as your `json` input.
            json = {
                "keyName": "str (optional)"
            }

            # response body for status code(s): 200
            response.json() == {
                "key1": "str (optional)",
                "key2": "str (optional)"
            }
    """

    content_type = kwargs.pop("content_type", None)  # type: Optional[str]

    api_version = "2015-05-01-preview"
    accept = "application/json, text/json"

    # Construct URL
    url = kwargs.pop(
        "template_url",
        "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Storage/storageAccounts/{accountName}/regenerateKey",
    )
    path_format_arguments = {
        "resourceGroupName": _SERIALIZER.url("resource_group_name", resource_group_name, "str"),
        "accountName": _SERIALIZER.url("account_name", account_name, "str"),
        "subscriptionId": _SERIALIZER.url("subscription_id", subscription_id, "str"),
    }
    url = _format_url_section(url, **path_format_arguments)

    # Construct parameters
    query_parameters = kwargs.pop("params", {})  # type: Dict[str, Any]
    query_parameters["api-version"] = _SERIALIZER.query("api_version", api_version, "str")

    # Construct headers
    header_parameters = kwargs.pop("headers", {})  # type: Dict[str, Any]
    if content_type is not None:
        header_parameters["Content-Type"] = _SERIALIZER.header("content_type", content_type, "str")
    header_parameters["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(
        method="POST", url=url, params=query_parameters, headers=header_parameters, json=json, content=content, **kwargs
    )
