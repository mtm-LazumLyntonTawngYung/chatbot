import requests

from openapi_server.variables import GEMINI_API_ENDPOINT


def infer_case_group(care_id, body):
    url = f'{GEMINI_API_ENDPOINT}/v1/case-groups/inference'
    headers = {
        'Content-Type': 'application/json',
        'X-API-KEY': 'apiKey',
    }
    data = {
        'care_id': care_id,
        'body': body,
    }
    result = requests.post(url, json=data, headers=headers, timeout=100)
    return result.json()
