from pathlib import Path
import json

from unittest import TestCase
from unittest.mock import patch, call
from tests.helpers.response import MockResponse

import vercel


class TestAliases(TestCase):
    def setUp(self):
        vercel.api_token = "fake-api-token"
        vercel.team_id = "fake-team-id"

    def tearDown(self):
        vercel.api_token = None
        vercel.team_id = None

    @patch("requests.request")
    def test_delete_v2(self, mock_request):
        mock_v2_get = Path("tests/fixtures/responses/aliases/v2/get.json")
        mock_request.return_value = MockResponse(
            response=json.loads(mock_v2_get.open().read())
        )

        team = vercel.Alias.get("test-alias")
        team.delete()

        assert [
            call(
                method="GET",
                url="https://api.vercel.com/v2/now/aliases/test-alias",
                headers={
                    "Content-Type": "application/json",
                    "Authorization": "Bearer fake-api-token",
                },
                params={"teamId": "fake-team-id"},
            ),
            call(
                method="DELETE",
                url="https://api.vercel.com/v2/now/aliases/alias-id",
                headers={
                    "Content-Type": "application/json",
                    "Authorization": "Bearer fake-api-token",
                },
                params={"teamId": "fake-team-id"},
            ),
        ] == mock_request.mock_calls

    @patch("requests.request")
    def test_get_v2(self, mock_request):
        mock_v2_get = Path("tests/fixtures/responses/aliases/v2/get.json")
        mock_request.return_value = MockResponse(
            response=json.loads(mock_v2_get.open().read())
        )

        alias = vercel.Alias.get("test-alias")

        assert isinstance(alias, vercel.Alias)

        assert [
            call(
                method="GET",
                url="https://api.vercel.com/v2/now/aliases/test-alias",
                headers={
                    "Content-Type": "application/json",
                    "Authorization": "Bearer fake-api-token",
                },
                params={"teamId": "fake-team-id"},
            )
        ] == mock_request.mock_calls

    @patch("requests.request")
    def test_list_aliases_v3(self, mock_request):
        mock_v3_list_one = json.loads(
            Path("tests/fixtures/responses/aliases/v3/list_1.json").open().read()
        )
        mock_v3_list_two = json.loads(
            Path("tests/fixtures/responses/aliases/v3/list_2.json").open().read()
        )
        mock_v3_list_three = json.loads(
            Path("tests/fixtures/responses/aliases/v3/list_3.json").open().read()
        )
        mock_request.side_effect = [
            MockResponse(mock_v3_list_one),
            MockResponse(mock_v3_list_two),
            MockResponse(mock_v3_list_three),
        ]

        aliases = vercel.Alias.list_all()

        assert len(aliases) == 6

        assert mock_request.mock_calls == [
            call(
                url="https://api.vercel.com/v3/now/aliases",
                method="GET",
                headers={
                    "Content-Type": "application/json",
                    "Authorization": "Bearer fake-api-token",
                },
                params={"teamId": "fake-team-id"},
            ),
            call(
                url="https://api.vercel.com/v3/now/aliases",
                method="GET",
                headers={
                    "Content-Type": "application/json",
                    "Authorization": "Bearer fake-api-token",
                },
                params={"teamId": "fake-team-id", "since": 1464807790001},
            ),
            call(
                url="https://api.vercel.com/v3/now/aliases",
                method="GET",
                headers={
                    "Content-Type": "application/json",
                    "Authorization": "Bearer fake-api-token",
                },
                params={"teamId": "fake-team-id", "since": 1464807790002},
            ),
        ]

    @patch("requests.request")
    def test_list_aliases_with_project_filter_v3(self, mock_request):
        mock_v3_list_one = json.loads(
            Path("tests/fixtures/responses/aliases/v3/list_1.json").open().read()
        )
        mock_v3_list_two = json.loads(
            Path("tests/fixtures/responses/aliases/v3/list_2.json").open().read()
        )
        mock_v3_list_three = json.loads(
            Path("tests/fixtures/responses/aliases/v3/list_3.json").open().read()
        )
        mock_request.side_effect = [
            MockResponse(mock_v3_list_one),
            MockResponse(mock_v3_list_two),
            MockResponse(mock_v3_list_three),
        ]

        aliases = vercel.Alias.list_all(project_id="test-project")

        assert len(aliases) == 6

        assert mock_request.mock_calls == [
            call(
                url="https://api.vercel.com/v3/now/aliases",
                method="GET",
                headers={
                    "Content-Type": "application/json",
                    "Authorization": "Bearer fake-api-token",
                },
                params={"teamId": "fake-team-id", "projectId": "test-project"},
            ),
            call(
                url="https://api.vercel.com/v3/now/aliases",
                method="GET",
                headers={
                    "Content-Type": "application/json",
                    "Authorization": "Bearer fake-api-token",
                },
                params={
                    "teamId": "fake-team-id",
                    "projectId": "test-project",
                    "since": 1464807790001,
                },
            ),
            call(
                url="https://api.vercel.com/v3/now/aliases",
                method="GET",
                headers={
                    "Content-Type": "application/json",
                    "Authorization": "Bearer fake-api-token",
                },
                params={
                    "teamId": "fake-team-id",
                    "projectId": "test-project",
                    "since": 1464807790002,
                },
            ),
        ]
