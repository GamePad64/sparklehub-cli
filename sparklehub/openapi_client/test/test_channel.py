# coding: utf-8

"""
    SparkleHub API

    Test description  # noqa: E501

    The version of the OpenAPI document: v1
    Contact: alex@shishenko.com
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import sparklehub.openapi_client
from sparklehub.openapi_client.models.channel import Channel  # noqa: E501
from sparklehub.openapi_client.rest import ApiException

class TestChannel(unittest.TestCase):
    """Channel unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test Channel
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = sparklehub.openapi_client.models.channel.Channel()  # noqa: E501
        if include_optional :
            return Channel(
                id = '0', 
                title = '0', 
                description = '0'
            )
        else :
            return Channel(
        )

    def testChannel(self):
        """Test Channel"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
