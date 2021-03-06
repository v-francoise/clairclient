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


class ClairpbPagedVulnerableAncestries(object):
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
        'current_page': 'str',
        'next_page': 'str',
        'limit': 'int',
        'vulnerability': 'ClairpbVulnerability',
        'ancestries': 'list[ClairpbIndexedAncestryName]'
    }

    attribute_map = {
        'current_page': 'current_page',
        'next_page': 'next_page',
        'limit': 'limit',
        'vulnerability': 'vulnerability',
        'ancestries': 'ancestries'
    }

    def __init__(self, current_page=None, next_page=None, limit=None, vulnerability=None, ancestries=None):  # noqa: E501
        """ClairpbPagedVulnerableAncestries - a model defined in OpenAPI"""  # noqa: E501

        self._current_page = None
        self._next_page = None
        self._limit = None
        self._vulnerability = None
        self._ancestries = None
        self.discriminator = None

        if current_page is not None:
            self.current_page = current_page
        if next_page is not None:
            self.next_page = next_page
        if limit is not None:
            self.limit = limit
        if vulnerability is not None:
            self.vulnerability = vulnerability
        if ancestries is not None:
            self.ancestries = ancestries

    @property
    def current_page(self):
        """Gets the current_page of this ClairpbPagedVulnerableAncestries.  # noqa: E501


        :return: The current_page of this ClairpbPagedVulnerableAncestries.  # noqa: E501
        :rtype: str
        """
        return self._current_page

    @current_page.setter
    def current_page(self, current_page):
        """Sets the current_page of this ClairpbPagedVulnerableAncestries.


        :param current_page: The current_page of this ClairpbPagedVulnerableAncestries.  # noqa: E501
        :type: str
        """

        self._current_page = current_page

    @property
    def next_page(self):
        """Gets the next_page of this ClairpbPagedVulnerableAncestries.  # noqa: E501

        if next_page is empty, it signals the end of all pages.  # noqa: E501

        :return: The next_page of this ClairpbPagedVulnerableAncestries.  # noqa: E501
        :rtype: str
        """
        return self._next_page

    @next_page.setter
    def next_page(self, next_page):
        """Sets the next_page of this ClairpbPagedVulnerableAncestries.

        if next_page is empty, it signals the end of all pages.  # noqa: E501

        :param next_page: The next_page of this ClairpbPagedVulnerableAncestries.  # noqa: E501
        :type: str
        """

        self._next_page = next_page

    @property
    def limit(self):
        """Gets the limit of this ClairpbPagedVulnerableAncestries.  # noqa: E501


        :return: The limit of this ClairpbPagedVulnerableAncestries.  # noqa: E501
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ClairpbPagedVulnerableAncestries.


        :param limit: The limit of this ClairpbPagedVulnerableAncestries.  # noqa: E501
        :type: int
        """

        self._limit = limit

    @property
    def vulnerability(self):
        """Gets the vulnerability of this ClairpbPagedVulnerableAncestries.  # noqa: E501


        :return: The vulnerability of this ClairpbPagedVulnerableAncestries.  # noqa: E501
        :rtype: ClairpbVulnerability
        """
        return self._vulnerability

    @vulnerability.setter
    def vulnerability(self, vulnerability):
        """Sets the vulnerability of this ClairpbPagedVulnerableAncestries.


        :param vulnerability: The vulnerability of this ClairpbPagedVulnerableAncestries.  # noqa: E501
        :type: ClairpbVulnerability
        """

        self._vulnerability = vulnerability

    @property
    def ancestries(self):
        """Gets the ancestries of this ClairpbPagedVulnerableAncestries.  # noqa: E501


        :return: The ancestries of this ClairpbPagedVulnerableAncestries.  # noqa: E501
        :rtype: list[ClairpbIndexedAncestryName]
        """
        return self._ancestries

    @ancestries.setter
    def ancestries(self, ancestries):
        """Sets the ancestries of this ClairpbPagedVulnerableAncestries.


        :param ancestries: The ancestries of this ClairpbPagedVulnerableAncestries.  # noqa: E501
        :type: list[ClairpbIndexedAncestryName]
        """

        self._ancestries = ancestries

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
        if not isinstance(other, ClairpbPagedVulnerableAncestries):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
