#!/usr/bin/env python3
""" task test client """

import unittest
from unittest.mock import patch, PropertyMock
from parameterized import parameterized, parameterized_class
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """ cls test git hub org """

    @parameterized.expand([
        ('google',),
        ('abc')
    ])
    @patch('client.get_json')
    def test_org(self, data_in, mock_g):
        """ correct result from test """
        cl_test = GithubOrgClient(data_in)
        cl_test.org()
        the_url = f"https://api.github.com/orgs/{data_in}"
        mock_g.assert_called_once_with(the_url)

    def test_public_repos_url(self):
        """ """
        with patch('client.GithubOrgClient.org',
                   the_call=PropertyMock) as mock_g:
            pay_load = {"the_url": "World"}
            mock_g.return_value = pay_load
            cl_test = GithubOrgClient('check')
            output = cl_test._public_repos_url
            self.assertEqual(output, pay_load["the_url"])
