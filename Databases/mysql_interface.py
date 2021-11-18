import json

from mysql import connector
from pathlib import Path
from argparse import ArgumentParser



class IOFile:
    def __init__(self, c_file):
        self.c_file = c_file


    def open_file(self):
        f_obj = open(self.c_file)
        return self.parse_json(f_obj)


    def open_file(self):
        contents = ""
        with open(self.c_file, "r") as fh:
            for line in fh.readlines():
                contents += line
        return self.parse_json(contents.strip())


    def parse_json(self, j_string):
        return json.loads(j_string)


class MySql:
    def __init__(self, cnx):
        self.cnx = cnx


    def select_id(self, query):
        try:
            cursor = self.cnx.cursor()
            cursor.execute(query)
            data = cursor.fetchall()
        finally:
            cursor.close()
        return data[0][0]


    def select(self, query, d_id, M = False):
        try:
            cursor = self.cnx.cursor()
            cursor.execute(query, (d_id, ))
            data = cursor.fetchall()
        finally:
            cursor.close()
        return data[0][0] if not M else data


    def insert(self, d_id):
        return


    def close(self):
        self.cnx.close()



if __name__ == "__main__":
    # We have 1 arg, drink name
    parser = ArgumentParser(description="Drink database query")
    parser.add_argument("--name", "-n", required=True)
    args = parser.parse_args()

    # Open and read DB config file
    c_obj = IOFile(str(Path.cwd().joinpath("config", "mysql_db.json")))
    config = c_obj.open_file()["config"][0]
    cnx = MySql(connector.connect(**config))

    # Build object
    # below - CBt-2oz whiskey or captains, 1oz Herring, 6oz ginger ale
    # below - CBs-1oz whiskey or captains, tsp Herring
    drink = {
            #"name": "Cherry Bomb (tall)",
            "name": f"{args.name}",
            }
    query = (f"select drinks.id from drinks where drinks.drink_name = \"{drink['name']}\"")
    d_id = cnx.select_id(query)
    query = ("select types.type_name "
            "from drink_type "
            "inner join drinks on drink_type.drink_id = drinks.id "
            "inner join types on drink_type.type_id = types.type_id "
            "where drinks.id = %s"
            )
    drink["type"] = cnx.select(query, d_id)
    query = ("select containers.cont_name "
            "from drink_container "
            "inner join drinks on drink_container.drink_id = drinks.id "
            "inner join containers on drink_container.cont_id = containers.cont_id "
            "where drinks.id = %s"
            )
    drink["container"] = cnx.select(query, d_id)
    query = ("select measurements.amount, ingredients.ingredient_name "
            "from ingredient_combos "
            "inner join drinks on ingredient_combos.drink_id = drinks.id "
            "inner join ingredients on ingredient_combos.ingred_id = ingredients.ingred_id "
            "inner join measurements on ingredient_combos.measure_id = measurements.measure_id "
            "where drinks.id = %s"
            )
    drink["ingredients"] = cnx.select(query, d_id, True)
    query = ("select instructions.description "
            "from instructions "
            "inner join drinks on instructions.drink_id = drinks.id "
            "where drinks.id = %s"
            )
    drink["instructions"] = cnx.select(query, d_id)
    for key, val in drink.items():
        if key == "ingredients":
            print(key)
            [print("\t", x) for x in val]
        else: print(key, ":", val)

    cnx.close()
