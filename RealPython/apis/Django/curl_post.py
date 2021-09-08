curl -i "http://localhost:8000/countries" \
-X POST \
-H "Content-type: application/json" \
-d '{"name": "Germany", "capital": "Berlin", "area": 357022}' \
-w "\n"
