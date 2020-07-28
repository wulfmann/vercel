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
