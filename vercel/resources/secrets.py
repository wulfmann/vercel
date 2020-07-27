from vercel.resources.base import Resource


class Secret(Resource):
    def __init__(self, id, name, value, team_id, user_id, created, created_at):
        self.id = id
        self.name = name
        self.value = value
        self.team_id = team_id
        self.user_id = user_id
        self.created = created
        self.created_at = created_at

    @classmethod
    def from_data(cls, data):
        return cls(
            id=data["uid"],
            name=data["name"],
            value=data.get("value"),
            team_id=data.get("teamId"),
            user_id=data["userId"],
            created=data["created"],
            created_at=data.get("createdAt"),
        )

    @classmethod
    def get(cls, identifier, api_version="v3"):
        res = cls.make_request(
            method="GET", resource=f"/now/secrets/{identifier}", api_version=api_version
        )

        return cls.from_data(res)

    @classmethod
    def create(cls, name, value, api_version="v2"):
        res = cls.make_request(
            method="POST",
            resource=f"/now/secrets",
            data={"name": name, "value": value},
            api_version=api_version,
        )

        return cls.from_data(res)

    def delete(self, api_version="v2"):
        return self.make_request(
            method="DELETE", resource=f"/now/secrets/{self.id}", api_version=api_version
        )

    def update_name(self, name, api_version="v2"):
        res = self.make_request(
            method="PATCH",
            resource=f"/now/secrets/{self.id}",
            data={"name": name},
            api_version=api_version,
        )
        self.name = res["name"]
        return self
