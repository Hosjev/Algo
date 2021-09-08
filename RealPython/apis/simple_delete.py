""" The most simple API DELETE resource, synchronous. 204 return """


# HTTP library
import requests


URL = "https://jsonplaceholder.typicode.com/todos/10"



def get_resource(url):
    return requests.get(url)


def delete_resource(url):
    return requests.delete(url)


def parse_json(data):
    return data.json()


if __name__ == "__main__":
    # {'userId': 1, 'id': 10, 'title': 'Clean laundry', 'completed': True}
    print(parse_json(get_resource(URL)))

    response = delete_resource(URL)
    print(parse_json(response), response.status_code)
