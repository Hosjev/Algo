""" The most simple PUT(new record) api, synchronous. 200 return """


# HTTP library
import requests


URL = "https://jsonplaceholder.typicode.com/todos/10"


def get_url(url):
    return requests.get(url)


def put_url(url, data):
    return requests.put(url, json=data)


def parse_json(data):
    return data.json()


if __name__ == "__main__":
    data = {"userId": 1, "title": "Wash car", "completed": True}
    response = get_url(URL)
    print("Get response", parse_json(response), response.status_code)

    # Now we change it (title, Completed)
    put_response = put_url(URL, data)
    print("Put response", parse_json(put_response), put_response.status_code)
