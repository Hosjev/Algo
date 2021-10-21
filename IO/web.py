"""
Get and read a file containing URL/API with data type json.
Parse it and pull out certain information.
Write that info to another file.
** use classes
** use dict
** use Apis
** use with
"""
import requests
import sys
import json
from pathlib import Path



class WebAPI:
    def __init__(self, url):
        self.url = url

    def get_resource(self):
        self.resource = requests.get(self.url)

    def parse_json(self) -> dict:
        return self.resource.json()

    def status_code(self):
        return self.resource.status_code


class IOFile:
    """
    Class with methods shared between
    reading URIs and downloaded data.
    """
    def __init__(self, file_name):
        self.file_name = file_name

    def read_file(self):
        contents = ""
        with open(self.file_name, "r") as fh:
            for line in fh.readlines():
                contents += line
        return contents.strip()

    def write_file(self, content):
        with open(self.file_name, "w") as fh:
            for k,v in content.items():
                fh.write(f"{k}: {v}\n")

    def write_json(self, data):
        with open(self.file_name, "w") as fh:
            fh.write(data)



def parse_drink(data) -> dict:
    """
    Pulling out certain data (deserialized)
     - name: strDrink
     - ingredients: strIngredient1-15 (if not None)
     - container: strGlass
     - instructions: strInstructions
    """
    drink = {}
    
    drink["Name"] = data["drinks"][0]["strDrink"]
    drink["Container"] = data["drinks"][0]["strGlass"]
    drink["Ingredients"] = []
    for x in range(1,16):
        i = data["drinks"][0]["strIngredient" + str(x)]
        if i: drink["Ingredients"].append(i)
    drink["Instructions"] = data["drinks"][0]["strInstructions"]
    return drink


if __name__ == "__main__":
    # Calling classes, methods, functions
    # TODO section
    # Error handling class or function
    file_containing_url = sys.argv[1]

    # The goodies
    read_url = IOFile(file_containing_url).read_file()
    web_object = WebAPI(read_url)
    web_object.get_resource()
    url_data = web_object.parse_json()
    print(type(url_data))
    sud = json.dumps(url_data)
    print(type(sud))
    dud = json.loads(sud)
    print(type(dud))

    # JSON data retrieved.
    # Now, we get info out and write it.
    drink_data = parse_drink(url_data)
    outfile_object = IOFile(str(Path.cwd().joinpath("Output", "drink.txt")))
    outfile_object.write_file(drink_data) 

    # Pretty JSON (getting idents for free)
    output_file = Path.cwd().joinpath("Output", "data.json")
    fo = IOFile(str(output_file))
    fo.write_json(json.dumps(url_data, indent=4))
