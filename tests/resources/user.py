from unittest import TestCase
from unittest.mock import patch, call
from tests.helpers.response import MockResponse

import vercel

class UserTest(TestCase):

    def setUp(self):
        vercel.api_key = 'fake-api-key'
        vercel.team_id = 'fake-team-id'

    def tearDown(self):
        vercel.api_key = None
        vercel.team_id = None

    @patch('requests.request')
    def test_get_user(self, mock_request):
        mock_request.return_value = MockResponse(response={
            'uid': 'fake-record-id'
        })

        record = vercel.User.get()

        assert isinstance(record, vercel.User)

        assert [
            call(
                method='GET',
                url='https://api.vercel.com/www/user',
                headers={
                    'Content-Type': 'application/json',
                    'Authorization': 'Bearer fake-api-key'
                }
            )
        ] == mock_request.mock_calls
