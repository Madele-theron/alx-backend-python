#!/usr/bin/env python3
"""A module ...  """
import unittest
from unittest.mock import patch
from parameterized import parameterized
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """Test case for the class GithubOrgClient"""

    @parameterized.expand([
        ("google"),
        ("abc"),
    ])
    @patch('client.get_json')
    def test_org(self, org_name: str, mock: unittest.mock.patch):
        """Test that GithubOrgClient.org returns the correct value. """
        test_client = GithubOrgClient(org_name)
        # call org method and store in result
        result = test_client.org

        self.assertEqual(result, mock.return_value)
        mock.assert_called_once_with(f"https://api.github.com/orgs/{org_name}")


if __name__ == "__main__":
    unittest.main()
