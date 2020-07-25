import requests
import vercel
from vercel.exceptions import VercelError

class Resource:
    @classmethod
    def make_request(cls, method, resource, base_url='api.vercel.com', data=None, query_string={}, api_key=None, team_id=None):
        if api_key is None:
            api_key = vercel.api_key

        if team_id is None:
            team_id = vercel.team_id

        if api_key is None:
            raise Exception(f'api_key was not found')

        try:
            url = f'https://{base_url}{resource}'

            kwargs = dict(
                method=method,
                url=url,
                headers={
                    'Content-Type': 'application/json',
                    'Authorization': f'Bearer {vercel.api_key}'
                },
                params=query_string
            )

            if data is not None:
                kwargs['json'] = data

            if team_id is not None:
                kwargs['params']['teamId'] = team_id

            response = requests.request(**kwargs)
            status_code = response.status_code
            response = response.json()

            if 'error' in response:
                raise VercelError(
                    code=response['error']['code'],
                    message=response['error']['message']
                )

            return response
        except Exception as e:
            raise e
