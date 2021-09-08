""" The most simple API, synchronous. GET record(s). 200 return """

# HTTP library
import requests

# Explicit named resource
# URL = "https://jsonplaceholder.typicode.com/todos/1"
# OR query string
URL = "https://jsonplaceholder.typicode.com/todos?id=1"

class WebResource:
    def __init__(self, url):
        self.url = url

    def get_url(self):
        self.resp = requests.get(self.url)

    def json_data(self):
        return self.resp.json()

    def resp_code(self):
        return self.resp.status_code


if __name__ == "__main__":
    wb = WebResource(URL)
    wb.get_url()
    print(wb.resp_code())
    print(wb.json_data())

