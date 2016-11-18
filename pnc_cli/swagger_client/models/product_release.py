# coding: utf-8

"""
Copyright 2015 SmartBear Software

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.

    Ref: https://github.com/swagger-api/swagger-codegen
"""

from datetime import datetime
from pprint import pformat
from six import iteritems


class ProductRelease(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        ProductRelease - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'int',
            'version': 'str',
            'support_level': 'str',
            'release_date': 'datetime',
            'download_url': 'str',
            'issue_tracker_url': 'str',
            'product_milestone': 'ProductMilestone',
            'field_handler': 'FieldHandler',
            'product_version': 'ProductVersion'
        }

        self.attribute_map = {
            'id': 'id',
            'version': 'version',
            'support_level': 'supportLevel',
            'release_date': 'releaseDate',
            'download_url': 'downloadUrl',
            'issue_tracker_url': 'issueTrackerUrl',
            'product_milestone': 'productMilestone',
            'field_handler': 'fieldHandler',
            'product_version': 'productVersion'
        }

        self._id = None
        self._version = None
        self._support_level = None
        self._release_date = None
        self._download_url = None
        self._issue_tracker_url = None
        self._product_milestone = None
        self._field_handler = None
        self._product_version = None

    @property
    def id(self):
        """
        Gets the id of this ProductRelease.


        :return: The id of this ProductRelease.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this ProductRelease.


        :param id: The id of this ProductRelease.
        :type: int
        """
        self._id = id

    @property
    def version(self):
        """
        Gets the version of this ProductRelease.


        :return: The version of this ProductRelease.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """
        Sets the version of this ProductRelease.


        :param version: The version of this ProductRelease.
        :type: str
        """
        self._version = version

    @property
    def support_level(self):
        """
        Gets the support_level of this ProductRelease.


        :return: The support_level of this ProductRelease.
        :rtype: str
        """
        return self._support_level

    @support_level.setter
    def support_level(self, support_level):
        """
        Sets the support_level of this ProductRelease.


        :param support_level: The support_level of this ProductRelease.
        :type: str
        """
        allowed_values = ["UNRELEASED", "EARLYACCESS", "SUPPORTED", "EXTENDED_SUPPORT", "EOL"]
        if support_level not in allowed_values:
            raise ValueError(
                "Invalid value for `support_level`, must be one of {0}"
                .format(allowed_values)
            )
        self._support_level = support_level

    @property
    def release_date(self):
        """
        Gets the release_date of this ProductRelease.


        :return: The release_date of this ProductRelease.
        :rtype: datetime
        """
        return self._release_date

    @release_date.setter
    def release_date(self, release_date):
        """
        Sets the release_date of this ProductRelease.


        :param release_date: The release_date of this ProductRelease.
        :type: datetime
        """
        self._release_date = release_date

    @property
    def download_url(self):
        """
        Gets the download_url of this ProductRelease.


        :return: The download_url of this ProductRelease.
        :rtype: str
        """
        return self._download_url

    @download_url.setter
    def download_url(self, download_url):
        """
        Sets the download_url of this ProductRelease.


        :param download_url: The download_url of this ProductRelease.
        :type: str
        """
        self._download_url = download_url

    @property
    def issue_tracker_url(self):
        """
        Gets the issue_tracker_url of this ProductRelease.


        :return: The issue_tracker_url of this ProductRelease.
        :rtype: str
        """
        return self._issue_tracker_url

    @issue_tracker_url.setter
    def issue_tracker_url(self, issue_tracker_url):
        """
        Sets the issue_tracker_url of this ProductRelease.


        :param issue_tracker_url: The issue_tracker_url of this ProductRelease.
        :type: str
        """
        self._issue_tracker_url = issue_tracker_url

    @property
    def product_milestone(self):
        """
        Gets the product_milestone of this ProductRelease.


        :return: The product_milestone of this ProductRelease.
        :rtype: ProductMilestone
        """
        return self._product_milestone

    @product_milestone.setter
    def product_milestone(self, product_milestone):
        """
        Sets the product_milestone of this ProductRelease.


        :param product_milestone: The product_milestone of this ProductRelease.
        :type: ProductMilestone
        """
        self._product_milestone = product_milestone

    @property
    def field_handler(self):
        """
        Gets the field_handler of this ProductRelease.


        :return: The field_handler of this ProductRelease.
        :rtype: FieldHandler
        """
        return self._field_handler

    @field_handler.setter
    def field_handler(self, field_handler):
        """
        Sets the field_handler of this ProductRelease.


        :param field_handler: The field_handler of this ProductRelease.
        :type: FieldHandler
        """
        self._field_handler = field_handler

    @property
    def product_version(self):
        """
        Gets the product_version of this ProductRelease.


        :return: The product_version of this ProductRelease.
        :rtype: ProductVersion
        """
        return self._product_version

    @product_version.setter
    def product_version(self, product_version):
        """
        Sets the product_version of this ProductRelease.


        :param product_version: The product_version of this ProductRelease.
        :type: ProductVersion
        """
        self._product_version = product_version

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, datetime):
                result[attr] = str(value.date())
            else:
                result[attr] = value

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()
