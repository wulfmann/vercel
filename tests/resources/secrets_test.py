from pathlib import Path
import json

from unittest import TestCase
from unittest.mock import patch, call
from tests.helpers.response import MockResponse

import vercel


class TestSecrets(TestCase):
    def setUp(self):
        vercel.api_token = "fake-api-token"
        vercel.team_id = "fake-team-id"

    def tearDown(self):
        vercel.api_token = None
        vercel.team_id = None

    @patch("requests.request")
    def test_delete_v2(self, mock_request):
        mock_v3_get = Path("tests/fixtures/responses/secrets/v3/get.json")
        mock_v2_delete = Path("tests/fixtures/responses/secrets/v2/delete.json")

        mock_request.side_effect = [
            MockResponse(response=json.loads(mock_v3_get.open().read())),
            MockResponse(response=json.loads(mock_v2_delete.open().read())),
        ]

        secret = vercel.Secret.get("test-secret")
        secret.delete()

        assert [
            call(
                method="GET",
                url="https://api.vercel.com/v3/now/secrets/test-secret",
                headers={
                    "Content-Type": "application/json",
                    "Authorization": "Bearer fake-api-token",
                },
                params={"teamId": "fake-team-id"},
            ),
            call(
                method="DELETE",
                url="https://api.vercel.com/v2/now/secrets/secret-id",
                headers={
                    "Content-Type": "application/json",
                    "Authorization": "Bearer fake-api-token",
                },
                params={"teamId": "fake-team-id"},
            ),
        ] == mock_request.mock_calls

    @patch("requests.request")
    def testupdate_name_v2(self, mock_request):
        mock_v3_get = Path("tests/fixtures/responses/secrets/v3/get.json")
        mock_v2_update_name = Path(
            "tests/fixtures/responses/secrets/v2/update_name.json"
        )

        mock_request.side_effect = [
            MockResponse(response=json.loads(mock_v3_get.open().read())),
            MockResponse(response=json.loads(mock_v2_update_name.open().read())),
        ]

        secret = vercel.Secret.get("test-secret")
        secret.update_name(name="new-name")

        assert [
            call(
                method="GET",
                url="https://api.vercel.com/v3/now/secrets/test-secret",
                headers={
                    "Content-Type": "application/json",
                    "Authorization": "Bearer fake-api-token",
                },
                params={"teamId": "fake-team-id"},
            ),
            call(
                method="PATCH",
                url="https://api.vercel.com/v2/now/secrets/secret-id",
                headers={
                    "Content-Type": "application/json",
                    "Authorization": "Bearer fake-api-token",
                },
                json={"name": "new-name"},
                params={"teamId": "fake-team-id"},
            ),
        ] == mock_request.mock_calls

    @patch("requests.request")
    def test_get_v3(self, mock_request):
        mock_v3_get = Path("tests/fixtures/responses/secrets/v3/get.json")
        mock_request.return_value = MockResponse(
            response=json.loads(mock_v3_get.open().read())
        )

        secret = vercel.Secret.get("test-secret")

        assert isinstance(secret, vercel.Secret)

        assert [
            call(
                method="GET",
                url="https://api.vercel.com/v3/now/secrets/test-secret",
                headers={
                    "Content-Type": "application/json",
                    "Authorization": "Bearer fake-api-token",
                },
                params={"teamId": "fake-team-id"},
            )
        ] == mock_request.mock_calls

    @patch("requests.request")
    def test_create_v2(self, mock_request):
        response = Path("tests/fixtures/responses/secrets/v2/create.json")
        mock_request.return_value = MockResponse(
            response=json.loads(response.open().read())
        )

        alias = vercel.Secret.create(name="my-secret", value="my-secret-value")

        assert isinstance(alias, vercel.Secret)

        assert [
            call(
                method="POST",
                url="https://api.vercel.com/v2/now/secrets",
                headers={
                    "Content-Type": "application/json",
                    "Authorization": "Bearer fake-api-token",
                },
                json={"name": "my-secret", "value": "my-secret-value"},
                params={"teamId": "fake-team-id"},
            )
        ] == mock_request.mock_calls

    @patch("requests.request")
    def test_list_secrets_v3(self, mock_request):
        mock_v3_list_one = json.loads(
            Path("tests/fixtures/responses/secrets/v3/list_1.json").open().read()
        )
        mock_v3_list_two = json.loads(
            Path("tests/fixtures/responses/secrets/v3/list_2.json").open().read()
        )
        mock_v3_list_three = json.loads(
            Path("tests/fixtures/responses/secrets/v3/list_3.json").open().read()
        )

        mock_request.side_effect = [
            MockResponse(mock_v3_list_one),
            MockResponse(mock_v3_list_two),
            MockResponse(mock_v3_list_three),
        ]

        secrets = vercel.Secret.list_all()

        assert len(secrets) == 6

        assert mock_request.mock_calls == [
            call(url='https://api.vercel.com/v3/now/secrets', method='GET', headers={'Content-Type': 'application/json', 'Authorization': 'Bearer fake-api-token'}, params={'teamId': 'fake-team-id'}),
            call(url='https://api.vercel.com/v3/now/secrets', method='GET', headers={'Content-Type': 'application/json', 'Authorization': 'Bearer fake-api-token'}, params={'teamId': 'fake-team-id', 'since': 1472684630000}),
            call(url='https://api.vercel.com/v3/now/secrets', method='GET', headers={'Content-Type': 'application/json', 'Authorization': 'Bearer fake-api-token'}, params={'teamId': 'fake-team-id', 'since': 1472684630001})
        ]
