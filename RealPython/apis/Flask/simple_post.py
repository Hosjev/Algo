""" The most simple POST """


import requests
import json


URL = "http://localhost:5000/countries"


def get_resource(url):
    return requests.get(url)



def post_resource(url, raw_data, headers):
    return requests.post(url, data=json.dumps(raw_data), headers=headers)



def parse_json(response):
    return response.json()



if __name__ == "__main__":
    data = {
        "area": 309987,
        "name": "France",
        "capital": "Paris",
    }
    headers = {"Content-type": "application/json"}

    # Post
    response = post_resource(URL, data, headers)
    print(parse_json(response), response.status_code)
    print(parse_json(response)["id"])
