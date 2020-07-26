from pathlib import Path
import json

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

    @patch('requests.request')
    def test_get_dns_record_v2(self, mock_request):
        mock_v4_get = Path('tests/fixtures/responses/domains/v4/get.json')

        mock_request.side_effect = [
            MockResponse(response=json.loads(mock_v4_get.open().read())),
            MockResponse(response={
                'uid': 'fake-record-id'
            })
        ]

        domain = vercel.Domain.get('example.com')
        record = domain.get_dns_record('fake-record-id')

        assert isinstance(record, vercel.DnsRecord)
        assert record.domain_name == 'example.com'
        assert record.id == 'fake-record-id'

        assert [
            call(
                method='GET',
                url='https://api.vercel.com/v4/domains/example.com',
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
    def test_create_v4(self, mock_request):
        mock_v4_create = Path('tests/fixtures/responses/domains/v4/create.json')
        mock_request.return_value = MockResponse(response=json.loads(mock_v4_create.open().read()))

        domain = vercel.Domain.create('example.com')

        assert isinstance(domain, vercel.Domain)
        
        assert domain.name == 'example.com'
        assert domain.id == 'domain-id'
        assert domain.service_type == 'external'
        assert domain.ns_verified_at == None
        assert domain.txt_verified_at == None
        assert domain.cdn_enabled == False
        assert domain.created_at == 1544658552174
        assert domain.bought_at == None
        assert domain.transferred_at == None
        assert domain.verification_record == 'verification-id'
        assert domain.verified == True
        assert domain.nameservers == [
          "ns1.nameserver.net",
          "ns2.nameserver.net"
        ]

        assert domain.intended_nameservers == [
          "a.zeit-world.net",
          "b.zeit-world.co.uk",
          "e.zeit-world.org",
          "f.zeit-world.com"
        ]

        creator = domain.creator
        assert isinstance(creator, vercel.Creator)
        
        assert creator.id == 'creator-id'
        assert creator.username == 'zeit_user'
        assert creator.email == 'demo@example.com'
        
        
        assert [
            call(
                method='POST',
                url='https://api.vercel.com/v4/domains',
                headers={
                    'Content-Type': 'application/json',
                    'Authorization': 'Bearer fake-api-key'
                },
                params={
                    'teamId': 'fake-team-id'
                },
                json={
                    'name': 'example.com'
                }
            )
        ] == mock_request.mock_calls

    @patch('requests.request')
    def test_get_v4(self, mock_request):
        mock_v4_get = Path('tests/fixtures/responses/domains/v4/get.json')
        mock_request.return_value = MockResponse(response=json.loads(mock_v4_get.open().read()))

        domain = vercel.Domain.get('example.com')

        assert isinstance(domain, vercel.Domain)
        
        assert domain.name == 'example.com'
        assert domain.id == 'domain-id'
        assert domain.service_type == 'external'
        assert domain.ns_verified_at == None
        assert domain.txt_verified_at == None
        assert domain.cdn_enabled == False
        assert domain.created_at == 1544658552174
        assert domain.bought_at == None
        assert domain.transferred_at == None
        assert domain.verification_record == 'verification-id'
        assert domain.verified == False
        assert domain.nameservers == [
          "ns1.nameserver.net",
          "ns2.nameserver.net"
        ]

        assert domain.intended_nameservers == [
          "a.zeit-world.co.uk",
            "c.zeit-world.org",
            "d.zeit-world.com",
            "f.zeit-world.net"
        ]

        creator = domain.creator
        assert isinstance(creator, vercel.Creator)
        
        assert creator.id == 'creator-id'
        assert creator.username == 'zeit_user'
        assert creator.email == 'demo@example.com'
        
        assert domain.suffix == False
        assert domain.aliases == []
        assert domain.certs == []
        
        
        assert [
            call(
                method='GET',
                url='https://api.vercel.com/v4/domains/example.com',
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
    def test_delete_v4(self, mock_request):
        mock_v4_get = Path('tests/fixtures/responses/domains/v4/get.json')
        mock_request.side_effect = [
            MockResponse(response=json.loads(mock_v4_get.open().read())),
            MockResponse(response={}, status_code=204)
        ]

        domain = vercel.Domain.get('example.com')
        domain.delete()
        
        assert [
            call(
                method='GET',
                url='https://api.vercel.com/v4/domains/example.com',
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
                url='https://api.vercel.com/v4/domains/example.com',
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
    def test_create_dns_record_v2(self, mock_request):
        mock_v4_get = Path('tests/fixtures/responses/domains/v4/get.json')

        mock_request.side_effect = [
            MockResponse(response=json.loads(mock_v4_get.open().read())),
            MockResponse(response={
                'uid': 'fake-record-id'
            })
        ]

        domain = vercel.Domain.get('example.com')
        record = domain.create_dns_record(
            name='',
            type='TXT',
            value='something'
        )

        assert isinstance(record, vercel.DnsRecord)

        assert [
            call(
                method='GET',
                url='https://api.vercel.com/v4/domains/example.com',
                headers={
                    'Content-Type': 'application/json',
                    'Authorization': 'Bearer fake-api-key'
                },
                params={
                    'teamId': 'fake-team-id'
                }
            ),
            call(
                method='POST',
                url='https://api.vercel.com/v2/domains/example.com/records',
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
