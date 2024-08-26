#!/usr/bin/env python3
""" task test client """

import unittest
from unittest.mock import patch
from parameterized import parameterized
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """cls test git hub org"""

    @parameterized.expand([
        ("google", {'login': "google"}),
        ("abc", {'login': "abc"}),
    ])
    @patch("client.get_json")
    def test_org(self, data_in, get_mock):
        """correct result from test"""
        cl_test = GithubOrgClient(data_in)
        cl_test.org()
        the_url = f"https://api.github.com/orgs/{org_name}"
        mock_get_json.assert_called_once_with(the_url)
