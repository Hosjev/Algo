""" The most simple API, synchronous. POST(update) records. 201 return """


# HTTP library
import requests
import json


# Global variables
URL = "https://jsonplaceholder.typicode.com/todos"

def post_url(url, raw_data, headers):
    """ Using json dumps to ENSURE data is in correct format """
    return requests.post(url, data=json.dumps(raw_data), headers=headers)


def parse_json(resp):
    return resp.json()



if __name__ == "__main__":
    data = {"userId": 1, "title": "Buy milk", "Completed": False}
    headers = {"Content-type": "application/json"}
    response = post_url(URL, data, headers)
    print(parse_json(response), response.status_code)
