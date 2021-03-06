# coding: utf-8

"""

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from datetime import datetime
from pprint import pformat
from six import iteritems
import re


class RepositoryCreationUrlAutoRest(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
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
        'scm_url': 'str',
        'pre_build_sync_enabled': 'bool',
        'build_configuration_rest': 'BuildConfigurationRest'
    }

    attribute_map = {
        'scm_url': 'scmUrl',
        'pre_build_sync_enabled': 'preBuildSyncEnabled',
        'build_configuration_rest': 'buildConfigurationRest'
    }

    def __init__(self, scm_url=None, pre_build_sync_enabled=False, build_configuration_rest=None):
        """
        RepositoryCreationUrlAutoRest - a model defined in Swagger
        """

        self._scm_url = None
        self._pre_build_sync_enabled = None
        self._build_configuration_rest = None

        if scm_url is not None:
          self.scm_url = scm_url
        if pre_build_sync_enabled is not None:
          self.pre_build_sync_enabled = pre_build_sync_enabled
        if build_configuration_rest is not None:
          self.build_configuration_rest = build_configuration_rest

    @property
    def scm_url(self):
        """
        Gets the scm_url of this RepositoryCreationUrlAutoRest.

        :return: The scm_url of this RepositoryCreationUrlAutoRest.
        :rtype: str
        """
        return self._scm_url

    @scm_url.setter
    def scm_url(self, scm_url):
        """
        Sets the scm_url of this RepositoryCreationUrlAutoRest.

        :param scm_url: The scm_url of this RepositoryCreationUrlAutoRest.
        :type: str
        """

        self._scm_url = scm_url

    @property
    def pre_build_sync_enabled(self):
        """
        Gets the pre_build_sync_enabled of this RepositoryCreationUrlAutoRest.

        :return: The pre_build_sync_enabled of this RepositoryCreationUrlAutoRest.
        :rtype: bool
        """
        return self._pre_build_sync_enabled

    @pre_build_sync_enabled.setter
    def pre_build_sync_enabled(self, pre_build_sync_enabled):
        """
        Sets the pre_build_sync_enabled of this RepositoryCreationUrlAutoRest.

        :param pre_build_sync_enabled: The pre_build_sync_enabled of this RepositoryCreationUrlAutoRest.
        :type: bool
        """

        self._pre_build_sync_enabled = pre_build_sync_enabled

    @property
    def build_configuration_rest(self):
        """
        Gets the build_configuration_rest of this RepositoryCreationUrlAutoRest.

        :return: The build_configuration_rest of this RepositoryCreationUrlAutoRest.
        :rtype: BuildConfigurationRest
        """
        return self._build_configuration_rest

    @build_configuration_rest.setter
    def build_configuration_rest(self, build_configuration_rest):
        """
        Sets the build_configuration_rest of this RepositoryCreationUrlAutoRest.

        :param build_configuration_rest: The build_configuration_rest of this RepositoryCreationUrlAutoRest.
        :type: BuildConfigurationRest
        """

        self._build_configuration_rest = build_configuration_rest

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
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
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

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        if not isinstance(other, RepositoryCreationUrlAutoRest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
