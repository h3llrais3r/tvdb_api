# coding: utf-8

"""
    TheTVDB API v2

    API v3 targets v2 functionality with a few minor additions. The API is accessible via https://api.thetvdb.com and provides the following REST endpoints in JSON format.   How to use this API documentation ----------------   You may browse the API routes without authentication, but if you wish to send requests to the API and see response data, then you must authenticate. 1. Obtain a JWT token by `POST`ing  to the `/login` route in the `Authentication` section with your API key and credentials. 1. Paste the JWT token from the response into the \"JWT Token\" field at the top of the page and click the 'Add Token' button.   You will now be able to use the remaining routes to send requests to the API and get a response.   Language Selection ----------------   Language selection is done via the `Accept-Language` header. At the moment, you may only pass one language abbreviation in the header at a time. Valid language abbreviations can be found at the `/languages` route..   Authentication ----------------   Authentication to use the API is similar to the How-to section above. Users must `POST` to the `/login` route with their API key and credentials in the following format in order to obtain a JWT token.  `{\"apikey\":\"APIKEY\",\"username\":\"USERNAME\",\"userkey\":\"USERKEY\"}`  Note that the username and key are ONLY required for the `/user` routes. The user's key is labled `Account Identifier` in the account section of the main site. The token is then used in all subsequent requests by providing it in the `Authorization` header. The header will look like: `Authorization: Bearer <yourJWTtoken>`. Currently, the token expires after 24 hours. You can `GET` the `/refresh_token` route to extend that expiration date.   Versioning ----------------   You may request a different version of the API by including an `Accept` header in your request with the following format: `Accept:application/vnd.thetvdb.v$VERSION`. This documentation automatically uses the version seen at the top and bottom of the page.  # noqa: E501

    OpenAPI spec version: 3.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class Language(object):
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
        'abbreviation': 'str',
        'english_name': 'str',
        'id': 'int',
        'name': 'str'
    }

    attribute_map = {
        'abbreviation': 'abbreviation',
        'english_name': 'englishName',
        'id': 'id',
        'name': 'name'
    }

    def __init__(self, abbreviation=None, english_name=None, id=None, name=None):  # noqa: E501
        """Language - a model defined in Swagger"""  # noqa: E501

        self._abbreviation = None
        self._english_name = None
        self._id = None
        self._name = None
        self.discriminator = None

        if abbreviation is not None:
            self.abbreviation = abbreviation
        if english_name is not None:
            self.english_name = english_name
        if id is not None:
            self.id = id
        if name is not None:
            self.name = name

    @property
    def abbreviation(self):
        """Gets the abbreviation of this Language.  # noqa: E501


        :return: The abbreviation of this Language.  # noqa: E501
        :rtype: str
        """
        return self._abbreviation

    @abbreviation.setter
    def abbreviation(self, abbreviation):
        """Sets the abbreviation of this Language.


        :param abbreviation: The abbreviation of this Language.  # noqa: E501
        :type: str
        """

        self._abbreviation = abbreviation

    @property
    def english_name(self):
        """Gets the english_name of this Language.  # noqa: E501


        :return: The english_name of this Language.  # noqa: E501
        :rtype: str
        """
        return self._english_name

    @english_name.setter
    def english_name(self, english_name):
        """Sets the english_name of this Language.


        :param english_name: The english_name of this Language.  # noqa: E501
        :type: str
        """

        self._english_name = english_name

    @property
    def id(self):
        """Gets the id of this Language.  # noqa: E501


        :return: The id of this Language.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Language.


        :param id: The id of this Language.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this Language.  # noqa: E501


        :return: The name of this Language.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Language.


        :param name: The name of this Language.  # noqa: E501
        :type: str
        """

        self._name = name

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
        if issubclass(Language, dict):
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
        if not isinstance(other, Language):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
