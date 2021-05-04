# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from typing import Dict, List, Optional

from azure.core.exceptions import HttpResponseError
import msrest.serialization


class Boundary(msrest.serialization.Model):
    """Schema of boundary resource.

    Variables are only populated by the server, and will be ignored when sending a request.

    :ivar farmer_id: Farmer Id.
    :vartype farmer_id: str
    :param parent_id: Id of the parent(field or seasonalField) it belongs to.
    :type parent_id: str
    :param geometry: GeoJSON abstract class.
    :type geometry: ~bodycomplex.models.GeoJsonObject
    :param is_primary: Is the boundary primary.
    :type is_primary: bool
    :ivar acreage: Boundary area in acres.
    :vartype acreage: float
    :ivar parent_type: Type of the parent it belongs to.
    :vartype parent_type: str
    :ivar id: Unique resource ID.
    :vartype id: str
    :ivar e_tag: The ETag value to implement optimistic concurrency.
    :vartype e_tag: str
    :param status: Status of the resource.
    :type status: str
    :ivar created_date_time: Date-time when resource was created, sample format:
     yyyy-MM-ddTHH:mm:ssZ.
    :vartype created_date_time: ~datetime.datetime
    :ivar modified_date_time: Date-time when resource was last modified, sample format:
     yyyy-MM-ddTHH:mm:ssZ.
    :vartype modified_date_time: ~datetime.datetime
    :param name: Name to identify resource.
    :type name: str
    :param description: Textual description of the resource.
    :type description: str
    :param properties: A collection of key value pairs that belongs to the resource.
     Each pair must not have a key greater than 50 characters
     and must not have a value greater than 150 characters.
     Note: A maximum of 25 key value pairs can be provided for a resource and only string and
     numeral values are supported.
    :type properties: dict[str, object]
    """

    _validation = {
        "farmer_id": {"readonly": True},
        "acreage": {"readonly": True},
        "parent_type": {"readonly": True},
        "id": {"readonly": True},
        "e_tag": {"readonly": True},
        "status": {"max_length": 100, "min_length": 0},
        "created_date_time": {"readonly": True},
        "modified_date_time": {"readonly": True},
        "name": {"max_length": 100, "min_length": 0},
        "description": {"max_length": 500, "min_length": 0},
    }

    _attribute_map = {
        "farmer_id": {"key": "farmerId", "type": "str"},
        "parent_id": {"key": "parentId", "type": "str"},
        "geometry": {"key": "geometry", "type": "GeoJsonObject"},
        "is_primary": {"key": "isPrimary", "type": "bool"},
        "acreage": {"key": "acreage", "type": "float"},
        "parent_type": {"key": "parentType", "type": "str"},
        "id": {"key": "id", "type": "str"},
        "e_tag": {"key": "eTag", "type": "str"},
        "status": {"key": "status", "type": "str"},
        "created_date_time": {"key": "createdDateTime", "type": "iso-8601"},
        "modified_date_time": {"key": "modifiedDateTime", "type": "iso-8601"},
        "name": {"key": "name", "type": "str"},
        "description": {"key": "description", "type": "str"},
        "properties": {"key": "properties", "type": "{object}"},
    }

    def __init__(
        self,
        *,
        parent_id: Optional[str] = None,
        geometry: Optional["GeoJsonObject"] = None,
        is_primary: Optional[bool] = None,
        status: Optional[str] = None,
        name: Optional[str] = None,
        description: Optional[str] = None,
        properties: Optional[Dict[str, object]] = None,
        **kwargs
    ):
        super(Boundary, self).__init__(**kwargs)
        self.farmer_id = None
        self.parent_id = parent_id
        self.geometry = geometry
        self.is_primary = is_primary
        self.acreage = None
        self.parent_type = None
        self.id = None
        self.e_tag = None
        self.status = status
        self.created_date_time = None
        self.modified_date_time = None
        self.name = name
        self.description = description
        self.properties = properties


class Error(msrest.serialization.Model):
    """Error.

    :param status:
    :type status: int
    :param message:
    :type message: str
    """

    _attribute_map = {
        "status": {"key": "status", "type": "int"},
        "message": {"key": "message", "type": "str"},
    }

    def __init__(self, *, status: Optional[int] = None, message: Optional[str] = None, **kwargs):
        super(Error, self).__init__(**kwargs)
        self.status = status
        self.message = message


class GeoJsonObject(msrest.serialization.Model):
    """GeoJSON abstract class.

    You probably want to use the sub-classes and not this class directly. Known
    sub-classes are: MultiPolygon, Point, Polygon.

    All required parameters must be populated in order to send to Azure.

    :param type: Required. GeoJSON object type.Constant filled by server.  Possible values include:
     "Point", "Polygon", "MultiPolygon".
    :type type: str or ~bodycomplex.models.GeoJsonObjectType
    """

    _validation = {
        "type": {"required": True},
    }

    _attribute_map = {
        "type": {"key": "type", "type": "str"},
    }

    _subtype_map = {"type": {"MultiPolygon": "MultiPolygon", "Point": "Point", "Polygon": "Polygon"}}

    def __init__(self, **kwargs):
        super(GeoJsonObject, self).__init__(**kwargs)
        self.type = None  # type: Optional[str]


class MultiPolygon(GeoJsonObject):
    """MultiPolygon geometry.

    All required parameters must be populated in order to send to Azure.

    :param type: Required. GeoJSON object type.Constant filled by server.  Possible values include:
     "Point", "Polygon", "MultiPolygon".
    :type type: str or ~bodycomplex.models.GeoJsonObjectType
    :param coordinates: Required. Gets or sets Coordinates of GeoJSON Object.
     It must be an array of polygons, each polygon contains list of linear rings.
     For Polygons with more than one of these rings, the first MUST be the exterior ring,
     and any others MUST be interior rings.
    :type coordinates: list[list[list[list[float]]]]
    """

    _validation = {
        "type": {"required": True},
        "coordinates": {"required": True},
    }

    _attribute_map = {
        "type": {"key": "type", "type": "str"},
        "coordinates": {"key": "coordinates", "type": "[[[[float]]]]"},
    }

    def __init__(self, *, coordinates: List[List[List[List[float]]]], **kwargs):
        super(MultiPolygon, self).__init__(**kwargs)
        self.type = "MultiPolygon"  # type: str
        self.coordinates = coordinates


class Point(GeoJsonObject):
    """Point geometry.

    All required parameters must be populated in order to send to Azure.

    :param type: Required. GeoJSON object type.Constant filled by server.  Possible values include:
     "Point", "Polygon", "MultiPolygon".
    :type type: str or ~bodycomplex.models.GeoJsonObjectType
    :param coordinates: Required. Gets or sets the coordinate of this point.
     It must be an array of 2 or 3 elements for a 2D or 3D system.
    :type coordinates: list[float]
    """

    _validation = {
        "type": {"required": True},
        "coordinates": {"required": True},
    }

    _attribute_map = {
        "type": {"key": "type", "type": "str"},
        "coordinates": {"key": "coordinates", "type": "[float]"},
    }

    def __init__(self, *, coordinates: List[float], **kwargs):
        super(Point, self).__init__(**kwargs)
        self.type = "Point"  # type: str
        self.coordinates = coordinates


class Polygon(GeoJsonObject):
    """Polygon geometry.

    All required parameters must be populated in order to send to Azure.

    :param type: Required. GeoJSON object type.Constant filled by server.  Possible values include:
     "Point", "Polygon", "MultiPolygon".
    :type type: str or ~bodycomplex.models.GeoJsonObjectType
    :param coordinates: Required. Gets or sets type of the GeoJSON Object.
     It must be an array of linear ring coordinate arrays.
     For Polygons with more than one of these rings, the first MUST be the exterior ring,
     and any others MUST be interior rings.
    :type coordinates: list[list[list[float]]]
    """

    _validation = {
        "type": {"required": True},
        "coordinates": {"required": True},
    }

    _attribute_map = {
        "type": {"key": "type", "type": "str"},
        "coordinates": {"key": "coordinates", "type": "[[[float]]]"},
    }

    def __init__(self, *, coordinates: List[List[List[float]]], **kwargs):
        super(Polygon, self).__init__(**kwargs)
        self.type = "Polygon"  # type: str
        self.coordinates = coordinates
