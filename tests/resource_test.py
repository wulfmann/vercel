from pathlib import Path
import json
import pytest
from unittest import TestCase
from unittest.mock import patch, call
from tests.helpers.response import MockResponse

import vercel

class TestResource(TestCase):
    def setUp(self):
        vercel.api_token = "fake-api-token"
        vercel.team_id = "fake-team-id"

    def tearDown(self):
        vercel.api_token = None
        vercel.team_id = None

    @patch('requests.request')
    def test_make_request(self, mock_request):
        mock_request.side_effect = [
            MockResponse({})
        ]

        result = vercel.Resource._make_request(
            url='/',
            method='GET',
            headers={
                'Content-Type': 'application-json'
            },
            params={
                'teamId': 'team-id'
            }
        )

        assert result == {}

        assert mock_request.mock_calls == [
            call(
                url='/',
                method='GET',
                headers={
                    'Content-Type': 'application-json'
                },
                params={
                    'teamId': 'team-id'
                }
            )
        ]

    @patch('requests.request')
    def test_make_request_raises_vercel_error(self, mock_request):
        mock_request.side_effect = [
            MockResponse({
                'error': {
                    'code': 'error_code',
                    'message': 'Error Message'
                }
            })
        ]

        with pytest.raises(vercel.exceptions.VercelError) as e:
            result = vercel.Resource._make_request(
                url='/',
                method='GET',
                headers={
                    'Content-Type': 'application-json'
                },
                params={
                    'teamId': 'team-id'
                }
            )

            assert e.code == 'error_code'
            assert e.message == 'Error Message'

        assert mock_request.mock_calls == [
            call(
                url='/',
                method='GET',
                headers={
                    'Content-Type': 'application-json'
                },
                params={
                    'teamId': 'team-id'
                }
            )
        ]

    @patch('requests.request')
    def test_make_request_handles_unexpected_error(self, mock_request):
        mock_request.side_effect = [
            Exception('other-exception')
        ]

        with pytest.raises(Exception) as e:
            result = vercel.Resource._make_request(
                url='/',
                method='GET',
                headers={
                    'Content-Type': 'application-json'
                },
                params={
                    'teamId': 'team-id'
                }
            )

            assert e == 'other-exception'

        assert mock_request.mock_calls == [
            call(
                url='/',
                method='GET',
                headers={
                    'Content-Type': 'application-json'
                },
                params={
                    'teamId': 'team-id'
                }
            )
        ]

    @patch('requests.request')
    def test_make_request_uses_api_token_and_team_id(self, mock_request):
        mock_request.side_effect = [
            MockResponse({})
        ]

        result = vercel.Resource.make_request(
            method='GET',
            resource='/v2/domains',
            api_token='api-token',
            team_id='team-id'
        )

        assert result == {}

        assert mock_request.mock_calls == [
            call(
                url='https://api.vercel.com/v2/domains',
                method='GET',
                headers={
                    'Content-Type': 'application/json',
                    'Authorization': 'Bearer api-token'
                },
                params={
                    'teamId': 'team-id'
                }
            )
        ]

    @patch('requests.request')
    def test_make_request_honors_headers_and_params(self, mock_request):
        mock_request.side_effect = [
            MockResponse({})
        ]

        result = vercel.Resource.make_request(
            method='GET',
            resource='/v2/domains',
            headers={
                'Something': 'value'
            },
            params={
                'Another': False
            }
        )

        assert result == {}

        assert mock_request.mock_calls == [
            call(
                url='https://api.vercel.com/v2/domains',
                method='GET',
                headers={
                    'Content-Type': 'application/json',
                    'Authorization': 'Bearer fake-api-token',
                    'Something': 'value'
                },
                params={
                    'teamId': 'fake-team-id',
                    'Another': False
                }
            )
        ]

    @patch('requests.request')
    def test_make_paginated_request(self, mock_request):
        mock_request.side_effect = [
            MockResponse({
                'response': [
                    {
                        'id': '1'
                    }
                ],
                'pagination': {
                    'next': '2'
                }
            }),
            MockResponse({
                'response': [
                    {
                        'id': '2'
                    }
                ],
                'pagination': {
                    'next': '3'
                }
            }),
            MockResponse({
                'response': [
                    {
                        'id': '3'
                    }
                ]
            })
        ]

        result = vercel.Resource.make_paginated_request(
            resource='/v2/domains',
            response_key='response'
        )

        assert result == [
            {'id': '1'},
            {'id': '2'},
            {'id': '3'}
        ]

        assert mock_request.mock_calls == [
            call(
                url='https://api.vercel.com/v2/domains',
                method='GET',
                headers={
                    'Content-Type': 'application/json',
                    'Authorization': 'Bearer fake-api-token'
                },
                params={
                    'teamId': 'fake-team-id'
                }
            ),
            call(
                url='https://api.vercel.com/v2/domains',
                method='GET',
                headers={
                    'Content-Type': 'application/json',
                    'Authorization': 'Bearer fake-api-token'
                },
                params={
                    'teamId': 'fake-team-id',
                    'since': '2'
                }
            ),
            call(
                url='https://api.vercel.com/v2/domains',
                method='GET',
                headers={
                    'Content-Type': 'application/json',
                    'Authorization': 'Bearer fake-api-token'
                },
                params={
                    'teamId': 'fake-team-id',
                    'since': '3'
                }
            )
        ]

    @patch('requests.request')
    def test_make_paginated_request_honors_api_token_and_team_id(self, mock_request):
        mock_request.side_effect = [
            MockResponse({
                'response': [
                    {
                        'id': '1'
                    }
                ],
                'pagination': {
                    'next': '2'
                }
            }),
            MockResponse({
                'response': [
                    {
                        'id': '2'
                    }
                ],
                'pagination': {
                    'next': '3'
                }
            }),
            MockResponse({
                'response': [
                    {
                        'id': '3'
                    }
                ]
            })
        ]

        result = vercel.Resource.make_paginated_request(
            resource='/v2/domains',
            response_key='response',
            api_token='api-token',
            team_id='team-id'
        )

        assert result == [
            {'id': '1'},
            {'id': '2'},
            {'id': '3'}
        ]

        assert mock_request.mock_calls == [
            call(
                url='https://api.vercel.com/v2/domains',
                method='GET',
                headers={
                    'Content-Type': 'application/json',
                    'Authorization': 'Bearer api-token'
                },
                params={
                    'teamId': 'team-id'
                }
            ),
            call(
                url='https://api.vercel.com/v2/domains',
                method='GET',
                headers={
                    'Content-Type': 'application/json',
                    'Authorization': 'Bearer api-token'
                },
                params={
                    'teamId': 'team-id',
                    'since': '2'
                }
            ),
            call(
                url='https://api.vercel.com/v2/domains',
                method='GET',
                headers={
                    'Content-Type': 'application/json',
                    'Authorization': 'Bearer api-token'
                },
                params={
                    'teamId': 'team-id',
                    'since': '3'
                }
            )
        ]

    @patch('requests.request')
    def test_make_paginated_request_honors_headers_and_params(self, mock_request):
        mock_request.side_effect = [
            MockResponse({
                'response': [
                    {
                        'id': '1'
                    }
                ],
                'pagination': {
                    'next': '2'
                }
            }),
            MockResponse({
                'response': [
                    {
                        'id': '2'
                    }
                ],
                'pagination': {
                    'next': '3'
                }
            }),
            MockResponse({
                'response': [
                    {
                        'id': '3'
                    }
                ]
            })
        ]

        result = vercel.Resource.make_paginated_request(
            resource='/v2/domains',
            response_key='response',
            headers={
                'Another': 'header'
            },
            params={
                'limit': 10
            }
        )

        assert result == [
            {'id': '1'},
            {'id': '2'},
            {'id': '3'}
        ]

        assert mock_request.mock_calls == [
            call(
                url='https://api.vercel.com/v2/domains',
                method='GET',
                headers={
                    'Content-Type': 'application/json',
                    'Authorization': 'Bearer fake-api-token',
                    'Another': 'header'
                },
                params={
                    'limit': 10,
                    'teamId': 'fake-team-id'
                }
            ),
            call(
                url='https://api.vercel.com/v2/domains',
                method='GET',
                headers={
                    'Content-Type': 'application/json',
                    'Authorization': 'Bearer fake-api-token',
                    'Another': 'header'
                },
                params={
                    'limit': 10,
                    'teamId': 'fake-team-id',
                    'since': '2'
                }
            ),
            call(
                url='https://api.vercel.com/v2/domains',
                method='GET',
                headers={
                    'Content-Type': 'application/json',
                    'Authorization': 'Bearer fake-api-token',
                    'Another': 'header'
                },
                params={
                    'limit': 10,
                    'teamId': 'fake-team-id',
                    'since': '3'
                }
            )
        ]
