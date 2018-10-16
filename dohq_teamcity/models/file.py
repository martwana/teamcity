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

from dohq_teamcity.models.file import file  # noqa: F401,E501
from dohq_teamcity.models.files import Files  # noqa: F401,E501
from dohq_teamcity.models.href import Href  # noqa: F401,E501


class File(object):
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
        'children': 'Files',
        'content': 'Href',
        'full_name': 'str',
        'href': 'str',
        'modification_time': 'str',
        'name': 'str',
        'parent': 'file',
        'size': 'int'
    }

    attribute_map = {
        'children': 'children',
        'content': 'content',
        'full_name': 'fullName',
        'href': 'href',
        'modification_time': 'modificationTime',
        'name': 'name',
        'parent': 'parent',
        'size': 'size'
    }

    def __init__(self, children=None, content=None, full_name=None, href=None, modification_time=None, name=None, parent=None, size=None):  # noqa: E501
        """File - a model defined in Swagger"""  # noqa: E501

        self._children = None
        self._content = None
        self._full_name = None
        self._href = None
        self._modification_time = None
        self._name = None
        self._parent = None
        self._size = None
        self.discriminator = None

        if children is not None:
            self.children = children
        if content is not None:
            self.content = content
        if full_name is not None:
            self.full_name = full_name
        if href is not None:
            self.href = href
        if modification_time is not None:
            self.modification_time = modification_time
        if name is not None:
            self.name = name
        if parent is not None:
            self.parent = parent
        if size is not None:
            self.size = size

    @property
    def children(self):
        """Gets the children of this File.  # noqa: E501


        :return: The children of this File.  # noqa: E501
        :rtype: Files
        """
        return self._children

    @children.setter
    def children(self, children):
        """Sets the children of this File.


        :param children: The children of this File.  # noqa: E501
        :type: Files
        """

        self._children = children

    @property
    def content(self):
        """Gets the content of this File.  # noqa: E501


        :return: The content of this File.  # noqa: E501
        :rtype: Href
        """
        return self._content

    @content.setter
    def content(self, content):
        """Sets the content of this File.


        :param content: The content of this File.  # noqa: E501
        :type: Href
        """

        self._content = content

    @property
    def full_name(self):
        """Gets the full_name of this File.  # noqa: E501


        :return: The full_name of this File.  # noqa: E501
        :rtype: str
        """
        return self._full_name

    @full_name.setter
    def full_name(self, full_name):
        """Sets the full_name of this File.


        :param full_name: The full_name of this File.  # noqa: E501
        :type: str
        """

        self._full_name = full_name

    @property
    def href(self):
        """Gets the href of this File.  # noqa: E501


        :return: The href of this File.  # noqa: E501
        :rtype: str
        """
        return self._href

    @href.setter
    def href(self, href):
        """Sets the href of this File.


        :param href: The href of this File.  # noqa: E501
        :type: str
        """

        self._href = href

    @property
    def modification_time(self):
        """Gets the modification_time of this File.  # noqa: E501


        :return: The modification_time of this File.  # noqa: E501
        :rtype: str
        """
        return self._modification_time

    @modification_time.setter
    def modification_time(self, modification_time):
        """Sets the modification_time of this File.


        :param modification_time: The modification_time of this File.  # noqa: E501
        :type: str
        """

        self._modification_time = modification_time

    @property
    def name(self):
        """Gets the name of this File.  # noqa: E501


        :return: The name of this File.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this File.


        :param name: The name of this File.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def parent(self):
        """Gets the parent of this File.  # noqa: E501


        :return: The parent of this File.  # noqa: E501
        :rtype: file
        """
        return self._parent

    @parent.setter
    def parent(self, parent):
        """Sets the parent of this File.


        :param parent: The parent of this File.  # noqa: E501
        :type: file
        """

        self._parent = parent

    @property
    def size(self):
        """Gets the size of this File.  # noqa: E501


        :return: The size of this File.  # noqa: E501
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size):
        """Sets the size of this File.


        :param size: The size of this File.  # noqa: E501
        :type: int
        """

        self._size = size

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
        if issubclass(File, dict):
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
        if not isinstance(other, File):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
