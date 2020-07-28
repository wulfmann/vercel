from vercel.resources.base import Resource


class Alias(Resource):
    def __init__(self, id, alias, deployment, created, project_id, deployment_id):
        self.id = id
        self.alias = alias
        self.deployment = deployment
        self.created = created
        self.project_id = project_id
        self.deployment_id = deployment_id

    @classmethod
    def from_data(cls, data):
        return cls(
            id=data["uid"],
            alias=data["alias"],
            deployment=data["deployment"],
            created=data["created"],
            project_id=data["projectId"],
            deployment_id=data["deploymentId"],
        )

    @classmethod
    def assign_to_domain(
        cls,
        deployment_id,
        alias,
        redirect=None,
        api_version="v2",
        api_token=None,
        team_id=None,
    ):
        data = {"alias": alias}

        if redirect is not None:
            data["redirect"] = redirect

        return cls.make_request(
            method="POST",
            resource=f"/{api_version}/now/deployments/{deployment_id}/aliases",
            data=data,
            api_token=api_token,
            team_id=team_id,
        )

    @classmethod
    def get(cls, identifier, api_version="v2", api_token=None, team_id=None):
        res = cls.make_request(
            method="GET",
            resource=f"/{api_version}/now/aliases/{identifier}",
            api_token=api_token,
            team_id=team_id,
        )

        return cls.from_data(res)

    def delete(self, api_version="v2", api_token=None, team_id=None):
        return self.make_request(
            method="DELETE",
            resource=f"/{api_version}/now/aliases/{self.id}",
            api_token=api_token,
            team_id=team_id,
        )

    def purge(self, api_version="v2", api_token=None, team_id=None):
        return self.make_request(
            method="PURGE",
            resource=f"/{api_version}/now/aliases/{self.id}",
            api_token=api_token,
            team_id=team_id,
        )
