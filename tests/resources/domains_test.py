from pathlib import Path
import json

from unittest import TestCase
from unittest.mock import patch, call
from tests.helpers.response import MockResponse

import vercel


class TestDomains(TestCase):
    def setUp(self):
        vercel.api_key = "fake-api-key"
        vercel.team_id = "fake-team-id"

    def tearDown(self):
        vercel.api_key = None
        vercel.team_id = None

    @patch("requests.request")
    def test_get_dns_record_v2(self, mock_request):
        mock_v4_get = Path("tests/fixtures/responses/domains/v4/get.json")

        mock_request.side_effect = [
            MockResponse(response=json.loads(mock_v4_get.open().read())),
            MockResponse(response={"uid": "fake-record-id"}),
        ]

        domain = vercel.Domain.get("example.com")
        record = domain.get_dns_record("fake-record-id")

        assert isinstance(record, vercel.DnsRecord)
        assert record.domain_name == "example.com"
        assert record.id == "fake-record-id"

        assert [
            call(
                method="GET",
                url="https://api.vercel.com/v4/domains/example.com",
                headers={
                    "Content-Type": "application/json",
                    "Authorization": "Bearer fake-api-key",
                },
                params={"teamId": "fake-team-id"},
            )
        ] == mock_request.mock_calls

    @patch("requests.request")
    def test_list_all_v5(self, mock_request):
        mock_v5_list_one = json.loads(
            Path("tests/fixtures/responses/domains/v5/list_1.json").open().read()
        )
        mock_v5_list_two = json.loads(
            Path("tests/fixtures/responses/domains/v5/list_2.json").open().read()
        )
        mock_v5_list_three = json.loads(
            Path("tests/fixtures/responses/domains/v5/list_3.json").open().read()
        )

        mock_request.side_effect = [
            MockResponse(mock_v5_list_one),
            MockResponse(mock_v5_list_two),
            MockResponse(mock_v5_list_three),
        ]

        domains = vercel.Domain.list_all()

        assert [
            {
                "id": "EmTbe5CEJyTk2yVAHBUWy4A3sRusca3GCwRjTC1bpeVnt1",
                "name": "example.com",
                "serviceType": "external",
                "nsVerifiedAt": None,
                "txtVerifiedAt": None,
                "cdnEnabled": False,
                "createdAt": 1544658552174,
                "boughtAt": None,
                "verificationRecord": "YMc9dEJKbAncYtTqSH8dp1j5NXycfEzyjkzBJ3m3UGwR43",
                "verified": True,
                "nameservers": ["ns1.nameserver.net", "ns2.nameserver.net"],
                "intendedNameservers": [
                    "a.zeit-world.net",
                    "b.zeit-world.co.uk",
                    "e.zeit-world.org",
                    "f.zeit-world.com",
                ],
                "creator": {
                    "id": "ZspSRT4ljIEEmMHgoDwKWDei",
                    "username": "zeit_user",
                    "email": "demo@example.com",
                },
            },
            {
                "id": "EmTbe5CEJyTk2yVAHBUWy4A3sRusca3GCwRjTC1bpeVnt1",
                "name": "example.com",
                "serviceType": "external",
                "nsVerifiedAt": None,
                "txtVerifiedAt": None,
                "cdnEnabled": False,
                "createdAt": 1544658552174,
                "boughtAt": None,
                "verificationRecord": "YMc9dEJKbAncYtTqSH8dp1j5NXycfEzyjkzBJ3m3UGwR43",
                "verified": True,
                "nameservers": ["ns1.nameserver.net", "ns2.nameserver.net"],
                "intendedNameservers": [
                    "a.zeit-world.net",
                    "b.zeit-world.co.uk",
                    "e.zeit-world.org",
                    "f.zeit-world.com",
                ],
                "creator": {
                    "id": "ZspSRT4ljIEEmMHgoDwKWDei",
                    "username": "zeit_user",
                    "email": "demo@example.com",
                },
            },
            {
                "id": "EmTbe5CEJyTk2yVAHBUWy4A3sRusca3GCwRjTC1bpeVnt1",
                "name": "example.com",
                "serviceType": "external",
                "nsVerifiedAt": None,
                "txtVerifiedAt": None,
                "cdnEnabled": False,
                "createdAt": 1544658552174,
                "boughtAt": None,
                "verificationRecord": "YMc9dEJKbAncYtTqSH8dp1j5NXycfEzyjkzBJ3m3UGwR43",
                "verified": True,
                "nameservers": ["ns1.nameserver.net", "ns2.nameserver.net"],
                "intendedNameservers": [
                    "a.zeit-world.net",
                    "b.zeit-world.co.uk",
                    "e.zeit-world.org",
                    "f.zeit-world.com",
                ],
                "creator": {
                    "id": "ZspSRT4ljIEEmMHgoDwKWDei",
                    "username": "zeit_user",
                    "email": "demo@example.com",
                },
            },
        ] == domains

    @patch("requests.request")
    def test_create_v4(self, mock_request):
        mock_v4_create = Path("tests/fixtures/responses/domains/v4/create.json")
        mock_request.return_value = MockResponse(
            response=json.loads(mock_v4_create.open().read())
        )

        domain = vercel.Domain.create("example.com")

        assert isinstance(domain, vercel.Domain)

        assert domain.name == "example.com"
        assert domain.id == "domain-id"
        assert domain.service_type == "external"
        assert domain.ns_verified_at == None
        assert domain.txt_verified_at == None
        assert domain.cdn_enabled == False
        assert domain.created_at == 1544658552174
        assert domain.bought_at == None
        assert domain.transferred_at == None
        assert domain.verification_record == "verification-id"
        assert domain.verified == True
        assert domain.nameservers == ["ns1.nameserver.net", "ns2.nameserver.net"]

        assert domain.intended_nameservers == [
            "a.zeit-world.net",
            "b.zeit-world.co.uk",
            "e.zeit-world.org",
            "f.zeit-world.com",
        ]

        creator = domain.creator
        assert isinstance(creator, vercel.Creator)

        assert creator.id == "creator-id"
        assert creator.username == "zeit_user"
        assert creator.email == "demo@example.com"

        assert [
            call(
                method="POST",
                url="https://api.vercel.com/v4/domains",
                headers={
                    "Content-Type": "application/json",
                    "Authorization": "Bearer fake-api-key",
                },
                params={"teamId": "fake-team-id"},
                json={"name": "example.com"},
            )
        ] == mock_request.mock_calls

    @patch("requests.request")
    def test_get_v4(self, mock_request):
        mock_v4_get = Path("tests/fixtures/responses/domains/v4/get.json")
        mock_request.return_value = MockResponse(
            response=json.loads(mock_v4_get.open().read())
        )

        domain = vercel.Domain.get("example.com")

        assert isinstance(domain, vercel.Domain)

        assert domain.name == "example.com"
        assert domain.id == "domain-id"
        assert domain.service_type == "external"
        assert domain.ns_verified_at == None
        assert domain.txt_verified_at == None
        assert domain.cdn_enabled == False
        assert domain.created_at == 1544658552174
        assert domain.bought_at == None
        assert domain.transferred_at == None
        assert domain.verification_record == "verification-id"
        assert domain.verified == False
        assert domain.nameservers == ["ns1.nameserver.net", "ns2.nameserver.net"]

        assert domain.intended_nameservers == [
            "a.zeit-world.co.uk",
            "c.zeit-world.org",
            "d.zeit-world.com",
            "f.zeit-world.net",
        ]

        creator = domain.creator
        assert isinstance(creator, vercel.Creator)

        assert creator.id == "creator-id"
        assert creator.username == "zeit_user"
        assert creator.email == "demo@example.com"

        assert domain.suffix == False
        assert domain.aliases == []
        assert domain.certs == []

        assert [
            call(
                method="GET",
                url="https://api.vercel.com/v4/domains/example.com",
                headers={
                    "Content-Type": "application/json",
                    "Authorization": "Bearer fake-api-key",
                },
                params={"teamId": "fake-team-id"},
            )
        ] == mock_request.mock_calls

    @patch("requests.request")
    def test_delete_v4(self, mock_request):
        mock_v4_get = Path("tests/fixtures/responses/domains/v4/get.json")
        mock_request.side_effect = [
            MockResponse(response=json.loads(mock_v4_get.open().read())),
            MockResponse(response={}, status_code=204),
        ]

        domain = vercel.Domain.get("example.com")
        domain.delete()

        assert [
            call(
                method="GET",
                url="https://api.vercel.com/v4/domains/example.com",
                headers={
                    "Content-Type": "application/json",
                    "Authorization": "Bearer fake-api-key",
                },
                params={"teamId": "fake-team-id"},
            ),
            call(
                method="DELETE",
                url="https://api.vercel.com/v4/domains/example.com",
                headers={
                    "Content-Type": "application/json",
                    "Authorization": "Bearer fake-api-key",
                },
                params={"teamId": "fake-team-id"},
            ),
        ] == mock_request.mock_calls

    @patch("requests.request")
    def test_create_dns_record_v2(self, mock_request):
        mock_v4_get = Path("tests/fixtures/responses/domains/v4/get.json")

        mock_request.side_effect = [
            MockResponse(response=json.loads(mock_v4_get.open().read())),
            MockResponse(response={"uid": "fake-record-id"}),
        ]

        domain = vercel.Domain.get("example.com")
        record = domain.create_dns_record(name="", type="TXT", value="something")

        assert isinstance(record, vercel.DnsRecord)

        assert [
            call(
                method="GET",
                url="https://api.vercel.com/v4/domains/example.com",
                headers={
                    "Content-Type": "application/json",
                    "Authorization": "Bearer fake-api-key",
                },
                params={"teamId": "fake-team-id"},
            ),
            call(
                method="POST",
                url="https://api.vercel.com/v2/domains/example.com/records",
                headers={
                    "Content-Type": "application/json",
                    "Authorization": "Bearer fake-api-key",
                },
                params={"teamId": "fake-team-id"},
                json={"name": "", "type": "TXT", "value": "something"},
            ),
        ] == mock_request.mock_calls

    @patch("requests.request")
    def test_check_availability_v4(self, mock_request):
        mock_v4_check_availability = Path(
            "tests/fixtures/responses/domains/v4/check_availability.json"
        )

        mock_request.side_effect = [
            MockResponse(response=json.loads(mock_v4_check_availability.open().read()))
        ]

        vercel.Domain.check_availability("test.com")

        assert [
            call(
                method="GET",
                url="https://api.vercel.com/v4/domains/status",
                headers={
                    "Content-Type": "application/json",
                    "Authorization": "Bearer fake-api-key",
                },
                params={"teamId": "fake-team-id", "name": "test.com"},
            )
        ] == mock_request.mock_calls

    @patch("requests.request")
    def test_check_price_v4(self, mock_request):
        mock_v4_check_price = Path(
            "tests/fixtures/responses/domains/v4/check_price.json"
        )

        mock_request.side_effect = [
            MockResponse(response=json.loads(mock_v4_check_price.open().read()))
        ]

        vercel.Domain.check_price("test.com")

        assert [
            call(
                method="GET",
                url="https://api.vercel.com/v4/domains/price",
                headers={
                    "Content-Type": "application/json",
                    "Authorization": "Bearer fake-api-key",
                },
                params={"teamId": "fake-team-id", "name": "test.com"},
            )
        ] == mock_request.mock_calls

    @patch("requests.request")
    def test_purchase_v4(self, mock_request):
        mock_v4_check_price = Path(
            "tests/fixtures/responses/domains/v4/check_price.json"
        )
        mock_v4_purchase = Path("tests/fixtures/responses/domains/v4/purchase.json")

        mock_request.side_effect = [
            MockResponse(response=json.loads(mock_v4_check_price.open().read())),
            MockResponse(response=json.loads(mock_v4_purchase.open().read())),
        ]

        checked = vercel.Domain.check_price("test.com")
        checked.purchase()

        assert [
            call(
                method="GET",
                url="https://api.vercel.com/v4/domains/price",
                headers={
                    "Content-Type": "application/json",
                    "Authorization": "Bearer fake-api-key",
                },
                params={"teamId": "fake-team-id", "name": "test.com"},
            ),
            call(
                method="POST",
                url="https://api.vercel.com/v4/domains/buy",
                headers={
                    "Content-Type": "application/json",
                    "Authorization": "Bearer fake-api-key",
                },
                json={"name": "test.com", "expectedPrice": 17},
                params={"teamId": "fake-team-id"},
            ),
        ] == mock_request.mock_calls
