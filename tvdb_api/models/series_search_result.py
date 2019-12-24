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


class SeriesSearchResult(object):
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
        'aliases': 'list[str]',
        'banner': 'str',
        'first_aired': 'str',
        'id': 'int',
        'network': 'str',
        'overview': 'str',
        'series_name': 'str',
        'slug': 'str',
        'status': 'str'
    }

    attribute_map = {
        'aliases': 'aliases',
        'banner': 'banner',
        'first_aired': 'firstAired',
        'id': 'id',
        'network': 'network',
        'overview': 'overview',
        'series_name': 'seriesName',
        'slug': 'slug',
        'status': 'status'
    }

    def __init__(self, aliases=None, banner=None, first_aired=None, id=None, network=None, overview=None, series_name=None, slug=None, status=None):  # noqa: E501
        """SeriesSearchResult - a model defined in Swagger"""  # noqa: E501

        self._aliases = None
        self._banner = None
        self._first_aired = None
        self._id = None
        self._network = None
        self._overview = None
        self._series_name = None
        self._slug = None
        self._status = None
        self.discriminator = None

        if aliases is not None:
            self.aliases = aliases
        if banner is not None:
            self.banner = banner
        if first_aired is not None:
            self.first_aired = first_aired
        if id is not None:
            self.id = id
        if network is not None:
            self.network = network
        if overview is not None:
            self.overview = overview
        if series_name is not None:
            self.series_name = series_name
        if slug is not None:
            self.slug = slug
        if status is not None:
            self.status = status

    @property
    def aliases(self):
        """Gets the aliases of this SeriesSearchResult.  # noqa: E501


        :return: The aliases of this SeriesSearchResult.  # noqa: E501
        :rtype: list[str]
        """
        return self._aliases

    @aliases.setter
    def aliases(self, aliases):
        """Sets the aliases of this SeriesSearchResult.


        :param aliases: The aliases of this SeriesSearchResult.  # noqa: E501
        :type: list[str]
        """

        self._aliases = aliases

    @property
    def banner(self):
        """Gets the banner of this SeriesSearchResult.  # noqa: E501


        :return: The banner of this SeriesSearchResult.  # noqa: E501
        :rtype: str
        """
        return self._banner

    @banner.setter
    def banner(self, banner):
        """Sets the banner of this SeriesSearchResult.


        :param banner: The banner of this SeriesSearchResult.  # noqa: E501
        :type: str
        """

        self._banner = banner

    @property
    def first_aired(self):
        """Gets the first_aired of this SeriesSearchResult.  # noqa: E501


        :return: The first_aired of this SeriesSearchResult.  # noqa: E501
        :rtype: str
        """
        return self._first_aired

    @first_aired.setter
    def first_aired(self, first_aired):
        """Sets the first_aired of this SeriesSearchResult.


        :param first_aired: The first_aired of this SeriesSearchResult.  # noqa: E501
        :type: str
        """

        self._first_aired = first_aired

    @property
    def id(self):
        """Gets the id of this SeriesSearchResult.  # noqa: E501


        :return: The id of this SeriesSearchResult.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this SeriesSearchResult.


        :param id: The id of this SeriesSearchResult.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def network(self):
        """Gets the network of this SeriesSearchResult.  # noqa: E501


        :return: The network of this SeriesSearchResult.  # noqa: E501
        :rtype: str
        """
        return self._network

    @network.setter
    def network(self, network):
        """Sets the network of this SeriesSearchResult.


        :param network: The network of this SeriesSearchResult.  # noqa: E501
        :type: str
        """

        self._network = network

    @property
    def overview(self):
        """Gets the overview of this SeriesSearchResult.  # noqa: E501


        :return: The overview of this SeriesSearchResult.  # noqa: E501
        :rtype: str
        """
        return self._overview

    @overview.setter
    def overview(self, overview):
        """Sets the overview of this SeriesSearchResult.


        :param overview: The overview of this SeriesSearchResult.  # noqa: E501
        :type: str
        """

        self._overview = overview

    @property
    def series_name(self):
        """Gets the series_name of this SeriesSearchResult.  # noqa: E501


        :return: The series_name of this SeriesSearchResult.  # noqa: E501
        :rtype: str
        """
        return self._series_name

    @series_name.setter
    def series_name(self, series_name):
        """Sets the series_name of this SeriesSearchResult.


        :param series_name: The series_name of this SeriesSearchResult.  # noqa: E501
        :type: str
        """

        self._series_name = series_name

    @property
    def slug(self):
        """Gets the slug of this SeriesSearchResult.  # noqa: E501


        :return: The slug of this SeriesSearchResult.  # noqa: E501
        :rtype: str
        """
        return self._slug

    @slug.setter
    def slug(self, slug):
        """Sets the slug of this SeriesSearchResult.


        :param slug: The slug of this SeriesSearchResult.  # noqa: E501
        :type: str
        """

        self._slug = slug

    @property
    def status(self):
        """Gets the status of this SeriesSearchResult.  # noqa: E501


        :return: The status of this SeriesSearchResult.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this SeriesSearchResult.


        :param status: The status of this SeriesSearchResult.  # noqa: E501
        :type: str
        """

        self._status = status

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
        if issubclass(SeriesSearchResult, dict):
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
        if not isinstance(other, SeriesSearchResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
