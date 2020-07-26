from pathlib import Path
import json

from unittest import TestCase
from unittest.mock import patch, call
from tests.helpers.response import MockResponse

import vercel
from vercel.resources.deployments import Deployment

class TestDeployment(TestCase):

    def setUp(self):
        vercel.api_key = 'fake-api-key'
        vercel.team_id = 'fake-team-id'

    def tearDown(self):
        vercel.api_key = None
        vercel.team_id = None

    @patch('requests.request')
    def test_get_v11(self, mock_request):
        mock_v11_get = Path('tests/fixtures/responses/deployments/v11/get.json')
        mock_request.return_value = MockResponse(response=json.loads(mock_v11_get.open().read()))

        deployment = vercel.Deployment.get('deployment-id')

        assert isinstance(deployment, vercel.Deployment)
        
        assert deployment.id == 'deployment-id'
        assert deployment.url == 'test-deployment.now.sh'
        assert deployment.version == 2
        assert deployment.name == 'test-deployment'
        assert deployment.target == 'production'
        assert deployment.meta == {}
        assert deployment.plan == 'pro'
        assert deployment.public == False
        assert deployment.owner_id == 'owner-id'
        assert deployment.ready_state == 'QUEUED'
        assert deployment.created_at == 1540257589405
        assert deployment.created_in == 'sfo1'
        assert deployment.regions == [
          'sfo1'
        ]
        assert deployment.functions == {
          "api/test.js": {
            "memory": 3008
          }
        }
        assert deployment.routes == None
        assert deployment.env == []
        assert deployment.build == {
          'env': {}
        }
        assert deployment.aliases == [
          "test.com",
          "project.my-team.now.sh"
        ]
        assert deployment.alias_error == None
        assert deployment.alias_assigned == True

        assert [
            call(
                method='GET',
                url='https://api.vercel.com/v11/deployments/deployment-id',
                headers={
                    'Content-Type': 'application/json',
                    'Authorization': 'Bearer fake-api-key'
                },
                params={
                    'teamId': 'fake-team-id'
                }
            )
        ] == mock_request.mock_calls