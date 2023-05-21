#!/usr/bin/env python3
"""
Module containing the unit tests for the access_nested_map
function from the utils module.
"""
import unittest
import utils
from parameterized import parameterized, parameterized_class


class TestAccessNestedMap(unittest.TestCase):
    """Test case for access_nested_map function"""
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(self, nested_map, path, expected_result):
        """
        Test the access_nested_map function with various
        input cases. Decorated with  @parameterized.expand.

        Args:
            nested_map (dict): Nested dictionary.
            path (tuple): The path of keys to access the value.
            expected_result: The expected result
        """
        result = utils.access_nested_map(nested_map, path)
        self.assertEqual(result, expected_result)

    @parameterized.expand([
        ({}, ("a",), "KeyError: 'a'"),
        ({"a": 1}, ("a", "b"), "KeyError: 'b'"),
    ])
    def test_access_nested_map_exception(self,
                                         nested_map, path, expected_error):
        """
        Test that a KeyError is raised with the expected
        error message for each test case.
        Decorated with  @parameterized.expand.

        Args:
            nested_map (dict): Nested dictionary.
            path (tuple): The path of keys to access value.
            expected_result: The expected error message.
        """
        # call the access_nested_map function within
        # the contect manager "assertRaises"
        # to assert that a KeyError was raised
        # The assertRaises context manager catches the
        # exception and allows us to make further assertions on it.
        with self.assertRaises(KeyError) as cm:
            utils.access_nested_map(nested_map, path)

        self.assertEqual(str(cm.exception), expected_error)
