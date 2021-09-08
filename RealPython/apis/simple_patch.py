""" The most simple API for PATCH(update fields), synchronous. 200 return """


# HTTP library
import requests


# Global variables
URL = "https://jsonplaceholder.typicode.com/todos/10"


def get_resource(url):
    return requests.get(url)


def patch_resource(url, data):
    return requests.patch(url, json=data)


def parse_json(data):
    return data.json()


if __name__ == "__main__":
    # Before
    print(parse_json(get_resource(URL)))
    data_change = {"title": "Clean laundry"}
    response = patch_resource(URL, data_change)
    # After
    print(parse_json(response), response.status_code)
