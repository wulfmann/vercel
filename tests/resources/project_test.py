from pathlib import Path
import json

from unittest import TestCase
from unittest.mock import patch, call
from tests.helpers.response import MockResponse

import vercel

class TestProject(TestCase):

    def setUp(self):
        vercel.api_key = 'fake-api-key'
        vercel.team_id = 'fake-team-id'

    def tearDown(self):
        vercel.api_key = None
        vercel.team_id = None

    @patch('requests.request')
    def test_create_v1(self, mock_request):
        mock_v1_create = Path('tests/fixtures/responses/projects/v1/create.json')
        mock_request.return_value = MockResponse(response=json.loads(mock_v1_create.open().read()))

        project = vercel.Project.create('test-project')

        assert isinstance(project, vercel.Project)

        # Verify Project Properties
        assert project.id == 'project-id'
        assert project.name == 'test-project'
        assert 1 == len(project.aliases)
        alias = project.aliases[0]
        assert isinstance(alias, vercel.Alias)
        
        # Verify Alias Properties
        assert alias.domain == 'test-project.now.sh'
        assert alias.target == 'PRODUCTION'
        assert alias.created_at == 1555413045188
        assert alias.configured_by == 'A'
        assert alias.configured_changed_at == 1555413045188

        assert project.account_id == 'account-id'
        assert project.updated_at == 1555413045188
        assert project.created_at == 1555413045188
        
        assert project.production_deployment == None
        assert 0 == len(project.latest_deployments)

        assert project.production_deployment == None
        
        assert [
            call(
                method='POST',
                url='https://api.vercel.com/v1/projects',
                headers={
                    'Content-Type': 'application/json',
                    'Authorization': 'Bearer fake-api-key'
                },
                params={
                    'teamId': 'fake-team-id'
                },
                json={
                    'name': 'test-project'
                }
            )
        ] == mock_request.mock_calls
