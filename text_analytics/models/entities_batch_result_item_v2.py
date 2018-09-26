# coding: utf-8

"""
    Text Analytics API (v2.0)

    The Text Analytics API is a suite of text analytics web services built with best-in-class Microsoft machine learning algorithms.   The API can be used to analyze unstructured text for tasks such as sentiment analysis, key phrase extraction and language detection.   No training data is needed to use this API; just bring your text data.   This API uses advanced natural language processing techniques to deliver best in class predictions.    Further documentation can be found in https://docs.microsoft.com/en-us/azure/cognitive-services/text-analytics/overview  # noqa: E501

    OpenAPI spec version: 1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from swagger_client.models.entity_record_v2 import EntityRecordV2  # noqa: F401,E501


class EntitiesBatchResultItemV2(object):
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
        'id': 'str',
        'entities': 'list[EntityRecordV2]'
    }

    attribute_map = {
        'id': 'id',
        'entities': 'entities'
    }

    def __init__(self, id=None, entities=None):  # noqa: E501
        """EntitiesBatchResultItemV2 - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._entities = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if entities is not None:
            self.entities = entities

    @property
    def id(self):
        """Gets the id of this EntitiesBatchResultItemV2.  # noqa: E501

        Unique document identifier.  # noqa: E501

        :return: The id of this EntitiesBatchResultItemV2.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this EntitiesBatchResultItemV2.

        Unique document identifier.  # noqa: E501

        :param id: The id of this EntitiesBatchResultItemV2.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def entities(self):
        """Gets the entities of this EntitiesBatchResultItemV2.  # noqa: E501

        Recognized entities in the document.  # noqa: E501

        :return: The entities of this EntitiesBatchResultItemV2.  # noqa: E501
        :rtype: list[EntityRecordV2]
        """
        return self._entities

    @entities.setter
    def entities(self, entities):
        """Sets the entities of this EntitiesBatchResultItemV2.

        Recognized entities in the document.  # noqa: E501

        :param entities: The entities of this EntitiesBatchResultItemV2.  # noqa: E501
        :type: list[EntityRecordV2]
        """

        self._entities = entities

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

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, EntitiesBatchResultItemV2):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
