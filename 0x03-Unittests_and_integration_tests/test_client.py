#!/usr/bin/env python3
"""A module ...  """
import unittest
from unittest.mock import patch, PropertyMock
from parameterized import parameterized, parameterized_class
from client import GithubOrgClient
from fixtures import TEST_PAYLOAD


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
            mock.return_value = {"repos_url": "test"}
            test_client = GithubOrgClient('test')
            public_repos_url = test_client._public_repos_url
            expected_url = mock.return_value['repos_url']
            self.assertEqual(public_repos_url, expected_url)

    @patch('client.get_json')
    def test_public_repos(self, mock_get_json):
        """Test the public_repos method of GithubOrgClient."""

        mock_payload = [{"name": "Google"}, {"name": "Facebook"}]
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
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False)
    ])
    def test_has_license(self, repo, license_key, expected_result):
        """to unit-test GithubOrgClient.has_license."""

        result = GithubOrgClient.has_license(repo, license_key)

        self.assertEqual(result, expected_result)


@parameterized_class(
    ("org_payload", "repos_payload", "expected_repos", "apache2_repos"),
    TEST_PAYLOAD
)
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """ Class for Integration test of fixtures """

    @classmethod
    def setUpClass(cls):
        """Set up the test class by patching requests.get."""

        payload = {
            'return_value.json.side_effect':
                [
                    cls.org_payload, cls.repos_payload,
                    cls.org_payload, cls.repos_payload
                ]

        }
        cls.get_patcher = patch('requests.get', **payload)
        cls.mock = cls.get_patcher.start()

    def test_public_repos(self):
        """Test the public_repos method of GithubOrgClient"""
        test_client = GithubOrgClient("google")
        self.assertEqual(test_client.org, self.org_payload)
        self.assertEqual(test_client.repos_payload, self.repos_payload)
        self.assertEqual(test_client.public_repos(), self.expected_repos)
        self.assertEqual(test_client.public_repos('XLICENSE'), [])
        self.mock.assert_called()

    def test_public_repos_with_license(self):
        "Test for public repos with License"
        test_client = GithubOrgClient("google")

        self.assertEqual(test_client.public_repos(), self.expected_repos)
        self.assertEqual(test_client.public_repos("XLICENSE"), [])
        self.assertEqual(test_client.public_repos(
            "apache-2.0"), self.apache2_repos)
        self.mock.assert_called()

    @classmethod
    def tearDownClass(cls):
        """Tear down test class, stop patcher"""
        cls.get_patcher.stop()


if __name__ == "__main__":
    unittest.main()
