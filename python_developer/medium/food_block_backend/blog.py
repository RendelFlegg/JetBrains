import sqlite3


data = {"meals": ("breakfast", "brunch", "lunch", "supper"),
        "ingredients": ("milk", "cacao", "strawberry", "blueberry", "blackberry", "sugar"),
        "measures": ("ml", "g", "l", "cup", "tbsp", "tsp", "dsp", "")}
status = "go"
conn = sqlite3.connect('food_blog.db')
c = conn.cursor()

c.execute("""CREATE TABLE IF NOT EXISTS meals (
            meal_id INT PRIMARY KEY,
            meal_name TEXT NOT NULL UNIQUE
            )""")

c.execute("""CREATE TABLE IF NOT EXISTS ingredients (
            ingredient_id INT PRIMARY KEY,
            ingredient_name TEXT NOT NULL UNIQUE
            )""")

c.execute("""CREATE TABLE IF NOT EXISTS measures (
            measure_id INT PRIMARY KEY,
            measure_name TEXT UNIQUE
            )""")

c.execute("""CREATE TABLE IF NOT EXISTS recipes (
            recipe_id INT PRIMARY KEY,
            recipe_name TEXT NOT NULL,
            recipe_description TEXT
            )""")
conn.commit()


for key, value in data.items():
    for idx, element in enumerate(value, 1):
        c.execute(f"INSERT INTO {key} VALUES ('{idx}', '{element}')")
        conn.commit()


def populate_recipes():
    global status
    name = input('Recipe name: ',)
    if name == "":
        status = "break"
        return status
    description = input('Recipe description: ',)
    c.execute(f"INSERT INTO recipes ('recipe_name', 'recipe_description') VALUES ('{name}', '{description}')")
    conn.commit()


print("Pass the empty recipe name to exit.")
while status == "go":
    populate_recipes()
    if status == "break":
        break

conn.close()
