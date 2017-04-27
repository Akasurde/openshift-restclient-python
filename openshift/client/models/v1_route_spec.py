# coding: utf-8

"""
    OpenShift API (with Kubernetes)

    OpenShift provides builds, application lifecycle, image content management, and administrative policy on top of Kubernetes. The API allows consistent management of those objects.  All API operations are authenticated via an Authorization bearer token that is provided for service accounts as a generated secret (in JWT form) or via the native OAuth endpoint located at /oauth/authorize. Core infrastructure components may use client certificates that require no authentication.  All API operations return a 'resourceVersion' string that represents the version of the object in the underlying storage. The standard LIST operation performs a snapshot read of the underlying objects, returning a resourceVersion representing a consistent version of the listed objects. The WATCH operation allows all updates to a set of objects after the provided resourceVersion to be observed by a client. By listing and beginning a watch from the returned resourceVersion, clients may observe a consistent view of the state of one or more objects. Note that WATCH always returns the update after the provided resourceVersion. Watch may be extended a limited time in the past - using etcd 2 the watch window is 1000 events (which on a large cluster may only be a few tens of seconds) so clients must explicitly handle the \"watch to old error\" by re-listing.  Objects are divided into two rough categories - those that have a lifecycle and must reflect the state of the cluster, and those that have no state. Objects with lifecycle typically have three main sections:  * 'metadata' common to all objects * a 'spec' that represents the desired state * a 'status' that represents how much of the desired state is reflected on   the cluster at the current time  Objects that have no state have 'metadata' but may lack a 'spec' or 'status' section.  Objects are divided into those that are namespace scoped (only exist inside of a namespace) and those that are cluster scoped (exist outside of a namespace). A namespace scoped resource will be deleted when the namespace is deleted and cannot be created if the namespace has not yet been created or is in the process of deletion. Cluster scoped resources are typically only accessible to admins - resources like nodes, persistent volumes, and cluster policy.  All objects have a schema that is a combination of the 'kind' and 'apiVersion' fields. This schema is additive only for any given version - no backwards incompatible changes are allowed without incrementing the apiVersion. The server will return and accept a number of standard responses that share a common schema - for instance, the common error type is 'unversioned.Status' (described below) and will be returned on any error from the API server.  The API is available in multiple serialization formats - the default is JSON (Accept: application/json and Content-Type: application/json) but clients may also use YAML (application/yaml) or the native Protobuf schema (application/vnd.kubernetes.protobuf). Note that the format of the WATCH API call is slightly different - for JSON it returns newline delimited objects while for Protobuf it returns length-delimited frames (4 bytes in network-order) that contain a 'versioned.Watch' Protobuf object.  See the OpenShift documentation at https://docs.openshift.org for more information. 

    OpenAPI spec version: v1.5.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class V1RouteSpec(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, alternate_backends=None, host=None, path=None, port=None, tls=None, to=None, wildcard_policy=None):
        """
        V1RouteSpec - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'alternate_backends': 'list[V1RouteTargetReference]',
            'host': 'str',
            'path': 'str',
            'port': 'V1RoutePort',
            'tls': 'V1TLSConfig',
            'to': 'V1RouteTargetReference',
            'wildcard_policy': 'str'
        }

        self.attribute_map = {
            'alternate_backends': 'alternateBackends',
            'host': 'host',
            'path': 'path',
            'port': 'port',
            'tls': 'tls',
            'to': 'to',
            'wildcard_policy': 'wildcardPolicy'
        }

        self._alternate_backends = alternate_backends
        self._host = host
        self._path = path
        self._port = port
        self._tls = tls
        self._to = to
        self._wildcard_policy = wildcard_policy

    @property
    def alternate_backends(self):
        """
        Gets the alternate_backends of this V1RouteSpec.
        alternateBackends is an extension of the 'to' field. If more than one service needs to be pointed to, then use this field. Use the weight field in RouteTargetReference object to specify relative preference. If the weight field is zero, the backend is ignored.

        :return: The alternate_backends of this V1RouteSpec.
        :rtype: list[V1RouteTargetReference]
        """
        return self._alternate_backends

    @alternate_backends.setter
    def alternate_backends(self, alternate_backends):
        """
        Sets the alternate_backends of this V1RouteSpec.
        alternateBackends is an extension of the 'to' field. If more than one service needs to be pointed to, then use this field. Use the weight field in RouteTargetReference object to specify relative preference. If the weight field is zero, the backend is ignored.

        :param alternate_backends: The alternate_backends of this V1RouteSpec.
        :type: list[V1RouteTargetReference]
        """

        self._alternate_backends = alternate_backends

    @property
    def host(self):
        """
        Gets the host of this V1RouteSpec.
        host is an alias/DNS that points to the service. Optional. If not specified a route name will typically be automatically chosen. Must follow DNS952 subdomain conventions.

        :return: The host of this V1RouteSpec.
        :rtype: str
        """
        return self._host

    @host.setter
    def host(self, host):
        """
        Sets the host of this V1RouteSpec.
        host is an alias/DNS that points to the service. Optional. If not specified a route name will typically be automatically chosen. Must follow DNS952 subdomain conventions.

        :param host: The host of this V1RouteSpec.
        :type: str
        """
        if host is None:
            raise ValueError("Invalid value for `host`, must not be `None`")

        self._host = host

    @property
    def path(self):
        """
        Gets the path of this V1RouteSpec.
        Path that the router watches for, to route traffic for to the service. Optional

        :return: The path of this V1RouteSpec.
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        """
        Sets the path of this V1RouteSpec.
        Path that the router watches for, to route traffic for to the service. Optional

        :param path: The path of this V1RouteSpec.
        :type: str
        """

        self._path = path

    @property
    def port(self):
        """
        Gets the port of this V1RouteSpec.
        If specified, the port to be used by the router. Most routers will use all endpoints exposed by the service by default - set this value to instruct routers which port to use.

        :return: The port of this V1RouteSpec.
        :rtype: V1RoutePort
        """
        return self._port

    @port.setter
    def port(self, port):
        """
        Sets the port of this V1RouteSpec.
        If specified, the port to be used by the router. Most routers will use all endpoints exposed by the service by default - set this value to instruct routers which port to use.

        :param port: The port of this V1RouteSpec.
        :type: V1RoutePort
        """

        self._port = port

    @property
    def tls(self):
        """
        Gets the tls of this V1RouteSpec.
        The tls field provides the ability to configure certificates and termination for the route.

        :return: The tls of this V1RouteSpec.
        :rtype: V1TLSConfig
        """
        return self._tls

    @tls.setter
    def tls(self, tls):
        """
        Sets the tls of this V1RouteSpec.
        The tls field provides the ability to configure certificates and termination for the route.

        :param tls: The tls of this V1RouteSpec.
        :type: V1TLSConfig
        """

        self._tls = tls

    @property
    def to(self):
        """
        Gets the to of this V1RouteSpec.
        to is an object the route should use as the primary backend. Only the Service kind is allowed, and it will be defaulted to Service. If the weight field is set to zero, no traffic will be sent to this service.

        :return: The to of this V1RouteSpec.
        :rtype: V1RouteTargetReference
        """
        return self._to

    @to.setter
    def to(self, to):
        """
        Sets the to of this V1RouteSpec.
        to is an object the route should use as the primary backend. Only the Service kind is allowed, and it will be defaulted to Service. If the weight field is set to zero, no traffic will be sent to this service.

        :param to: The to of this V1RouteSpec.
        :type: V1RouteTargetReference
        """
        if to is None:
            raise ValueError("Invalid value for `to`, must not be `None`")

        self._to = to

    @property
    def wildcard_policy(self):
        """
        Gets the wildcard_policy of this V1RouteSpec.
        Wildcard policy if any for the route. Currently only 'Subdomain' or 'None' is allowed.

        :return: The wildcard_policy of this V1RouteSpec.
        :rtype: str
        """
        return self._wildcard_policy

    @wildcard_policy.setter
    def wildcard_policy(self, wildcard_policy):
        """
        Sets the wildcard_policy of this V1RouteSpec.
        Wildcard policy if any for the route. Currently only 'Subdomain' or 'None' is allowed.

        :param wildcard_policy: The wildcard_policy of this V1RouteSpec.
        :type: str
        """

        self._wildcard_policy = wildcard_policy

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        if not isinstance(other, V1RouteSpec):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
