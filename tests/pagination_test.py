from pathlib import Path
import json

from unittest import TestCase
from unittest.mock import patch, call
from tests.helpers.response import MockResponse

import vercel

class TestPagination(TestCase):

    def setUp(self):
        vercel.api_key = 'fake-api-key'

    def tearDown(self):
        vercel.api_key = None

    @patch('requests.get')
    def test_make_paginated_request(self, mock_request):
        mock_request.side_effect = [
            MockResponse({
                'domains': [
                    {
                        'id': 'domain-one'
                    }
                ],
                'pagination': {
                    'next': 'middle'
                }
            }),
            MockResponse({
                'domains': [
                    {
                        'id': 'domain-two'
                    }
                ],
                'pagination': {
                    'next': 'end'
                }
            }),
            MockResponse({
                'domains': [
                    {
                        'id': 'domain-three'
                    }
                ]
            })
        ]

        domains = vercel.Resource.make_paginated_request('/v2/domains', 'domains')
        
        assert [
            { 'id': 'domain-one' },
            { 'id': 'domain-two' },
            { 'id': 'domain-three' }
        ] == domains
        # assert mock_request.mock_calls == [
        #     call(
        #         method='GET',
        #         url='https://api.vercel.com/v2/domains',
        #         headers={
        #             'Content-Type': 'application/json',
        #             'Authorization': 'Bearer fake-api-key'
        #         }
        #     ),
        #     call(
        #         method='GET',
        #         url='https://api.vercel.com/v2/domains',
        #         headers={
        #             'Content-Type': 'application/json',
        #             'Authorization': 'Bearer fake-api-key'
        #         },
        #         params={
        #             'since': 'middle'
        #         }
        #     ),
        #     call(
        #         method='GET',
        #         url='https://api.vercel.com/v2/domains',
        #         headers={
        #             'Content-Type': 'application/json',
        #             'Authorization': 'Bearer fake-api-key'
        #         },
        #         params={
        #             'since': 'end'
        #         }
        #     )
        # ]
        