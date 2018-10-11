# coding: utf-8

from dohq_teamcity.custom.base_model import TeamCityObject



class StateField(TeamCityObject):
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
        'inherited': 'bool',
        'value': 'bool'
    }

    attribute_map = {
        'inherited': 'inherited',
        'value': 'value'
    }

    def __init__(self, inherited=False, value=False, teamcity=None):  # noqa: E501
        """StateField - a model defined in Swagger"""  # noqa: E501
        super(StateField, self).__init__(teamcity=teamcity)

        self._inherited = None
        self._value = None
        self.discriminator = None

        if inherited is not None:
            self.inherited = inherited
        if value is not None:
            self.value = value

    @property
    def inherited(self):
        """Gets the inherited of this StateField.  # noqa: E501


        :return: The inherited of this StateField.  # noqa: E501
        :rtype: bool
        """
        return self._inherited

    @inherited.setter
    def inherited(self, inherited):
        """Sets the inherited of this StateField.


        :param inherited: The inherited of this StateField.  # noqa: E501
        :type: bool
        """

        self._inherited = inherited

    @property
    def value(self):
        """Gets the value of this StateField.  # noqa: E501


        :return: The value of this StateField.  # noqa: E501
        :rtype: bool
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this StateField.


        :param value: The value of this StateField.  # noqa: E501
        :type: bool
        """

        self._value = value
