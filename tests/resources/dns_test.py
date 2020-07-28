from pathlib import Path
import json

from unittest import TestCase
from unittest.mock import patch, call
from tests.helpers.response import MockResponse

import vercel


class TestDns(TestCase):
    def setUp(self):
        vercel.api_token = "fake-api-token"
        vercel.team_id = "fake-team-id"

    def tearDown(self):
        vercel.api_token = None
        vercel.team_id = None

    def test_get_record(self):
        record = vercel.DnsRecord.get("test.com", "fake-record-id")

        assert isinstance(record, vercel.DnsRecord)
        assert record.domain_name == "test.com"
        assert record.id == "fake-record-id"

    @patch("requests.request")
    def test_create_record(self, mock_request):
        mock_request.return_value = MockResponse(response={"uid": "fake-record-id"})

        record = vercel.DnsRecord.create(
            domain_name="test.com", name="", type="TXT", value="something"
        )

        assert isinstance(record, vercel.DnsRecord)

        assert [
            call(
                method="POST",
                url="https://api.vercel.com/v2/domains/test.com/records",
                headers={
                    "Content-Type": "application/json",
                    "Authorization": "Bearer fake-api-token",
                },
                params={"teamId": "fake-team-id"},
                json={"name": "", "type": "TXT", "value": "something"},
            )
        ] == mock_request.mock_calls

    @patch("requests.request")
    def test_delete_record(self, mock_request):
        mock_request.return_value = MockResponse(response={})

        record = vercel.DnsRecord.delete("test.com", "fake-record-id")

        assert [
            call(
                method="DELETE",
                url="https://api.vercel.com/v2/domains/test.com/records/fake-record-id",
                headers={
                    "Content-Type": "application/json",
                    "Authorization": "Bearer fake-api-token",
                },
                params={"teamId": "fake-team-id"},
            )
        ] == mock_request.mock_calls

    @patch("requests.request")
    def test_list_records_v4(self, mock_request):
        mock_v4_list_one = json.loads(
            Path("tests/fixtures/responses/dns/v4/list_1.json").open().read()
        )
        mock_v4_list_two = json.loads(
            Path("tests/fixtures/responses/dns/v4/list_2.json").open().read()
        )
        mock_v4_list_three = json.loads(
            Path("tests/fixtures/responses/dns/v4/list_3.json").open().read()
        )

        mock_request.side_effect = [
            MockResponse(mock_v4_list_one),
            MockResponse(mock_v4_list_two),
            MockResponse(mock_v4_list_three),
        ]

        records = vercel.DnsRecord.list_records('my-domain')

        assert len(records) == 6

        assert mock_request.mock_calls == [
            call(url='https://api.vercel.com/v4/domains/my-domain/records', method='GET', headers={'Content-Type': 'application/json', 'Authorization': 'Bearer fake-api-token'}, params={'teamId': 'fake-team-id'}),
            call(url='https://api.vercel.com/v4/domains/my-domain/records', method='GET', headers={'Content-Type': 'application/json', 'Authorization': 'Bearer fake-api-token'}, params={'teamId': 'fake-team-id', 'since': 1474631619961}),
            call(url='https://api.vercel.com/v4/domains/my-domain/records', method='GET', headers={'Content-Type': 'application/json', 'Authorization': 'Bearer fake-api-token'}, params={'teamId': 'fake-team-id', 'since': 1474631619962})
        ]
