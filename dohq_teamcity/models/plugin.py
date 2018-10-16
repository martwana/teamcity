# coding: utf-8

"""
    TeamCity REST API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 10.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from dohq_teamcity.models.properties import Properties  # noqa: F401,E501


class Plugin(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'display_name': 'str',
        'load_path': 'str',
        'name': 'str',
        'parameters': 'Properties',
        'version': 'str'
    }

    attribute_map = {
        'display_name': 'displayName',
        'load_path': 'loadPath',
        'name': 'name',
        'parameters': 'parameters',
        'version': 'version'
    }

    def __init__(self, display_name=None, load_path=None, name=None, parameters=None, version=None):  # noqa: E501
        """Plugin - a model defined in Swagger"""  # noqa: E501

        self._display_name = None
        self._load_path = None
        self._name = None
        self._parameters = None
        self._version = None
        self.discriminator = None

        if display_name is not None:
            self.display_name = display_name
        if load_path is not None:
            self.load_path = load_path
        if name is not None:
            self.name = name
        if parameters is not None:
            self.parameters = parameters
        if version is not None:
            self.version = version

    @property
    def display_name(self):
        """Gets the display_name of this Plugin.  # noqa: E501


        :return: The display_name of this Plugin.  # noqa: E501
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """Sets the display_name of this Plugin.


        :param display_name: The display_name of this Plugin.  # noqa: E501
        :type: str
        """

        self._display_name = display_name

    @property
    def load_path(self):
        """Gets the load_path of this Plugin.  # noqa: E501


        :return: The load_path of this Plugin.  # noqa: E501
        :rtype: str
        """
        return self._load_path

    @load_path.setter
    def load_path(self, load_path):
        """Sets the load_path of this Plugin.


        :param load_path: The load_path of this Plugin.  # noqa: E501
        :type: str
        """

        self._load_path = load_path

    @property
    def name(self):
        """Gets the name of this Plugin.  # noqa: E501


        :return: The name of this Plugin.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Plugin.


        :param name: The name of this Plugin.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def parameters(self):
        """Gets the parameters of this Plugin.  # noqa: E501


        :return: The parameters of this Plugin.  # noqa: E501
        :rtype: Properties
        """
        return self._parameters

    @parameters.setter
    def parameters(self, parameters):
        """Sets the parameters of this Plugin.


        :param parameters: The parameters of this Plugin.  # noqa: E501
        :type: Properties
        """

        self._parameters = parameters

    @property
    def version(self):
        """Gets the version of this Plugin.  # noqa: E501


        :return: The version of this Plugin.  # noqa: E501
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this Plugin.


        :param version: The version of this Plugin.  # noqa: E501
        :type: str
        """

        self._version = version

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
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
        if issubclass(Plugin, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, Plugin):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
