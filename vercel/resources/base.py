import requests
import vercel
from vercel.exceptions import VercelError


class Resource:
    @classmethod
    def make_request(
        cls,
        method,
        resource,
        api_version=None,
        base_url="api.vercel.com",
        data=None,
        query_string={},
        api_key=None,
        team_id=None,
    ):
        if api_key is None:
            api_key = vercel.api_key

        if team_id is None:
            team_id = vercel.team_id

        if api_key is None:
            raise Exception(f"api_key was not found")

        if api_version is None:
            raise Exception(f"api_version was not found")

        try:
            url = f"https://{base_url}/{api_version}{resource}"

            kwargs = dict(
                method=method,
                url=url,
                headers={
                    "Content-Type": "application/json",
                    "Authorization": f"Bearer {vercel.api_key}",
                },
                params=query_string,
            )

            if data is not None:
                kwargs["json"] = data

            if team_id is not None:
                kwargs["params"]["teamId"] = team_id

            response = requests.request(**kwargs)
            status_code = response.status_code
            response = response.json()

            if "error" in response:
                print(response)
                raise VercelError(
                    code=response["error"]["code"], message=response["error"]["message"]
                )

            return response
        except Exception as e:
            raise e

    @classmethod
    def make_paginated_request(
        cls,
        resource,
        response_key,
        headers={},
        params={},
        api_key=None,
        team_id=None,
        results=[],
    ):
        if api_key is None:
            api_key = vercel.api_key

        if api_key is None:
            raise Exception(f"api_key was not found")

        # Add Authentication Headers
        headers.update(
            {
                "Content-Type": "application/json",
                "Authorization": f"Bearer {vercel.api_key}",
            }
        )

        if team_id is None:
            team_id = vercel.team_id

        # Add Team ID if set
        if team_id is not None:
            params.update({"teamId": team_id})

        base_url = "api.vercel.com"

        try:
            url = f"https://{base_url}{resource}"

            response = requests.request(url=url, method='GET', headers=headers, params=params).json()

            # Handle Errors
            if "error" in response:
                raise VercelError(
                    code=response["error"]["code"], message=response["error"]["message"]
                )

            # Append result
            records = response.get(response_key)
            if records is None:
                raise Exception(f"failed to find response_key in response")
            results += records

            # Handle Pagination
            if "pagination" in response:
                next_since = response["pagination"].get("next")
                if next_since is None:
                    raise ValueError("unable to get next value for pagination")

                params.update({"since": next_since})

                return cls.make_paginated_request(
                    resource=resource,
                    response_key=response_key,
                    headers=headers,
                    params=params,
                    api_key=api_key,
                    team_id=team_id,
                    results=results,
                )

            return results
        except Exception as e:
            raise e
