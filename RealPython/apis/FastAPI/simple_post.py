import requests, json


URL = "http://localhost:8000/countries"



def get_resource(url):
    return requests.get(url)


def post_resource(url, raw_data, headers):
    return requests.post(url, data=json.dumps(raw_data), headers=headers)


def parse_json(response):
    return response.json()




if __name__ == "__main__":
    # Before
    response = get_resource(URL)
    for country in parse_json(response):
        print(country)

    data = {"name": "Germany", "capital": "Berlin", "area": 531722}
    headers = {"Content-type": "application/json"}

    # After
    response = post_resource(URL, data, headers)
    for country in parse_json(response):
        print(country)
