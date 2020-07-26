from pathlib import Path
import json

from unittest import TestCase
from unittest.mock import patch, call
from tests.helpers.response import MockResponse

import vercel

class TestCertificates(TestCase):

    def setUp(self):
        vercel.api_key = 'fake-api-key'
        vercel.team_id = 'fake-team-id'

    def tearDown(self):
        vercel.api_key = None
        vercel.team_id = None
        
    @patch('requests.request')
    def test_delete_v3(self, mock_request):
        mock_v2_get = Path('tests/fixtures/responses/certificates/v3/get.json')
        mock_request.return_value = MockResponse(response=json.loads(mock_v3_get.open().read()))

        team = vercel.Certificate.get('certificate-id')
        team.delete()
        
        assert [
            call(
                method='GET',
                url='https://api.vercel.com/v3/now/certs/certificate-id',
                headers={
                    'Content-Type': 'application/json',
                    'Authorization': 'Bearer fake-api-key'
                },
                params={
                    'teamId': 'fake-team-id'
                }
            ),
            call(
                method='DELETE',
                url='https://api.vercel.com/v3/now/certs/certificate-id',
                headers={
                    'Content-Type': 'application/json',
                    'Authorization': 'Bearer fake-api-key'
                },
                params={
                    'teamId': 'fake-team-id'
                }
            )
        ] == mock_request.mock_calls
        
    @patch('requests.request')
    def test_get_v3(self, mock_request):
        mock_v3_get = Path('tests/fixtures/responses/certificates/v3/get.json')
        mock_request.return_value = MockResponse(response=json.loads(mock_v3_get.open().read()))

        alias = vercel.Certificate.get('certificate-id')

        assert isinstance(alias, vercel.Certificate)
        
        assert [
            call(
                method='GET',
                url='https://api.vercel.com/v3/now/certs/certificate-id',
                headers={
                    'Content-Type': 'application/json',
                    'Authorization': 'Bearer fake-api-key'
                },
                params={
                    'teamId': 'fake-team-id'
                }
            )
        ] == mock_request.mock_calls