""" The most simple API, synchronous. GET record(s). 200 return """

# HTTP library
import requests

# Explicit named resource
# URL = "https://jsonplaceholder.typicode.com/todos/1"
# OR query string
URL = "http://localhost:5000/countries"

def get_url(url):
    return requests.get(url)


def json_data(resp):
    return resp.json()


def resp_code(resp):
    return resp.status_code


if __name__ == "__main__":
    resp = get_url(URL)

    for item in json_data(resp):
        print(item)
    print(resp_code(resp))
