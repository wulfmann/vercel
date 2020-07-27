from pathlib import Path
import json

from unittest import TestCase
from unittest.mock import patch, call
from tests.helpers.response import MockResponse

import vercel


class TestUser(TestCase):
    def setUp(self):
        vercel.api_key = "fake-api-key"
        vercel.team_id = "fake-team-id"

    def tearDown(self):
        vercel.api_key = None
        vercel.team_id = None

    @patch("requests.request")
    def test_get(self, mock_request):
        mock_get = Path("tests/fixtures/responses/user/get.json")
        mock_request.return_value = MockResponse(
            response=json.loads(mock_get.open().read())
        )

        user = vercel.User.get()

        assert [
            call(
                method="GET",
                url="https://api.vercel.com/www/user",
                headers={
                    "Content-Type": "application/json",
                    "Authorization": "Bearer fake-api-key",
                },
                params={"teamId": "fake-team-id"},
            )
        ] == mock_request.mock_calls
