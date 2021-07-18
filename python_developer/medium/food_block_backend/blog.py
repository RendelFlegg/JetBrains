import sqlite3


data = {"meals": ("breakfast", "brunch", "lunch", "supper"),
        "ingredients": ("milk", "cacao", "strawberry", "blueberry", "blackberry", "sugar"),
        "measures": ("ml", "g", "l", "cup", "tbsp", "tsp", "dsp", "")}
conn = sqlite3.connect('food_blog.db')
c = conn.cursor()

c.execute("""CREATE TABLE meals (
            meal_id INT PRIMARY KEY,
            meal_name TEXT NOT NULL UNIQUE
            )""")

c.execute("""CREATE TABLE ingredients (
            ingredient_id INT PRIMARY KEY,
            ingredient_name TEXT NOT NULL UNIQUE
            )""")

c.execute("""CREATE TABLE measures (
            measure_id INT PRIMARY KEY,
            measure_name TEXT UNIQUE
            )""")

conn.commit()


for key, value in data.items():
    for idx, element in enumerate(value, 1):
        c.execute(f"INSERT INTO {key} VALUES ('{idx}', '{element}')")
        conn.commit()

conn.close()
