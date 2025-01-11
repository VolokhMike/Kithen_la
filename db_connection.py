import sqlite3


def init():
    connection = sqlite3.connect("database.db")
    create_table = '''CREATE TABLE IF NOT EXISTS recipes (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    author TEXT NOT NULL,
                    recipe TEXT NOT NULL UNIQUE);'''
    cursor = connection.cursor()
    cursor.execute(create_table)
    connection.commit()
    connection.close()
    connection = sqlite3.connect("database.db")
    cursor = connection.cursor()
    ai_recipes = [
        {
            "recipe": "Spaghetti Carbonara",
            "author": "John Smith"
        },
        {
            "recipe": "Chicken Tikka Masala",
            "author": "Aisha Patel"
        },
        {
            "recipe": "Beef Stroganoff",
            "author": "Elena Ivanova"
        },
        {
            "recipe": "Vegetarian Chili",
            "author": "Emma Green"
        },
        {
            "recipe": "Shrimp Pad Thai",
            "author": "Somsak Chaiyut"
        },
        {
            "recipe": "Classic Margherita Pizza",
            "author": "Luigi Rossi"
        },
        {
            "recipe": "French Onion Soup",
            "author": "Marie Dupont"
        },
        {
            "recipe": "Sushi Rolls",
            "author": "Hiroshi Tanaka"
        },
        {
            "recipe": "Apple Pie",
            "author": "Susan Baker"
        },
        {
            "recipe": "Tacos al Pastor",
            "author": "Carlos Martinez"
        }
    ]
    for record in ai_recipes:
        cursor.execute("INSERT INTO recipes (author, recipe) VALUES (?, ?)",
                       (record["author"], record["recipe"]))
    connection.commit()
    connection.close()


def get_db_connection():
    connection = sqlite3.connect("database.db", timeout=10)
    connection.row_factory = sqlite3.Row
    return connection


def get_recipe(recipe_id):
    connection = get_db_connection()
    select_query = "SELECT * FROM recipes WHERE id=?"
    recipe = connection.execute(select_query, (recipe_id,)).fetchone()
    connection.close()
    return recipe


def limit():
    connection = get_db_connection()
    limit_query = "SELECT COUNT(*) FROM recipes"
    limit_number = connection.execute(limit_query).fetchone()[0]
    connection.close()
    return int(limit_number)


def create(author, recipe):
    connection = get_db_connection()
    create_query = "INSERT INTO recipes (author, recipe) VALUES (?, ?)"
    index = connection.execute(create_query, (author, recipe)).lastrowid
    connection.commit()
    connection.close()
    return index


def update(recipe_id, author, recipe):
    conn = get_db_connection()
    conn.execute("UPDATE quotes SET author=?, quote=? WHERE id=?",
                 (author, recipe, recipe_id))
    conn.commit()
    conn.close()
    return 202


def delete(recipe_id):
    connection = get_db_connection()
    connection.execute('DELETE FROM recipes WHERE id = ?', (recipe_id,))
    connection.commit()
    connection.close()
    return 200
