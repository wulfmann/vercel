from unittest import TestCase
from unittest.mock import patch, call
from tests.helpers.response import MockResponse

import vercel

class TestDns(TestCase):

    def setUp(self):
        vercel.api_key = 'fake-api-key'
        vercel.team_id = 'fake-team-id'

    def tearDown(self):
        vercel.api_key = None
        vercel.team_id = None

    @patch('requests.request')
    def test_create_record(self, mock_request):
        mock_request.return_value = MockResponse(response={
            'uid': 'fake-record-id'
        })
    
        record = vercel.DnsRecord.create(
            domain_name='test.com',
            name='',
            type='TXT',
            value='something'
        )

        assert isinstance(record, vercel.DnsRecord)

        assert [
            call(
                method='POST',
                url='https://api.vercel.com/v2/domains/test.com/records?teamId=fake-team-id',
                headers={
                    'Content-Type': 'application/json',
                    'Authorization': 'Bearer fake-api-key'
                },
                json={
                    'name': '',
                    'type': 'TXT',
                    'value': 'something',
                    'ttl': 60
                }
            )
        ] == mock_request.mock_calls

    @patch('requests.request')
    def test_delete_record(self, mock_request):
        mock_request.return_value = MockResponse(response={})

        record = vercel.DnsRecord.get('test.com', 'fake-record-id')
        record.delete()

        assert isinstance(record, vercel.DnsRecord)

        assert [
            call(
                method='DELETE',
                url='https://api.vercel.com/v2/domains/test.com/records/fake-record-id?teamId=fake-team-id',
                headers={
                    'Content-Type': 'application/json',
                    'Authorization': 'Bearer fake-api-key'
                }
            )
        ] == mock_request.mock_calls
