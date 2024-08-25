#!/usr/bin/env python3
""" test utils """

import unittest
from unittest.mock import patch, Mock
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
        """ output get json """
        at_payload = {'json.return_value': test_payload}
        with patch("requests.get", return_value=Mock(**at_payload)) as y:
            self.assertEqual(get_json(test_url), test_payload)
            y.assert_called_once_with(test_url)


class TestMemoize(unittest.TestCase):
    """ memoize test class """
    def test_memoize(self) -> None:
        """ memoize test function """
        class TestClass:
            """ test class """
            def a_method(self):
                """ a_method function """
                return 42

            @memoize
            def a_property(self):
                """ a_property function """
                return self.a_method()

        with patch.object(cl_test, "a_method", return_value=lambda: 42) as z:
            cl_test = TestClass()
            self.assertEqual(cl_test.a_property(), 42)
            self.assertEqual(cl_test.a_property(), 42)
            z.assert_called_once()
