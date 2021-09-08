from fastapi import FastAPI
from pydantic import BaseModel, Field


app = FastAPI()



def _find_next_id():
    return max(country.country_id for country in countries) + 1


class Country(BaseModel):
    country_id: int = Field(default_factory=_find_next_id, alias="id")
    name: str
    capital: str
    area: int

# Build your database here, after BaseModel class defined
countries = [
    Country(id=1, name="Thailand", capital="Bangkok", area=513223),
    Country(id=2, name="Australia", capital="Canberra", area=7093223),
    Country(id=3, name="Egypt", capital="Cairo", area=917859),
]

@app.get("/countries")
async def get_countries():
    return countries


@app.post("/countries", status_code=201)
async def add_country(country: Country):
    countries.append(country)
    return country
