from pathlib import Path
import json

from unittest import TestCase
from unittest.mock import patch, call
from tests.helpers.response import MockResponse

import vercel
from vercel.resources.deployments import Deployment


class TestProjects(TestCase):
    def setUp(self):
        vercel.api_key = "fake-api-key"
        vercel.team_id = "fake-team-id"

    def tearDown(self):
        vercel.api_key = None
        vercel.team_id = None

    @patch("requests.request")
    def test_create_v1(self, mock_request):
        mock_v1_create = Path("tests/fixtures/responses/projects/v1/create.json")
        mock_request.return_value = MockResponse(
            response=json.loads(mock_v1_create.open().read())
        )

        project = vercel.Project.create("test-project")

        assert isinstance(project, vercel.Project)

        # Verify Project Properties
        assert project.id == "project-id"
        assert project.name == "test-project"
        assert 1 == len(project.aliases)
        alias = project.aliases[0]
        assert isinstance(alias, vercel.ProjectAlias)

        # Verify Alias Properties
        assert alias.domain == "test-project.now.sh"
        assert alias.target == "PRODUCTION"
        assert alias.created_at == 1555413045188
        assert alias.configured_by == "A"
        assert alias.configured_changed_at == 1555413045188

        assert project.account_id == "account-id"
        assert project.updated_at == 1555413045188
        assert project.created_at == 1555413045188

        assert project.production_deployment == None
        assert 0 == len(project.latest_deployments)

        assert project.production_deployment == None

        assert [
            call(
                method="POST",
                url="https://api.vercel.com/v1/projects",
                headers={
                    "Content-Type": "application/json",
                    "Authorization": "Bearer fake-api-key",
                },
                params={"teamId": "fake-team-id"},
                json={"name": "test-project"},
            )
        ] == mock_request.mock_calls

    @patch("requests.request")
    def test_get_v1(self, mock_request):
        mock_v1_get = Path("tests/fixtures/responses/projects/v1/get.json")
        mock_request.return_value = MockResponse(
            response=json.loads(mock_v1_get.open().read())
        )

        project = vercel.Project.get("test-project")

        assert isinstance(project, vercel.Project)

        # Verify Project Properties
        assert project.id == "project-id"
        assert project.name == "test-project"

        assert 1 == len(project.aliases)
        alias = project.aliases[0]
        assert isinstance(alias, vercel.ProjectAlias)

        # Verify Alias Properties
        assert alias.domain == "test-project.now.sh"
        assert alias.target == "PRODUCTION"
        assert alias.created_at == 1555413045188
        assert alias.configured_by == "A"
        assert alias.configured_changed_at == 1555413045188

        assert project.account_id == "account-id"
        assert project.updated_at == 1555413045188
        assert project.created_at == 1555413045188

        # Environment Variables
        assert 1 == len(project.environment_variables)
        env_var = project.environment_variables[0]

        assert env_var.key == "API_SECRET"
        assert env_var.value == "@a-new-secret"
        assert env_var.configuration_id == None
        assert env_var.updated_at == 1557241361455
        assert env_var.created_at == 1557241361455

        # Production Deployment
        production_deployment = project.production_deployment
        assert isinstance(production_deployment, Deployment)

        assert production_deployment.aliases == ["test-project.now.sh"]
        assert production_deployment.alias_assigned == 1571239348998
        assert production_deployment.created_at == 1571239348998
        assert production_deployment.created_in == "sfo1"
        assert production_deployment.deployment_hostname == "test-project-rjtr4pz3f"
        assert production_deployment.forced == False
        assert production_deployment.id == "deployment-id"
        assert production_deployment.meta == {}
        assert production_deployment.plan == "pro"
        assert production_deployment.private == True
        assert production_deployment.ready_state == "READY"
        assert production_deployment.requested_at == 1571239348998
        assert production_deployment.target == "production"
        assert production_deployment.team_id == None
        assert production_deployment.type == "LAMBDAS"
        assert production_deployment.url == "test-project-rjtr4pz3f.now.sh"
        assert production_deployment.user_id == "user-id"

        # Latest Deployments
        assert 1 == len(project.latest_deployments)
        latest_deployment = project.latest_deployments[0]
        assert isinstance(latest_deployment, Deployment)

        assert latest_deployment.aliases == ["test-project.now.sh"]
        assert latest_deployment.alias_assigned == 1571239348998
        assert latest_deployment.created_at == 1571239348998
        assert latest_deployment.created_in == "sfo1"
        assert latest_deployment.deployment_hostname == "test-project-rjtr4pz3f"
        assert latest_deployment.forced == False
        assert latest_deployment.id == "deployment-id"
        assert latest_deployment.meta == {}
        assert latest_deployment.plan == "pro"
        assert latest_deployment.private == True
        assert latest_deployment.ready_state == "READY"
        assert latest_deployment.requested_at == 1571239348998
        assert latest_deployment.target == "production"
        assert latest_deployment.team_id == None
        assert latest_deployment.type == "LAMBDAS"
        assert latest_deployment.url == "test-project-rjtr4pz3f.now.sh"
        assert latest_deployment.user_id == "user-id"

        assert [
            call(
                method="GET",
                url="https://api.vercel.com/v1/projects/test-project",
                headers={
                    "Content-Type": "application/json",
                    "Authorization": "Bearer fake-api-key",
                },
                params={"teamId": "fake-team-id"},
            )
        ] == mock_request.mock_calls

    @patch("requests.request")
    def test_delete_v1(self, mock_request):
        mock_v1_get = Path("tests/fixtures/responses/projects/v1/get.json")
        mock_v1_delete = Path("tests/fixtures/responses/projects/v1/delete.json")

        mock_request.side_effect = [
            MockResponse(response=json.loads(mock_v1_get.open().read())),
            MockResponse(response=json.loads(mock_v1_delete.open().read())),
        ]

        project = vercel.Project.get("test-project")
        project.delete()

        assert [
            call(
                method="GET",
                url="https://api.vercel.com/v1/projects/test-project",
                headers={
                    "Content-Type": "application/json",
                    "Authorization": "Bearer fake-api-key",
                },
                params={"teamId": "fake-team-id"},
            ),
            call(
                method="DELETE",
                url="https://api.vercel.com/v1/projects/project-id",
                headers={
                    "Content-Type": "application/json",
                    "Authorization": "Bearer fake-api-key",
                },
                params={"teamId": "fake-team-id"},
            ),
        ] == mock_request.mock_calls

    @patch("requests.request")
    def test_create_env_var_v4(self, mock_request):
        mock_v1_get = Path("tests/fixtures/responses/projects/v1/get.json")
        mock_v4_create_env_var = Path(
            "tests/fixtures/responses/projects/v4/create_env_var.json"
        )

        mock_request.side_effect = [
            MockResponse(response=json.loads(mock_v1_get.open().read())),
            MockResponse(response=json.loads(mock_v4_create_env_var.open().read())),
        ]

        project = vercel.Project.get("test-project")
        project.create_environment_variable(
            key="my-var", value="@my-secret", target="production"
        )

        assert [
            call(
                method="GET",
                url="https://api.vercel.com/v1/projects/test-project",
                headers={
                    "Content-Type": "application/json",
                    "Authorization": "Bearer fake-api-key",
                },
                params={"teamId": "fake-team-id"},
            ),
            call(
                method="POST",
                url="https://api.vercel.com/v4/projects/project-id/env",
                headers={
                    "Content-Type": "application/json",
                    "Authorization": "Bearer fake-api-key",
                },
                json={"key": "my-var", "value": "@my-secret", "target": "production"},
                params={"teamId": "fake-team-id"},
            ),
        ] == mock_request.mock_calls

    @patch("requests.request")
    def test_delete_env_var_v4(self, mock_request):
        mock_v1_get = Path("tests/fixtures/responses/projects/v1/get.json")
        mock_v4_delete_env_var = Path(
            "tests/fixtures/responses/projects/v4/create_env_var.json"
        )

        mock_request.side_effect = [
            MockResponse(response=json.loads(mock_v1_get.open().read())),
            MockResponse(response=json.loads(mock_v4_delete_env_var.open().read())),
        ]

        project = vercel.Project.get("test-project")
        project.delete_environment_variable(key="my-var", target="production")

        assert [
            call(
                method="GET",
                url="https://api.vercel.com/v1/projects/test-project",
                headers={
                    "Content-Type": "application/json",
                    "Authorization": "Bearer fake-api-key",
                },
                params={"teamId": "fake-team-id"},
            ),
            call(
                method="DELETE",
                url="https://api.vercel.com/v4/projects/project-id/env/my-var",
                headers={
                    "Content-Type": "application/json",
                    "Authorization": "Bearer fake-api-key",
                },
                params={"teamId": "fake-team-id", "target": "production"},
            ),
        ] == mock_request.mock_calls

    @patch("requests.request")
    def test_add_domain_v1(self, mock_request):
        mock_v1_get = Path("tests/fixtures/responses/projects/v1/get.json")
        mock_v1_add_domain = Path(
            "tests/fixtures/responses/projects/v1/add_domain.json"
        )

        mock_request.side_effect = [
            MockResponse(response=json.loads(mock_v1_get.open().read())),
            MockResponse(response=json.loads(mock_v1_add_domain.open().read())),
        ]

        project = vercel.Project.get("test-project")
        project.add_domain("foobar.com")

        assert [
            call(
                method="GET",
                url="https://api.vercel.com/v1/projects/test-project",
                headers={
                    "Content-Type": "application/json",
                    "Authorization": "Bearer fake-api-key",
                },
                params={"teamId": "fake-team-id"},
            ),
            call(
                method="POST",
                url="https://api.vercel.com/v1/projects/project-id/alias",
                headers={
                    "Content-Type": "application/json",
                    "Authorization": "Bearer fake-api-key",
                },
                json={"domain": "foobar.com"},
                params={"teamId": "fake-team-id"},
            ),
        ] == mock_request.mock_calls

    @patch("requests.request")
    def test_remove_domainv1(self, mock_request):
        mock_v1_get = Path("tests/fixtures/responses/projects/v1/get.json")
        mock_v1_remove_domain = Path(
            "tests/fixtures/responses/projects/v1/remove_domain.json"
        )

        mock_request.side_effect = [
            MockResponse(response=json.loads(mock_v1_get.open().read())),
            MockResponse(response=json.loads(mock_v1_remove_domain.open().read())),
        ]

        project = vercel.Project.get("test-project")
        project.remove_domain("foobar.com")

        assert [
            call(
                method="GET",
                url="https://api.vercel.com/v1/projects/test-project",
                headers={
                    "Content-Type": "application/json",
                    "Authorization": "Bearer fake-api-key",
                },
                params={"teamId": "fake-team-id"},
            ),
            call(
                method="DELETE",
                url="https://api.vercel.com/v1/projects/project-id/alias",
                headers={
                    "Content-Type": "application/json",
                    "Authorization": "Bearer fake-api-key",
                },
                params={"domain": "foobar.com", "teamId": "fake-team-id"},
            ),
        ] == mock_request.mock_calls

    @patch("requests.request")
    def test_redirect_domain_v1(self, mock_request):
        mock_v1_get = Path("tests/fixtures/responses/projects/v1/get.json")
        mock_v1_redirect_domain = Path(
            "tests/fixtures/responses/projects/v1/redirect_domain.json"
        )

        mock_request.side_effect = [
            MockResponse(response=json.loads(mock_v1_get.open().read())),
            MockResponse(response=json.loads(mock_v1_redirect_domain.open().read())),
        ]

        project = vercel.Project.get("test-project")
        project.redirect_domain("foobar.com", "www.foobar.com")

        assert [
            call(
                method="GET",
                url="https://api.vercel.com/v1/projects/test-project",
                headers={
                    "Content-Type": "application/json",
                    "Authorization": "Bearer fake-api-key",
                },
                params={"teamId": "fake-team-id"},
            ),
            call(
                method="PATCH",
                url="https://api.vercel.com/v1/projects/project-id/alias",
                headers={
                    "Content-Type": "application/json",
                    "Authorization": "Bearer fake-api-key",
                },
                json={"domain": "foobar.com", "redirect": "www.foobar.com"},
                params={"teamId": "fake-team-id"},
            ),
        ] == mock_request.mock_calls
