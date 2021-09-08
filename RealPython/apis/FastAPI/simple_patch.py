"""
You need to write this function in FastAPI first
"""

import requests, json, sys


URL = "http://localhost:8000/countries"



def get_resource(url):
    return requests.get(url)


def patch_resource(url, raw_data, headers):
    return requests.patch(url, data=json.dumps(raw_data), headers=headers)


def parse_json(response):
    return response.json()




if __name__ == "__main__":
    # Args for patch - ID
    country_id = sys.argv[1]
    print(country_id)

    # Before
    response = get_resource(URL)
    for country in parse_json(response):
        print(country)

    data = {"id": country_id, "name": "France", "capital": "Paris", "area": 678210}
    headers = {"Content-type": "application/json"}

    # After
    response = patch_resource(URL, data, headers)
    for country in parse_json(response):
        print(country)

