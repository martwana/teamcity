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

from dohq_teamcity.models.stack_trace_element import StackTraceElement  # noqa: F401,E501
from dohq_teamcity.models.throwable import Throwable  # noqa: F401,E501


class Exception(object):
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
        'cause': 'Throwable',
        'localized_message': 'str',
        'message': 'str',
        'stack_trace': 'list[StackTraceElement]',
        'suppressed': 'list[Throwable]'
    }

    attribute_map = {
        'cause': 'cause',
        'localized_message': 'localizedMessage',
        'message': 'message',
        'stack_trace': 'stackTrace',
        'suppressed': 'suppressed'
    }

    def __init__(self, cause=None, localized_message=None, message=None, stack_trace=None, suppressed=None):  # noqa: E501
        """Exception - a model defined in Swagger"""  # noqa: E501

        self._cause = None
        self._localized_message = None
        self._message = None
        self._stack_trace = None
        self._suppressed = None
        self.discriminator = None

        if cause is not None:
            self.cause = cause
        if localized_message is not None:
            self.localized_message = localized_message
        if message is not None:
            self.message = message
        if stack_trace is not None:
            self.stack_trace = stack_trace
        if suppressed is not None:
            self.suppressed = suppressed

    @property
    def cause(self):
        """Gets the cause of this Exception.  # noqa: E501


        :return: The cause of this Exception.  # noqa: E501
        :rtype: Throwable
        """
        return self._cause

    @cause.setter
    def cause(self, cause):
        """Sets the cause of this Exception.


        :param cause: The cause of this Exception.  # noqa: E501
        :type: Throwable
        """

        self._cause = cause

    @property
    def localized_message(self):
        """Gets the localized_message of this Exception.  # noqa: E501


        :return: The localized_message of this Exception.  # noqa: E501
        :rtype: str
        """
        return self._localized_message

    @localized_message.setter
    def localized_message(self, localized_message):
        """Sets the localized_message of this Exception.


        :param localized_message: The localized_message of this Exception.  # noqa: E501
        :type: str
        """

        self._localized_message = localized_message

    @property
    def message(self):
        """Gets the message of this Exception.  # noqa: E501


        :return: The message of this Exception.  # noqa: E501
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this Exception.


        :param message: The message of this Exception.  # noqa: E501
        :type: str
        """

        self._message = message

    @property
    def stack_trace(self):
        """Gets the stack_trace of this Exception.  # noqa: E501


        :return: The stack_trace of this Exception.  # noqa: E501
        :rtype: list[StackTraceElement]
        """
        return self._stack_trace

    @stack_trace.setter
    def stack_trace(self, stack_trace):
        """Sets the stack_trace of this Exception.


        :param stack_trace: The stack_trace of this Exception.  # noqa: E501
        :type: list[StackTraceElement]
        """

        self._stack_trace = stack_trace

    @property
    def suppressed(self):
        """Gets the suppressed of this Exception.  # noqa: E501


        :return: The suppressed of this Exception.  # noqa: E501
        :rtype: list[Throwable]
        """
        return self._suppressed

    @suppressed.setter
    def suppressed(self, suppressed):
        """Sets the suppressed of this Exception.


        :param suppressed: The suppressed of this Exception.  # noqa: E501
        :type: list[Throwable]
        """

        self._suppressed = suppressed

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
        if issubclass(Exception, dict):
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
        if not isinstance(other, Exception):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
