from pathlib import Path
import json

from unittest import TestCase
from unittest.mock import patch, call
from tests.helpers.response import MockResponse

import vercel

class TestTeams(TestCase):

    def setUp(self):
        vercel.api_key = 'fake-api-key'
        vercel.team_id = 'fake-team-id'

    def tearDown(self):
        vercel.api_key = None
        vercel.team_id = None

    @patch('requests.request')
    def test_create_v1(self, mock_request):
        mock_request.return_value = MockResponse(response={
          'id': 'team-id'
        })

        team = vercel.Team.create('my-team')

        assert isinstance(team, vercel.Team)
        assert team.id == 'team-id'
        
        assert [
            call(
                method='POST',
                url='https://api.vercel.com/v1/teams',
                headers={
                    'Content-Type': 'application/json',
                    'Authorization': 'Bearer fake-api-key'
                },
                data={
                  'slug': 'my-team'
                },
                params={
                    'teamId': 'fake-team-id'
                }
            )
        ] == mock_request.mock_calls
        
    @patch('requests.request')
    def test_delete_v1(self, mock_request):
        mock_v4_get = Path('tests/fixtures/responses/teams/v1/get.json')
        mock_request.return_value = MockResponse(response=json.loads(mock_v4_get.open().read()))

        team = vercel.Team.get('my-team')
        team.delete()
        
        assert [
            call(
                method='GET',
                url='https://api.vercel.com/v1/teams',
                headers={
                    'Content-Type': 'application/json',
                    'Authorization': 'Bearer fake-api-key'
                },
                params={
                    'teamId': 'fake-team-id',
                    'slug': 'my-team'
                }
            ),
            call(
                method='DELETE',
                url='https://api.vercel.com/v1/teams/team-id',
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
    def test_update_v1(self, mock_request):
        mock_v4_get = Path('tests/fixtures/responses/teams/v1/get.json')
        mock_request.return_value = MockResponse(response=json.loads(mock_v4_get.open().read()))

        team = vercel.Team.get('my-team')
        team.update(
          slug='new-slug',
          name='New Name'
        )
        
        assert [
            call(
                method='GET',
                url='https://api.vercel.com/v1/teams',
                headers={
                    'Content-Type': 'application/json',
                    'Authorization': 'Bearer fake-api-key'
                },
                params={
                    'teamId': 'fake-team-id',
                    'slug': 'my-team'
                }
            ),
            call(
                method='PATCH',
                url='https://api.vercel.com/v1/teams/team-id',
                headers={
                    'Content-Type': 'application/json',
                    'Authorization': 'Bearer fake-api-key'
                },
                data={
                  'slug': 'new-slug',
                  'name': 'New Name'
                },
                params={
                    'teamId': 'fake-team-id'
                }
            )
        ] == mock_request.mock_calls
        
    @patch('requests.request')
    def test_get_v1(self, mock_request):
        mock_v4_get = Path('tests/fixtures/responses/teams/v1/get.json')
        mock_request.return_value = MockResponse(response=json.loads(mock_v4_get.open().read()))

        team = vercel.Team.get('my-team')

        assert isinstance(team, vercel.Team)
        
        assert team.name == 'My Team'
        assert team.id == 'team-id'
        assert team.slug == 'my-team'
        assert team.creator_id == 'creator-id'
        assert team.created == '2017-04-29T17:21:54.514Z'
        assert team.avatar == None
        
        assert [
            call(
                method='GET',
                url='https://api.vercel.com/v1/teams',
                headers={
                    'Content-Type': 'application/json',
                    'Authorization': 'Bearer fake-api-key'
                },
                params={
                    'teamId': 'fake-team-id',
                    'slug': 'my-team'
                }
            )
        ] == mock_request.mock_calls