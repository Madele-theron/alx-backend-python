#!/usr/bin/env python3
"""
Module containing the unit tests for the access_nested_map
function from the utils module.
"""
import unittest
from unittest.mock import patch
import utils
from parameterized import parameterized, parameterized_class
from typing import Any, Dict, Tuple


class TestAccessNestedMap(unittest.TestCase):
    """Test case for access_nested_map function"""
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(
            self, nested_map: Dict[str, Any], path: Tuple[str, ...],
            expected_error: Any) -> None:
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
        ({}, ("a",), KeyError('a')),
        ({"a": 1}, ("a", "b"), KeyError('b')),
    ])
    def test_access_nested_map_exception(
            self, nested_map: Dict[str, Any], path: Tuple[str, ...],
            expected_error: Any) -> None:

        """
        Test that a KeyError is raised with the expected
        error message for each test case.
        Decorated with  @parameterized.expand.

        Args:
            nested_map (dict): Nested dictionary.
            path (tuple): The path of keys to access value.
            expected_result: The expected error message.
        """
        with self.assertRaises(KeyError) as cm:
            utils.access_nested_map(nested_map, path)

        self.assertEqual(repr(cm.exception), repr(expected_error))


class TestGetJson(unittest.TestCase):
    """Class that contains the test cases for the get_json function."""

    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False}),
    ])
    @patch('utils.requests.get')
    def test_get_json(self, test_url: str, test_payload: Dict[str, Any],
                      mock_requests: Any) -> None:
        """
        Method to test that the get_json function returns
        the expected result.
        """

        mock_response = mock_requests.return_value
        mock_response.json.return_value = test_payload

        result = utils.get_json(test_url)

        self.assertEqual(result, test_payload)
        mock_requests.assert_called_once_with(test_url)


class TestMemoize(unittest.TestCase):
    """A class that contains the test case
    for memoization decorator."""

    class TestClass:
        """A method that tests the classes"""

        def a_method(self) -> int:
            """A method that returns 42"""
            return 42

        @utils.memoize
        def a_property(self) -> int:
            """
            A property that calls a_method and caches the result
            """
            return self.a_method()

    @patch.object(TestClass, 'a_method')
    def test_memoize(self, mock_method: Any) -> None:
        """
        Method to test that the memoize function returns
        the expected result.
        The a_method should only get called once.
        """
        test_instance = self.TestClass()

        result1 = test_instance.a_property
        result2 = test_instance.a_property

        self.assertEqual(result1, 42)
        self.assertEqual(result2, 42)
        mock_method.assert_called_once()


if __name__ == "__main__":
    unittest.main()
