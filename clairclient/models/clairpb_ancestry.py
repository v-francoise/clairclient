# coding: utf-8

"""
    clair.proto

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    OpenAPI spec version: 3.0
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six


class ClairpbAncestry(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'name': 'str',
        'features': 'list[ClairpbFeature]',
        'layers': 'list[ClairpbLayer]',
        'scanned_listers': 'list[str]',
        'scanned_detectors': 'list[str]'
    }

    attribute_map = {
        'name': 'name',
        'features': 'features',
        'layers': 'layers',
        'scanned_listers': 'scanned_listers',
        'scanned_detectors': 'scanned_detectors'
    }

    def __init__(self, name=None, features=None, layers=None, scanned_listers=None, scanned_detectors=None):  # noqa: E501
        """ClairpbAncestry - a model defined in OpenAPI"""  # noqa: E501

        self._name = None
        self._features = None
        self._layers = None
        self._scanned_listers = None
        self._scanned_detectors = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if features is not None:
            self.features = features
        if layers is not None:
            self.layers = layers
        if scanned_listers is not None:
            self.scanned_listers = scanned_listers
        if scanned_detectors is not None:
            self.scanned_detectors = scanned_detectors

    @property
    def name(self):
        """Gets the name of this ClairpbAncestry.  # noqa: E501


        :return: The name of this ClairpbAncestry.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ClairpbAncestry.


        :param name: The name of this ClairpbAncestry.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def features(self):
        """Gets the features of this ClairpbAncestry.  # noqa: E501


        :return: The features of this ClairpbAncestry.  # noqa: E501
        :rtype: list[ClairpbFeature]
        """
        return self._features

    @features.setter
    def features(self, features):
        """Sets the features of this ClairpbAncestry.


        :param features: The features of this ClairpbAncestry.  # noqa: E501
        :type: list[ClairpbFeature]
        """

        self._features = features

    @property
    def layers(self):
        """Gets the layers of this ClairpbAncestry.  # noqa: E501


        :return: The layers of this ClairpbAncestry.  # noqa: E501
        :rtype: list[ClairpbLayer]
        """
        return self._layers

    @layers.setter
    def layers(self, layers):
        """Sets the layers of this ClairpbAncestry.


        :param layers: The layers of this ClairpbAncestry.  # noqa: E501
        :type: list[ClairpbLayer]
        """

        self._layers = layers

    @property
    def scanned_listers(self):
        """Gets the scanned_listers of this ClairpbAncestry.  # noqa: E501

        scanned_listers and scanned_detectors are used to scan this ancestry, it may be different from listers and detectors in ClairStatus since the ancestry could be scanned by previous version of Clair.  # noqa: E501

        :return: The scanned_listers of this ClairpbAncestry.  # noqa: E501
        :rtype: list[str]
        """
        return self._scanned_listers

    @scanned_listers.setter
    def scanned_listers(self, scanned_listers):
        """Sets the scanned_listers of this ClairpbAncestry.

        scanned_listers and scanned_detectors are used to scan this ancestry, it may be different from listers and detectors in ClairStatus since the ancestry could be scanned by previous version of Clair.  # noqa: E501

        :param scanned_listers: The scanned_listers of this ClairpbAncestry.  # noqa: E501
        :type: list[str]
        """

        self._scanned_listers = scanned_listers

    @property
    def scanned_detectors(self):
        """Gets the scanned_detectors of this ClairpbAncestry.  # noqa: E501


        :return: The scanned_detectors of this ClairpbAncestry.  # noqa: E501
        :rtype: list[str]
        """
        return self._scanned_detectors

    @scanned_detectors.setter
    def scanned_detectors(self, scanned_detectors):
        """Sets the scanned_detectors of this ClairpbAncestry.


        :param scanned_detectors: The scanned_detectors of this ClairpbAncestry.  # noqa: E501
        :type: list[str]
        """

        self._scanned_detectors = scanned_detectors

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
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
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ClairpbAncestry):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
