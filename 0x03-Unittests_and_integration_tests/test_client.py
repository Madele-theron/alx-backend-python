#!/usr/bin/env python3
"""A module ...  """
import unittest
from unittest.mock import patch, PropertyMock
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

    def test_public_repos_url(self):
        """Test the GithubOrgClient._public_repos_url property"""
        # mock return value for 'org' property
        mock_payload = {"repos_url": "test_url"}

        # Patch the org property and mock its return value
        with patch.object(
            GithubOrgClient, "org", new_callable=PropertyMock
            ) as mock:
            mock.return_value = mock_payload

            test_client = GithubOrgClient("testorg")
            public_repos_url = test_client._public_repos_url

            expected_url = "https://api.github.com/orgs/testorg/repos"
            self.assertEqual(public_repos_url, expected_url)

if __name__ == "__main__":
    unittest.main()
