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
        """ correct output from test """
        cl_test = GithubOrgClient(data_in)
        cl_test.org()
        the_url = f"https://api.github.com/orgs/{data_in}"
        mock_g.assert_called_once_with(the_url)

    def test_public_repos_url(self):
        """ test pub repo """
        with patch('client.GithubOrgClient.org',
                   the_call=PropertyMock) as mock_g:
            pay_load = {"the_url": "World"}
            mock_g.return_value = pay_load
            cl_test = GithubOrgClient('check')
            output = cl_test._public_repos_url
            self.assertEqual(output, pay_load["the_url"])

    @patch('client.get_json')
    def test_public_repos(self, mock_g):
        """ check list of repo
        check mocked get jison """
        pay_load_j = [{'name': 'Google'}, {'name': 'Twitter'}]
        mock_g.return_value = pay_load_j

        with patch('client.GithubOrgClient._public_repos_url',
                   the_call=PropertyMock) as mock_p:

            mock_p.return_value = "mock_url"
            cl_test = GithubOrgClient('check')
            output = cl_test.public_repos()

            re_check = [i["name"] for i in pay_load_j]
            self.assertEqual(output, re_check)

            mock_g.assert_called_once()
            mock_p.assert_called_once()

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False)
    ])
    def test_has_license(self, test_repo, key_l, check_ex):
        """ test licens """
        output = GithubOrgClient.has_license(test_repo, key_l)
        self.assertEqual(output, check_ex)
