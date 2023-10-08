import requests
import json
import pprint

from settings import TOKEN, urls


def get_data(url, headers, body):
    response = requests.post(url, data=json.dumps(body), headers=headers)
    return response.json()


headers = {
    "Authorization": "Bearer " + TOKEN,
    "Content-Type": "application/json"
}

body = {
    "method": "get",
    "params": {
        "FieldNames": ["Id", "Name", "Type", "State", "Status"],
        "SelectionCriteria": {
            # "Types": ["SMART_CAMPAIGN"],
            "Statuses": ["DRAFT", "ACCEPTED"]
        },
        "Page": {
            "Limit": 10,
            "Offset": 20
        }
    }
}

# dict --> json
data = get_data(urls["campaigns"], headers, body)
pprint.pprint(data)
