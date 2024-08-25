#!/usr/bin/env python3
""" test utils """

import unittest
from parameterized import parameterized
from utils import access_nested_map, get_json, memoize


class TestAccessNestedMap(unittest.TestCase):
    """test access class"""

    @parameterized.expand(
        [
            ({"a": 1}, ("a",), 1),
            ({"a": {"b": 2}}, ("a",), {"b": 2}),
            ({"a": {"b": 2}}, ("a", "b"), 2)
        ]
    )
    def test_access_nested_map(self, nested_map, path, re_expected):
        """ test nested access """
        self.assertEqual(access_nested_map(nested_map, path), re_expected)

    @parameterized.expand([
        ({"a": 1}, ("a", "b"), 'b'),
        ({}, ("a",), 'a')
    ])
    def test_access_nested_map_exception(self, nested_map, path, re_expected):
        """ test nested access exception """
        with self.assertRaises(KeyError) as x:
            access_nested_map(nested_map, path)
        self.assertEqual(f"KeyError('{re_expected}')", repr(x.exception))


class TestGetJson(unittest.TestCase):
    """ test get json"""
    @parameterized.expand(
        [
            ("http://example.com", {"payload": True}),
            ("http://holberton.io", {"payload": False})
        ]
    )
    def test_get_json(self, test_url, test_payload):
        """output get json"""
        at_payload = {'json.return_value': test_payload}
        with patch("requests.get", return_value=Mock(**at_payload)) as y:
            self.assertEqual(get_json(test_url), test_payload)
            y.assert_called_once_with(test_url)
