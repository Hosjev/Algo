import requests


URL = "http://localhost:8000/countries"


def get_resource(url):
    return requests.get(url)


def parse_json(response):
    return response.json()



if __name__ == "__main__":
    response = get_resource(URL)
    for item in parse_json(response):
        print(item)
    print(response.status_code)
