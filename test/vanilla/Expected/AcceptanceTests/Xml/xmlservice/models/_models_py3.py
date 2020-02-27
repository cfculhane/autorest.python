# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

import datetime
from typing import Dict, List, Optional, Union

from azure.core.exceptions import HttpResponseError
import msrest.serialization


class AccessPolicy(msrest.serialization.Model):
    """An Access policy.

    All required parameters must be populated in order to send to Azure.

    :param start: Required. the date-time the policy is active.
    :type start: ~datetime.datetime
    :param expiry: Required. the date-time the policy expires.
    :type expiry: ~datetime.datetime
    :param permission: Required. the permissions for the acl policy.
    :type permission: str
    """

    _validation = {
        'start': {'required': True},
        'expiry': {'required': True},
        'permission': {'required': True},
    }

    _attribute_map = {
        'start': {'key': 'Start', 'type': 'iso-8601'},
        'expiry': {'key': 'Expiry', 'type': 'iso-8601'},
        'permission': {'key': 'Permission', 'type': 'str'},
    }

    def __init__(
        self,
        *,
        start: datetime.datetime,
        expiry: datetime.datetime,
        permission: str,
        **kwargs
    ):
        super(AccessPolicy, self).__init__(**kwargs)
        self.start = start
        self.expiry = expiry
        self.permission = permission


class AppleBarrel(msrest.serialization.Model):
    """A barrel of apples.

    :param good_apples:
    :type good_apples: list[str]
    :param bad_apples:
    :type bad_apples: list[str]
    """

    _attribute_map = {
        'good_apples': {'key': 'GoodApples', 'type': '[str]', 'xml': {'wrapped': True, 'itemsName': 'Apple'}},
        'bad_apples': {'key': 'BadApples', 'type': '[str]', 'xml': {'wrapped': True, 'itemsName': 'Apple'}},
    }

    def __init__(
        self,
        *,
        good_apples: Optional[List[str]] = None,
        bad_apples: Optional[List[str]] = None,
        **kwargs
    ):
        super(AppleBarrel, self).__init__(**kwargs)
        self.good_apples = good_apples
        self.bad_apples = bad_apples


class Banana(msrest.serialization.Model):
    """A banana.

    :param name:
    :type name: str
    :param flavor:
    :type flavor: str
    :param expiration: The time at which you should reconsider eating this banana.
    :type expiration: ~datetime.datetime
    """

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str', 'xml': {'name': 'name'}},
        'flavor': {'key': 'flavor', 'type': 'str', 'xml': {'name': 'flavor'}},
        'expiration': {'key': 'expiration', 'type': 'iso-8601', 'xml': {'name': 'expiration'}},
    }
    _xml_map = {
        'name': 'banana'
    }

    def __init__(
        self,
        *,
        name: Optional[str] = None,
        flavor: Optional[str] = None,
        expiration: Optional[datetime.datetime] = None,
        **kwargs
    ):
        super(Banana, self).__init__(**kwargs)
        self.name = name
        self.flavor = flavor
        self.expiration = expiration


class Blob(msrest.serialization.Model):
    """An Azure Storage blob.

    All required parameters must be populated in order to send to Azure.

    :param name: Required.
    :type name: str
    :param deleted: Required.
    :type deleted: bool
    :param snapshot: Required.
    :type snapshot: str
    :param properties: Required. Properties of a blob.
    :type properties: ~xmlservice.models.BlobProperties
    :param metadata: Dictionary of :code:`<string>`.
    :type metadata: dict[str, str]
    """

    _validation = {
        'name': {'required': True},
        'deleted': {'required': True},
        'snapshot': {'required': True},
        'properties': {'required': True},
    }

    _attribute_map = {
        'name': {'key': 'Name', 'type': 'str'},
        'deleted': {'key': 'Deleted', 'type': 'bool'},
        'snapshot': {'key': 'Snapshot', 'type': 'str'},
        'properties': {'key': 'Properties', 'type': 'BlobProperties'},
        'metadata': {'key': 'Metadata', 'type': '{str}'},
    }
    _xml_map = {
        'name': 'Blob'
    }

    def __init__(
        self,
        *,
        name: str,
        deleted: bool,
        snapshot: str,
        properties: "BlobProperties",
        metadata: Optional[Dict[str, str]] = None,
        **kwargs
    ):
        super(Blob, self).__init__(**kwargs)
        self.name = name
        self.deleted = deleted
        self.snapshot = snapshot
        self.properties = properties
        self.metadata = metadata


class BlobPrefix(msrest.serialization.Model):
    """BlobPrefix.

    All required parameters must be populated in order to send to Azure.

    :param name: Required.
    :type name: str
    """

    _validation = {
        'name': {'required': True},
    }

    _attribute_map = {
        'name': {'key': 'Name', 'type': 'str'},
    }

    def __init__(
        self,
        *,
        name: str,
        **kwargs
    ):
        super(BlobPrefix, self).__init__(**kwargs)
        self.name = name


class BlobProperties(msrest.serialization.Model):
    """Properties of a blob.

    All required parameters must be populated in order to send to Azure.

    :param last_modified: Required.
    :type last_modified: ~datetime.datetime
    :param etag: Required.
    :type etag: str
    :param content_length: Size in bytes.
    :type content_length: long
    :param content_type:
    :type content_type: str
    :param content_encoding:
    :type content_encoding: str
    :param content_language:
    :type content_language: str
    :param content_md5:
    :type content_md5: str
    :param content_disposition:
    :type content_disposition: str
    :param cache_control:
    :type cache_control: str
    :param blob_sequence_number:
    :type blob_sequence_number: int
    :param blob_type:  Possible values include: 'BlockBlob', 'PageBlob', 'AppendBlob'.
    :type blob_type: str or ~xmlservice.models.BlobType
    :param lease_status:  Possible values include: 'locked', 'unlocked'.
    :type lease_status: str or ~xmlservice.models.LeaseStatusType
    :param lease_state:  Possible values include: 'available', 'leased', 'expired', 'breaking',
     'broken'.
    :type lease_state: str or ~xmlservice.models.LeaseStateType
    :param lease_duration:  Possible values include: 'infinite', 'fixed'.
    :type lease_duration: str or ~xmlservice.models.LeaseDurationType
    :param copy_id:
    :type copy_id: str
    :param copy_status:  Possible values include: 'pending', 'success', 'aborted', 'failed'.
    :type copy_status: str or ~xmlservice.models.CopyStatusType
    :param copy_source:
    :type copy_source: str
    :param copy_progress:
    :type copy_progress: str
    :param copy_completion_time:
    :type copy_completion_time: ~datetime.datetime
    :param copy_status_description:
    :type copy_status_description: str
    :param server_encrypted:
    :type server_encrypted: bool
    :param incremental_copy:
    :type incremental_copy: bool
    :param destination_snapshot:
    :type destination_snapshot: str
    :param deleted_time:
    :type deleted_time: ~datetime.datetime
    :param remaining_retention_days:
    :type remaining_retention_days: int
    :param access_tier:  Possible values include: 'P4', 'P6', 'P10', 'P20', 'P30', 'P40', 'P50',
     'Hot', 'Cool', 'Archive'.
    :type access_tier: str or ~xmlservice.models.AccessTier
    :param access_tier_inferred:
    :type access_tier_inferred: bool
    :param archive_status:  Possible values include: 'rehydrate-pending-to-hot', 'rehydrate-
     pending-to-cool'.
    :type archive_status: str or ~xmlservice.models.ArchiveStatus
    """

    _validation = {
        'last_modified': {'required': True},
        'etag': {'required': True},
    }

    _attribute_map = {
        'last_modified': {'key': 'Last-Modified', 'type': 'rfc-1123'},
        'etag': {'key': 'Etag', 'type': 'str'},
        'content_length': {'key': 'Content-Length', 'type': 'long'},
        'content_type': {'key': 'Content-Type', 'type': 'str'},
        'content_encoding': {'key': 'Content-Encoding', 'type': 'str'},
        'content_language': {'key': 'Content-Language', 'type': 'str'},
        'content_md5': {'key': 'Content-MD5', 'type': 'str'},
        'content_disposition': {'key': 'Content-Disposition', 'type': 'str'},
        'cache_control': {'key': 'Cache-Control', 'type': 'str'},
        'blob_sequence_number': {'key': 'x-ms-blob-sequence-number', 'type': 'int'},
        'blob_type': {'key': 'BlobType', 'type': 'str'},
        'lease_status': {'key': 'LeaseStatus', 'type': 'str'},
        'lease_state': {'key': 'LeaseState', 'type': 'str'},
        'lease_duration': {'key': 'LeaseDuration', 'type': 'str'},
        'copy_id': {'key': 'CopyId', 'type': 'str'},
        'copy_status': {'key': 'CopyStatus', 'type': 'str'},
        'copy_source': {'key': 'CopySource', 'type': 'str'},
        'copy_progress': {'key': 'CopyProgress', 'type': 'str'},
        'copy_completion_time': {'key': 'CopyCompletionTime', 'type': 'rfc-1123'},
        'copy_status_description': {'key': 'CopyStatusDescription', 'type': 'str'},
        'server_encrypted': {'key': 'ServerEncrypted', 'type': 'bool'},
        'incremental_copy': {'key': 'IncrementalCopy', 'type': 'bool'},
        'destination_snapshot': {'key': 'DestinationSnapshot', 'type': 'str'},
        'deleted_time': {'key': 'DeletedTime', 'type': 'rfc-1123'},
        'remaining_retention_days': {'key': 'RemainingRetentionDays', 'type': 'int'},
        'access_tier': {'key': 'AccessTier', 'type': 'str'},
        'access_tier_inferred': {'key': 'AccessTierInferred', 'type': 'bool'},
        'archive_status': {'key': 'ArchiveStatus', 'type': 'str'},
    }

    def __init__(
        self,
        *,
        last_modified: datetime.datetime,
        etag: str,
        content_length: Optional[int] = None,
        content_type: Optional[str] = None,
        content_encoding: Optional[str] = None,
        content_language: Optional[str] = None,
        content_md5: Optional[str] = None,
        content_disposition: Optional[str] = None,
        cache_control: Optional[str] = None,
        blob_sequence_number: Optional[int] = None,
        blob_type: Optional[Union[str, "BlobType"]] = None,
        lease_status: Optional[Union[str, "LeaseStatusType"]] = None,
        lease_state: Optional[Union[str, "LeaseStateType"]] = None,
        lease_duration: Optional[Union[str, "LeaseDurationType"]] = None,
        copy_id: Optional[str] = None,
        copy_status: Optional[Union[str, "CopyStatusType"]] = None,
        copy_source: Optional[str] = None,
        copy_progress: Optional[str] = None,
        copy_completion_time: Optional[datetime.datetime] = None,
        copy_status_description: Optional[str] = None,
        server_encrypted: Optional[bool] = None,
        incremental_copy: Optional[bool] = None,
        destination_snapshot: Optional[str] = None,
        deleted_time: Optional[datetime.datetime] = None,
        remaining_retention_days: Optional[int] = None,
        access_tier: Optional[Union[str, "AccessTier"]] = None,
        access_tier_inferred: Optional[bool] = None,
        archive_status: Optional[Union[str, "ArchiveStatus"]] = None,
        **kwargs
    ):
        super(BlobProperties, self).__init__(**kwargs)
        self.last_modified = last_modified
        self.etag = etag
        self.content_length = content_length
        self.content_type = content_type
        self.content_encoding = content_encoding
        self.content_language = content_language
        self.content_md5 = content_md5
        self.content_disposition = content_disposition
        self.cache_control = cache_control
        self.blob_sequence_number = blob_sequence_number
        self.blob_type = blob_type
        self.lease_status = lease_status
        self.lease_state = lease_state
        self.lease_duration = lease_duration
        self.copy_id = copy_id
        self.copy_status = copy_status
        self.copy_source = copy_source
        self.copy_progress = copy_progress
        self.copy_completion_time = copy_completion_time
        self.copy_status_description = copy_status_description
        self.server_encrypted = server_encrypted
        self.incremental_copy = incremental_copy
        self.destination_snapshot = destination_snapshot
        self.deleted_time = deleted_time
        self.remaining_retention_days = remaining_retention_days
        self.access_tier = access_tier
        self.access_tier_inferred = access_tier_inferred
        self.archive_status = archive_status


class Blobs(msrest.serialization.Model):
    """Blobs.

    :param blob_prefix:
    :type blob_prefix: list[~xmlservice.models.BlobPrefix]
    :param blob:
    :type blob: list[~xmlservice.models.Blob]
    """

    _attribute_map = {
        'blob_prefix': {'key': 'BlobPrefix', 'type': '[BlobPrefix]'},
        'blob': {'key': 'Blob', 'type': '[Blob]'},
    }

    def __init__(
        self,
        *,
        blob_prefix: Optional[List["BlobPrefix"]] = None,
        blob: Optional[List["Blob"]] = None,
        **kwargs
    ):
        super(Blobs, self).__init__(**kwargs)
        self.blob_prefix = blob_prefix
        self.blob = blob


class ComplexTypeNoMeta(msrest.serialization.Model):
    """I am a complex type with no XML node.

    :param id: The id of the res.
    :type id: str
    """

    _attribute_map = {
        'id': {'key': 'ID', 'type': 'str'},
    }

    def __init__(
        self,
        *,
        id: Optional[str] = None,
        **kwargs
    ):
        super(ComplexTypeNoMeta, self).__init__(**kwargs)
        self.id = id


class ComplexTypeWithMeta(msrest.serialization.Model):
    """I am a complex type with XML node.

    :param id: The id of the res.
    :type id: str
    """

    _attribute_map = {
        'id': {'key': 'ID', 'type': 'str'},
    }
    _xml_map = {
        'name': 'XMLComplexTypeWithMeta'
    }

    def __init__(
        self,
        *,
        id: Optional[str] = None,
        **kwargs
    ):
        super(ComplexTypeWithMeta, self).__init__(**kwargs)
        self.id = id


class Container(msrest.serialization.Model):
    """An Azure Storage container.

    All required parameters must be populated in order to send to Azure.

    :param name: Required.
    :type name: str
    :param properties: Required. Properties of a container.
    :type properties: ~xmlservice.models.ContainerProperties
    :param metadata: Dictionary of :code:`<string>`.
    :type metadata: dict[str, str]
    """

    _validation = {
        'name': {'required': True},
        'properties': {'required': True},
    }

    _attribute_map = {
        'name': {'key': 'Name', 'type': 'str'},
        'properties': {'key': 'Properties', 'type': 'ContainerProperties'},
        'metadata': {'key': 'Metadata', 'type': '{str}'},
    }

    def __init__(
        self,
        *,
        name: str,
        properties: "ContainerProperties",
        metadata: Optional[Dict[str, str]] = None,
        **kwargs
    ):
        super(Container, self).__init__(**kwargs)
        self.name = name
        self.properties = properties
        self.metadata = metadata


class ContainerProperties(msrest.serialization.Model):
    """Properties of a container.

    All required parameters must be populated in order to send to Azure.

    :param last_modified: Required.
    :type last_modified: ~datetime.datetime
    :param etag: Required.
    :type etag: str
    :param lease_status:  Possible values include: 'locked', 'unlocked'.
    :type lease_status: str or ~xmlservice.models.LeaseStatusType
    :param lease_state:  Possible values include: 'available', 'leased', 'expired', 'breaking',
     'broken'.
    :type lease_state: str or ~xmlservice.models.LeaseStateType
    :param lease_duration:  Possible values include: 'infinite', 'fixed'.
    :type lease_duration: str or ~xmlservice.models.LeaseDurationType
    :param public_access:  Possible values include: 'container', 'blob'.
    :type public_access: str or ~xmlservice.models.PublicAccessType
    """

    _validation = {
        'last_modified': {'required': True},
        'etag': {'required': True},
    }

    _attribute_map = {
        'last_modified': {'key': 'Last-Modified', 'type': 'rfc-1123'},
        'etag': {'key': 'Etag', 'type': 'str'},
        'lease_status': {'key': 'LeaseStatus', 'type': 'str'},
        'lease_state': {'key': 'LeaseState', 'type': 'str'},
        'lease_duration': {'key': 'LeaseDuration', 'type': 'str'},
        'public_access': {'key': 'PublicAccess', 'type': 'str'},
    }

    def __init__(
        self,
        *,
        last_modified: datetime.datetime,
        etag: str,
        lease_status: Optional[Union[str, "LeaseStatusType"]] = None,
        lease_state: Optional[Union[str, "LeaseStateType"]] = None,
        lease_duration: Optional[Union[str, "LeaseDurationType"]] = None,
        public_access: Optional[Union[str, "PublicAccessType"]] = None,
        **kwargs
    ):
        super(ContainerProperties, self).__init__(**kwargs)
        self.last_modified = last_modified
        self.etag = etag
        self.lease_status = lease_status
        self.lease_state = lease_state
        self.lease_duration = lease_duration
        self.public_access = public_access


class CorsRule(msrest.serialization.Model):
    """CORS is an HTTP feature that enables a web application running under one domain to access resources in another domain. Web browsers implement a security restriction known as same-origin policy that prevents a web page from calling APIs in a different domain; CORS provides a secure way to allow one domain (the origin domain) to call APIs in another domain.

    All required parameters must be populated in order to send to Azure.

    :param allowed_origins: Required. The origin domains that are permitted to make a request
     against the storage service via CORS. The origin domain is the domain from which the request
     originates. Note that the origin must be an exact case-sensitive match with the origin that the
     user age sends to the service. You can also use the wildcard character '*' to allow all origin
     domains to make requests via CORS.
    :type allowed_origins: str
    :param allowed_methods: Required. The methods (HTTP request verbs) that the origin domain may
     use for a CORS request. (comma separated).
    :type allowed_methods: str
    :param allowed_headers: Required. the request headers that the origin domain may specify on the
     CORS request.
    :type allowed_headers: str
    :param exposed_headers: Required. The response headers that may be sent in the response to the
     CORS request and exposed by the browser to the request issuer.
    :type exposed_headers: str
    :param max_age_in_seconds: Required. The maximum amount time that a browser should cache the
     preflight OPTIONS request.
    :type max_age_in_seconds: int
    """

    _validation = {
        'allowed_origins': {'required': True},
        'allowed_methods': {'required': True},
        'allowed_headers': {'required': True},
        'exposed_headers': {'required': True},
        'max_age_in_seconds': {'required': True, 'minimum': 0},
    }

    _attribute_map = {
        'allowed_origins': {'key': 'AllowedOrigins', 'type': 'str'},
        'allowed_methods': {'key': 'AllowedMethods', 'type': 'str'},
        'allowed_headers': {'key': 'AllowedHeaders', 'type': 'str'},
        'exposed_headers': {'key': 'ExposedHeaders', 'type': 'str'},
        'max_age_in_seconds': {'key': 'MaxAgeInSeconds', 'type': 'int'},
    }
    _xml_map = {
        'name': 'CorsRule'
    }

    def __init__(
        self,
        *,
        allowed_origins: str,
        allowed_methods: str,
        allowed_headers: str,
        exposed_headers: str,
        max_age_in_seconds: int,
        **kwargs
    ):
        super(CorsRule, self).__init__(**kwargs)
        self.allowed_origins = allowed_origins
        self.allowed_methods = allowed_methods
        self.allowed_headers = allowed_headers
        self.exposed_headers = exposed_headers
        self.max_age_in_seconds = max_age_in_seconds


class ErrorException(HttpResponseError):
    """Server responded with exception of type: 'Error'.

    :param response: Server response to be deserialized.
    :param error_model: A deserialized model of the response body as model.
    """

    def __init__(self, response, error_model):
        self.error = error_model
        super(ErrorException, self).__init__(response=response, error_model=error_model)

    @classmethod
    def from_response(cls, response, deserialize):
        """Deserialize this response as this exception, or a subclass of this exception.

        :param response: Server response to be deserialized.
        :param deserialize: A deserializer
        """
        model_name = 'Error'
        error = deserialize(model_name, response)
        if error is None:
            error = deserialize.dependencies[model_name]()
        return error._EXCEPTION_TYPE(response, error)


class Error(msrest.serialization.Model):
    """Error.

    :param status:
    :type status: int
    :param message:
    :type message: str
    """
    _EXCEPTION_TYPE = ErrorException

    _attribute_map = {
        'status': {'key': 'status', 'type': 'int'},
        'message': {'key': 'message', 'type': 'str'},
    }

    def __init__(
        self,
        *,
        status: Optional[int] = None,
        message: Optional[str] = None,
        **kwargs
    ):
        super(Error, self).__init__(**kwargs)
        self.status = status
        self.message = message


class JSONInput(msrest.serialization.Model):
    """JSONInput.

    :param id:
    :type id: int
    """

    _attribute_map = {
        'id': {'key': 'id', 'type': 'int'},
    }

    def __init__(
        self,
        *,
        id: Optional[int] = None,
        **kwargs
    ):
        super(JSONInput, self).__init__(**kwargs)
        self.id = id


class JSONOutput(msrest.serialization.Model):
    """JSONOutput.

    :param id:
    :type id: int
    """

    _attribute_map = {
        'id': {'key': 'id', 'type': 'int'},
    }

    def __init__(
        self,
        *,
        id: Optional[int] = None,
        **kwargs
    ):
        super(JSONOutput, self).__init__(**kwargs)
        self.id = id


class ListBlobsResponse(msrest.serialization.Model):
    """An enumeration of blobs.

    All required parameters must be populated in order to send to Azure.

    :param service_endpoint: Required.
    :type service_endpoint: str
    :param container_name: Required.
    :type container_name: str
    :param prefix: Required.
    :type prefix: str
    :param marker: Required.
    :type marker: str
    :param max_results: Required.
    :type max_results: int
    :param delimiter: Required.
    :type delimiter: str
    :param blobs: Required.
    :type blobs: ~xmlservice.models.Blobs
    :param next_marker: Required.
    :type next_marker: str
    """

    _validation = {
        'service_endpoint': {'required': True},
        'container_name': {'required': True},
        'prefix': {'required': True},
        'marker': {'required': True},
        'max_results': {'required': True},
        'delimiter': {'required': True},
        'blobs': {'required': True},
        'next_marker': {'required': True},
    }

    _attribute_map = {
        'service_endpoint': {'key': 'ServiceEndpoint', 'type': 'str', 'xml': {'attr': True}},
        'container_name': {'key': 'ContainerName', 'type': 'str', 'xml': {'attr': True}},
        'prefix': {'key': 'Prefix', 'type': 'str'},
        'marker': {'key': 'Marker', 'type': 'str'},
        'max_results': {'key': 'MaxResults', 'type': 'int'},
        'delimiter': {'key': 'Delimiter', 'type': 'str'},
        'blobs': {'key': 'Blobs', 'type': 'Blobs'},
        'next_marker': {'key': 'NextMarker', 'type': 'str'},
    }
    _xml_map = {
        'name': 'EnumerationResults'
    }

    def __init__(
        self,
        *,
        service_endpoint: str,
        container_name: str,
        prefix: str,
        marker: str,
        max_results: int,
        delimiter: str,
        blobs: "Blobs",
        next_marker: str,
        **kwargs
    ):
        super(ListBlobsResponse, self).__init__(**kwargs)
        self.service_endpoint = service_endpoint
        self.container_name = container_name
        self.prefix = prefix
        self.marker = marker
        self.max_results = max_results
        self.delimiter = delimiter
        self.blobs = blobs
        self.next_marker = next_marker


class ListContainersResponse(msrest.serialization.Model):
    """An enumeration of containers.

    All required parameters must be populated in order to send to Azure.

    :param service_endpoint: Required.
    :type service_endpoint: str
    :param prefix: Required.
    :type prefix: str
    :param marker:
    :type marker: str
    :param max_results: Required.
    :type max_results: int
    :param containers:
    :type containers: list[~xmlservice.models.Container]
    :param next_marker: Required.
    :type next_marker: str
    """

    _validation = {
        'service_endpoint': {'required': True},
        'prefix': {'required': True},
        'max_results': {'required': True},
        'next_marker': {'required': True},
    }

    _attribute_map = {
        'service_endpoint': {'key': 'ServiceEndpoint', 'type': 'str', 'xml': {'attr': True}},
        'prefix': {'key': 'Prefix', 'type': 'str'},
        'marker': {'key': 'Marker', 'type': 'str'},
        'max_results': {'key': 'MaxResults', 'type': 'int'},
        'containers': {'key': 'Containers', 'type': '[Container]', 'xml': {'wrapped': True}},
        'next_marker': {'key': 'NextMarker', 'type': 'str'},
    }
    _xml_map = {
        'name': 'EnumerationResults'
    }

    def __init__(
        self,
        *,
        service_endpoint: str,
        prefix: str,
        max_results: int,
        next_marker: str,
        marker: Optional[str] = None,
        containers: Optional[List["Container"]] = None,
        **kwargs
    ):
        super(ListContainersResponse, self).__init__(**kwargs)
        self.service_endpoint = service_endpoint
        self.prefix = prefix
        self.marker = marker
        self.max_results = max_results
        self.containers = containers
        self.next_marker = next_marker


class Logging(msrest.serialization.Model):
    """Azure Analytics Logging settings.

    All required parameters must be populated in order to send to Azure.

    :param version: Required. The version of Storage Analytics to configure.
    :type version: str
    :param delete: Required. Indicates whether all delete requests should be logged.
    :type delete: bool
    :param read: Required. Indicates whether all read requests should be logged.
    :type read: bool
    :param write: Required. Indicates whether all write requests should be logged.
    :type write: bool
    :param retention_policy: Required. the retention policy.
    :type retention_policy: ~xmlservice.models.RetentionPolicy
    """

    _validation = {
        'version': {'required': True},
        'delete': {'required': True},
        'read': {'required': True},
        'write': {'required': True},
        'retention_policy': {'required': True},
    }

    _attribute_map = {
        'version': {'key': 'Version', 'type': 'str'},
        'delete': {'key': 'Delete', 'type': 'bool'},
        'read': {'key': 'Read', 'type': 'bool'},
        'write': {'key': 'Write', 'type': 'bool'},
        'retention_policy': {'key': 'RetentionPolicy', 'type': 'RetentionPolicy'},
    }

    def __init__(
        self,
        *,
        version: str,
        delete: bool,
        read: bool,
        write: bool,
        retention_policy: "RetentionPolicy",
        **kwargs
    ):
        super(Logging, self).__init__(**kwargs)
        self.version = version
        self.delete = delete
        self.read = read
        self.write = write
        self.retention_policy = retention_policy


class Metrics(msrest.serialization.Model):
    """Metrics.

    All required parameters must be populated in order to send to Azure.

    :param version: The version of Storage Analytics to configure.
    :type version: str
    :param enabled: Required. Indicates whether metrics are enabled for the Blob service.
    :type enabled: bool
    :param include_ap_is: Indicates whether metrics should generate summary statistics for called
     API operations.
    :type include_ap_is: bool
    :param retention_policy: the retention policy.
    :type retention_policy: ~xmlservice.models.RetentionPolicy
    """

    _validation = {
        'enabled': {'required': True},
    }

    _attribute_map = {
        'version': {'key': 'Version', 'type': 'str'},
        'enabled': {'key': 'Enabled', 'type': 'bool'},
        'include_ap_is': {'key': 'IncludeAPIs', 'type': 'bool'},
        'retention_policy': {'key': 'RetentionPolicy', 'type': 'RetentionPolicy'},
    }

    def __init__(
        self,
        *,
        enabled: bool,
        version: Optional[str] = None,
        include_ap_is: Optional[bool] = None,
        retention_policy: Optional["RetentionPolicy"] = None,
        **kwargs
    ):
        super(Metrics, self).__init__(**kwargs)
        self.version = version
        self.enabled = enabled
        self.include_ap_is = include_ap_is
        self.retention_policy = retention_policy


class RetentionPolicy(msrest.serialization.Model):
    """the retention policy.

    All required parameters must be populated in order to send to Azure.

    :param enabled: Required. Indicates whether a retention policy is enabled for the storage
     service.
    :type enabled: bool
    :param days: Indicates the number of days that metrics or logging or soft-deleted data should
     be retained. All data older than this value will be deleted.
    :type days: int
    """

    _validation = {
        'enabled': {'required': True},
        'days': {'minimum': 1},
    }

    _attribute_map = {
        'enabled': {'key': 'Enabled', 'type': 'bool'},
        'days': {'key': 'Days', 'type': 'int'},
    }

    def __init__(
        self,
        *,
        enabled: bool,
        days: Optional[int] = None,
        **kwargs
    ):
        super(RetentionPolicy, self).__init__(**kwargs)
        self.enabled = enabled
        self.days = days


class RootWithRefAndMeta(msrest.serialization.Model):
    """I am root, and I ref a model WITH meta.

    :param ref_to_model: XML will use XMLComplexTypeWithMeta.
    :type ref_to_model: ~xmlservice.models.ComplexTypeWithMeta
    :param something: Something else (just to avoid flattening).
    :type something: str
    """

    _attribute_map = {
        'ref_to_model': {'key': 'RefToModel', 'type': 'ComplexTypeWithMeta'},
        'something': {'key': 'Something', 'type': 'str'},
    }

    def __init__(
        self,
        *,
        ref_to_model: Optional["ComplexTypeWithMeta"] = None,
        something: Optional[str] = None,
        **kwargs
    ):
        super(RootWithRefAndMeta, self).__init__(**kwargs)
        self.ref_to_model = ref_to_model
        self.something = something


class RootWithRefAndNoMeta(msrest.serialization.Model):
    """I am root, and I ref a model with no meta.

    :param ref_to_model: XML will use RefToModel.
    :type ref_to_model: ~xmlservice.models.ComplexTypeNoMeta
    :param something: Something else (just to avoid flattening).
    :type something: str
    """

    _attribute_map = {
        'ref_to_model': {'key': 'RefToModel', 'type': 'ComplexTypeNoMeta'},
        'something': {'key': 'Something', 'type': 'str'},
    }

    def __init__(
        self,
        *,
        ref_to_model: Optional["ComplexTypeNoMeta"] = None,
        something: Optional[str] = None,
        **kwargs
    ):
        super(RootWithRefAndNoMeta, self).__init__(**kwargs)
        self.ref_to_model = ref_to_model
        self.something = something


class SignedIdentifier(msrest.serialization.Model):
    """signed identifier.

    All required parameters must be populated in order to send to Azure.

    :param id: Required. a unique id.
    :type id: str
    :param access_policy: Required. The access policy.
    :type access_policy: ~xmlservice.models.AccessPolicy
    """

    _validation = {
        'id': {'required': True},
        'access_policy': {'required': True},
    }

    _attribute_map = {
        'id': {'key': 'Id', 'type': 'str'},
        'access_policy': {'key': 'AccessPolicy', 'type': 'AccessPolicy'},
    }
    _xml_map = {
        'name': 'SignedIdentifier'
    }

    def __init__(
        self,
        *,
        id: str,
        access_policy: "AccessPolicy",
        **kwargs
    ):
        super(SignedIdentifier, self).__init__(**kwargs)
        self.id = id
        self.access_policy = access_policy


class Slide(msrest.serialization.Model):
    """A slide in a slideshow.

    :param type:
    :type type: str
    :param title:
    :type title: str
    :param items:
    :type items: list[str]
    """

    _attribute_map = {
        'type': {'key': 'type', 'type': 'str', 'xml': {'attr': True}},
        'title': {'key': 'title', 'type': 'str'},
        'items': {'key': 'items', 'type': '[str]', 'xml': {'itemsName': 'item'}},
    }
    _xml_map = {
        'name': 'slide'
    }

    def __init__(
        self,
        *,
        type: Optional[str] = None,
        title: Optional[str] = None,
        items: Optional[List[str]] = None,
        **kwargs
    ):
        super(Slide, self).__init__(**kwargs)
        self.type = type
        self.title = title
        self.items = items


class Slideshow(msrest.serialization.Model):
    """Data about a slideshow.

    :param title:
    :type title: str
    :param date:
    :type date: str
    :param author:
    :type author: str
    :param slides:
    :type slides: list[~xmlservice.models.Slide]
    """

    _attribute_map = {
        'title': {'key': 'title', 'type': 'str', 'xml': {'attr': True}},
        'date': {'key': 'date', 'type': 'str', 'xml': {'attr': True}},
        'author': {'key': 'author', 'type': 'str', 'xml': {'attr': True}},
        'slides': {'key': 'slides', 'type': '[Slide]'},
    }
    _xml_map = {
        'name': 'slideshow'
    }

    def __init__(
        self,
        *,
        title: Optional[str] = None,
        date: Optional[str] = None,
        author: Optional[str] = None,
        slides: Optional[List["Slide"]] = None,
        **kwargs
    ):
        super(Slideshow, self).__init__(**kwargs)
        self.title = title
        self.date = date
        self.author = author
        self.slides = slides


class StorageServiceProperties(msrest.serialization.Model):
    """Storage Service Properties.

    :param logging: Azure Analytics Logging settings.
    :type logging: ~xmlservice.models.Logging
    :param hour_metrics: A summary of request statistics grouped by API in hourly aggregates for
     blobs.
    :type hour_metrics: ~xmlservice.models.Metrics
    :param minute_metrics: a summary of request statistics grouped by API in minute aggregates for
     blobs.
    :type minute_metrics: ~xmlservice.models.Metrics
    :param cors: The set of CORS rules.
    :type cors: list[~xmlservice.models.CorsRule]
    :param default_service_version: The default version to use for requests to the Blob service if
     an incoming request's version is not specified. Possible values include version 2008-10-27 and
     all more recent versions.
    :type default_service_version: str
    :param delete_retention_policy: The Delete Retention Policy for the service.
    :type delete_retention_policy: ~xmlservice.models.RetentionPolicy
    """

    _attribute_map = {
        'logging': {'key': 'Logging', 'type': 'Logging'},
        'hour_metrics': {'key': 'HourMetrics', 'type': 'Metrics'},
        'minute_metrics': {'key': 'MinuteMetrics', 'type': 'Metrics'},
        'cors': {'key': 'Cors', 'type': '[CorsRule]', 'xml': {'wrapped': True, 'itemsName': 'CorsRule'}},
        'default_service_version': {'key': 'DefaultServiceVersion', 'type': 'str'},
        'delete_retention_policy': {'key': 'DeleteRetentionPolicy', 'type': 'RetentionPolicy'},
    }

    def __init__(
        self,
        *,
        logging: Optional["Logging"] = None,
        hour_metrics: Optional["Metrics"] = None,
        minute_metrics: Optional["Metrics"] = None,
        cors: Optional[List["CorsRule"]] = None,
        default_service_version: Optional[str] = None,
        delete_retention_policy: Optional["RetentionPolicy"] = None,
        **kwargs
    ):
        super(StorageServiceProperties, self).__init__(**kwargs)
        self.logging = logging
        self.hour_metrics = hour_metrics
        self.minute_metrics = minute_metrics
        self.cors = cors
        self.default_service_version = default_service_version
        self.delete_retention_policy = delete_retention_policy
