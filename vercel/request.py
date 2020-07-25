import requests
import vercel
from vercel.exceptions import VercelError

def make_request(method, resource, data=None):
    if vercel.api_key is None:
        raise Exception(f'api_key was not found')

    try:
        base = 'api.vercel.com'
        url = f'https://{base}{resource}'

        if vercel.team_id is not None:
            url += f'?teamId={vercel.team_id}'

        kwargs = dict(
            method=method,
            url=url,
            headers={
                'Content-Type': 'application/json',
                'Authorization': f'Bearer {vercel.api_key}'
            }
        )

        if data is not None:
            kwargs['json'] = data

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