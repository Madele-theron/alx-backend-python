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

        # Patch the org property and mock its return value
        with patch.object(
            GithubOrgClient, "org", new_callable=PropertyMock
                ) as mock:
            mock.return_value = {"repos_url": "test_url"}

            test_client = GithubOrgClient('test_url')

            public_repos_url = test_client._public_repos_url
            expected_url = mock.return_value['repos_url']

            self.assertEqual(public_repos_url, expected_url)

    @patch('client.get_json')
    def test_public_repos(self, mock_get_json):
        """Test the public_repos method of GithubOrgClient."""

        mock_payload = [{"name": "repo1"}, {"name": "repo2"}]
        mock_get_json.return_value = mock_payload

        with patch(
            'clien.GithubOrgClient._public_repos_url',
                new_callable=PropertyMock) as mock:
            mock.return_value = "https://api.github.com/orgs/testorg/repos"
            test_client = GithubOrgClient('test')
            repos = test_client.public_repos()

            expected_repos = ["repo1", "repo2"]
            self.assertEqual(repos, expected_repos)

            mock.assert_called_once()
            mock_get_json.assert_called_once_with(
                "https://api.github.com/orgs/testorg/repos")

    @parameterized.expand([
        # (repo, license_key)
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False),
    ])
    def test_has_license(
        self,
        repo: dict,
        license_key: str,
        expected_result: bool
    ) -> None:
        """to unit-test GithubOrgClient.has_license."""
        test_client = GithubOrgClient("test")

        result = test_client.has_license(repo, license_key)

        self.assertEqual(result, expected_result)


if __name__ == "__main__":
    unittest.main()
