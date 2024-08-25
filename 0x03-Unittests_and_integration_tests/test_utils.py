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
            ({"a": {"b": 2}}, ("a", "b"), 2),
        ]
    )
    def test_access_nested_map(self, nested_map, path, re_expected):
        """test nested access"""
        self.assertEqual(access_nested_map(nested_map, path), re_expected)

    @parameterized.expand([({"a": 1}, ("a", "b"), "b"), ({}, ("a",), "a")])
    def test_access_nested_map_exception(self, nested_map, path, re_expected):
        """test nested access exception"""
        with self.assertRaises(KeyError) as x:
            access_nested_map(nested_map, path)
        self.assertEqual(repr(x.exception), re_expected)
