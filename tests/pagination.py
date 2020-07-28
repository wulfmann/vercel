from pathlib import Path
import json

from unittest import TestCase
from unittest.mock import patch, call
from tests.helpers.response import MockResponse

import vercel


class TestPagination(TestCase):
    def setUp(self):
        vercel.api_key = "fake-api-key"
        vercel.team_id = "fake-team-id"

    def tearDown(self):
        vercel.api_key = None
        vercel.team_id = None

    def test_make_paginated_call(self):
        with patch('requests.request') as mock_request:
            mock_request.side_effect = [
                MockResponse({ 'domains': [{ 'id': 'domain-1' }], 'pagination': { 'next': '1' }}),
                MockResponse({ 'domains': [{ 'id': 'domain-2' }], 'pagination': { 'next': '2' }}),
                MockResponse({ 'domains': [{ 'id': 'domain-3' }]})
            ]

            result = vercel.Resource.make_paginated_request('/test', 'domains')

            assert [
                {'id': 'domain-1'},
                {'id': 'domain-2'},
                {'id': 'domain-3'}
            ] == result

            assert mock_request.mock_calls == [
                call(url='https://api.vercel.com/test', method='GET', headers={'Content-Type': 'application/json', 'Authorization': 'Bearer fake-api-key'}, params={'teamId': 'fake-team-id'}),
                call(url='https://api.vercel.com/test', method='GET', headers={'Content-Type': 'application/json', 'Authorization': 'Bearer fake-api-key'}, params={'teamId': 'fake-team-id', 'since': '1'}),
                call(url='https://api.vercel.com/test', method='GET', headers={'Content-Type': 'application/json', 'Authorization': 'Bearer fake-api-key'}, params={'teamId': 'fake-team-id', 'since': '2'})
            ]
