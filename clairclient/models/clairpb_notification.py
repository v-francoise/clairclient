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


class ClairpbNotification(object):
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
        'created': 'str',
        'notified': 'str',
        'deleted': 'str',
        'old': 'ClairpbPagedVulnerableAncestries',
        'new': 'ClairpbPagedVulnerableAncestries'
    }

    attribute_map = {
        'name': 'name',
        'created': 'created',
        'notified': 'notified',
        'deleted': 'deleted',
        'old': 'old',
        'new': 'new'
    }

    def __init__(self, name=None, created=None, notified=None, deleted=None, old=None, new=None):  # noqa: E501
        """ClairpbNotification - a model defined in OpenAPI"""  # noqa: E501

        self._name = None
        self._created = None
        self._notified = None
        self._deleted = None
        self._old = None
        self._new = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if created is not None:
            self.created = created
        if notified is not None:
            self.notified = notified
        if deleted is not None:
            self.deleted = deleted
        if old is not None:
            self.old = old
        if new is not None:
            self.new = new

    @property
    def name(self):
        """Gets the name of this ClairpbNotification.  # noqa: E501


        :return: The name of this ClairpbNotification.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ClairpbNotification.


        :param name: The name of this ClairpbNotification.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def created(self):
        """Gets the created of this ClairpbNotification.  # noqa: E501


        :return: The created of this ClairpbNotification.  # noqa: E501
        :rtype: str
        """
        return self._created

    @created.setter
    def created(self, created):
        """Sets the created of this ClairpbNotification.


        :param created: The created of this ClairpbNotification.  # noqa: E501
        :type: str
        """

        self._created = created

    @property
    def notified(self):
        """Gets the notified of this ClairpbNotification.  # noqa: E501


        :return: The notified of this ClairpbNotification.  # noqa: E501
        :rtype: str
        """
        return self._notified

    @notified.setter
    def notified(self, notified):
        """Sets the notified of this ClairpbNotification.


        :param notified: The notified of this ClairpbNotification.  # noqa: E501
        :type: str
        """

        self._notified = notified

    @property
    def deleted(self):
        """Gets the deleted of this ClairpbNotification.  # noqa: E501


        :return: The deleted of this ClairpbNotification.  # noqa: E501
        :rtype: str
        """
        return self._deleted

    @deleted.setter
    def deleted(self, deleted):
        """Sets the deleted of this ClairpbNotification.


        :param deleted: The deleted of this ClairpbNotification.  # noqa: E501
        :type: str
        """

        self._deleted = deleted

    @property
    def old(self):
        """Gets the old of this ClairpbNotification.  # noqa: E501


        :return: The old of this ClairpbNotification.  # noqa: E501
        :rtype: ClairpbPagedVulnerableAncestries
        """
        return self._old

    @old.setter
    def old(self, old):
        """Sets the old of this ClairpbNotification.


        :param old: The old of this ClairpbNotification.  # noqa: E501
        :type: ClairpbPagedVulnerableAncestries
        """

        self._old = old

    @property
    def new(self):
        """Gets the new of this ClairpbNotification.  # noqa: E501


        :return: The new of this ClairpbNotification.  # noqa: E501
        :rtype: ClairpbPagedVulnerableAncestries
        """
        return self._new

    @new.setter
    def new(self, new):
        """Sets the new of this ClairpbNotification.


        :param new: The new of this ClairpbNotification.  # noqa: E501
        :type: ClairpbPagedVulnerableAncestries
        """

        self._new = new

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
        if not isinstance(other, ClairpbNotification):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
