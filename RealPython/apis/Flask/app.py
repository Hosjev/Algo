from flask import Flask, request, jsonify

app = Flask(__name__)

# My database, runs in memory only during runtime
countries = [
    {"id": 1, "name": "Alberta", "capital": "Edmonton", "area": 415673},
    {"id": 2, "name": "Australia", "capital": "Canberra", "area": 5097832},
    {"id": 3, "name": "Egypt", "capital": "Cairo", "area": 1010408},
]



# Find values for each ID key, find MAX, then add one
def _find_next_id():
    return max(country["id"] for country in countries) + 1



# Decorate with Flask (version 2+) get, resource as argument
@app.get("/countries")
def get_countries():
    return jsonify(countries)


# Decorate with Flask (version 2+) post, resource as argument
@app.post("/countries")
def add_country():
    if request.is_json:
        country = request.get_json()
        country["id"] = _find_next_id()
        countries.append(country)
        return country, 201
    return {"error": "Request must be JSON formatted"}, 415

