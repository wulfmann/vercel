from unittest import TestCase
from unittest.mock import patch, call
from tests.helpers.response import MockResponse

import vercel

class TestDomain(TestCase):

    def setUp(self):
        vercel.api_key = 'fake-api-key'
        vercel.team_id = 'fake-team-id'

    def tearDown(self):
        vercel.api_key = None
        vercel.team_id = None

    def test_get_dns_record(self):
        domain = vercel.Domain.get('test.com')
        record = domain.get_dns_record('fake-record-id')

        assert isinstance(record, vercel.DnsRecord)
        assert record.domain_name == 'test.com'
        assert record.id == 'fake-record-id'

    @patch('requests.request')
    def test_create_dns_record(self, mock_request):
        mock_request.return_value = MockResponse(response={
            'uid': 'fake-record-id'
        })

        domain = vercel.Domain.get('test.com')
        record = domain.create_dns_record(
            name='',
            type='TXT',
            value='something'
        )

        assert isinstance(record, vercel.DnsRecord)

        assert [
            call(
                method='POST',
                url='https://api.vercel.com/v2/domains/test.com/records',
                headers={
                    'Content-Type': 'application/json',
                    'Authorization': 'Bearer fake-api-key'
                },
                params={
                    'teamId': 'fake-team-id'
                },
                json={
                    'name': '',
                    'type': 'TXT',
                    'value': 'something'
                }
            )
        ] == mock_request.mock_calls
