import sqlite3
import json
from models import Category


def get_single_category(id):
    with sqlite3.connect("./db.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
        SELECT
            c.id,
            c.label
        FROM Categories c
        WHERE c.id = ?
        """, ( id, ))

        # Load the single result into memory
        data = db_cursor.fetchone()

        # Create an category instance from the current row
        category = Category(data['id'], data['label'])

        return category.__dict__

def get_all_categories():
    # Open a connection to the database
    with sqlite3.connect("./db.sqlite3") as conn:

        # Just use these. It's a Black Box.
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        # Write the SQL query to get the information you want
        db_cursor.execute("""
        SELECT
            c.id,
            c.label
        FROM Categories c
        """)

        # Initialize an empty list to hold all category representations
        categories = []

        # Convert rows of data into a Python list
        dataset = db_cursor.fetchall()

        for row in dataset:

            # Create an animal instance from the current row
            category = Category(row['id'], row['label'])

            # Add the dictionary representation of the animal to the list
            categories.append(category.__dict__)

    return categories

def create_category(new_category):
    with sqlite3.connect("./db.sqlite3") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        INSERT INTO Categories
            ( label )
        VALUES
            ( ? );
        """, (new_category['label'],))

        # The `lastrowid` property on the cursor will return
        # the primary key of the last thing that got added to
        # the database.
        id = db_cursor.lastrowid

        # Add the `id` property to the animal dictionary that
        # was sent by the client so that the client sees the
        # primary key in the response.
        new_category['id'] = id


    return new_category
