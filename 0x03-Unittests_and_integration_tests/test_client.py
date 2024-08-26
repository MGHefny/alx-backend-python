#!/usr/bin/env python3
""" task test client """

import unittest
from unittest.mock import patch
from parameterized import parameterized, parameterized_class
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """ cls test git hub org """

    @parameterized.expand([
        ("google", {'login': "google"}),
        ("abc", {'login': "abc"}),
    ])
    @patch("client.get_json")
    def test_org(self, data_in, mock_g):
        """ correct result from test """
        cl_test = GithubOrgClient(data_in)
        cl_test.org()
        the_url = f"https://api.github.com/orgs/{data_in}"
        mock_g.assert_called_once_with(the_url)
