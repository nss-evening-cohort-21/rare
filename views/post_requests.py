import sqlite3
import json
from models import Post

def get_all_posts():
    # Open a connection to the database
    with sqlite3.connect("./db.sqlite3") as conn:

        # Just use these. It's a Black Box.
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        # Write the SQL query to get the information you want
        db_cursor.execute("""
        SELECT
            p.id,
            p.user_id,
            p.category_id,
            p.title,
            p.publication_date,
            p.image_url,
            p.content,
            p.approved
        FROM Posts p
        """)

        # Initialize an empty list to hold all category representations
        posts = []

        # Convert rows of data into a Python list
        dataset = db_cursor.fetchall()

        for row in dataset:

            # Create an animal instance from the current row
            post = Post(row['id'], row['user_id'], row['category_id'], row['title'], row['publication_date'], row['image_url'], row['content'], row['approved'])

            # Add the dictionary representation of the animal to the list
            posts.append(post.__dict__)

    return posts

def get_single_post(id):
    with sqlite3.connect("./db.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
        SELECT
            p.id,
            p.user_id,
            p.category_id,
            p.title,
            p.publication_date,
            p.image_url,
            p.content,
            p.approved
        FROM Posts p
        WHERE p.id = ?
        """, ( id, ))

        # Load the single result into memory
        data = db_cursor.fetchone()

        # Create an category instance from the current row
        post = Post(data['id'], data['user_id'], data['category_id'], data['title'], data['publication_date'], data['image_url'], data['content'], data['approved'])

        return post.__dict__

def create_post(new_post):
    '''creates new post'''
    with sqlite3.connect("./db.sqlite3") as conn:
        db_cursor = conn.cursor()
        db_cursor.execute("""
        INSERT INTO Posts
            ( user_id, category_id, title, publication_date, image_url, content, approved )
        VALUES
            ( ?, ?, ?, ?, ?, ?, ?);
        """, (new_post['user_id'], new_post['category_id'], new_post['title'], new_post['publication_date'], new_post['image_url'], new_post['content'], new_post['approved'], ))
        
        id = db_cursor.lastrowid
    
        new_post['id'] = id
    return new_post

def delete_post(id):
    with sqlite3.connect("./db.sqlite3") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        DELETE FROM Posts
        WHERE id = ?
        """, (id, ))

def update_post(id, new_post):
    with sqlite3.connect("./db.sqlite3") as conn:
        db_cursor = conn.cursor()
        db_cursor.execute("""
        UPDATE Posts
            SET
                user_id = ?,
                category_id = ?,
                title = ?,
                publication_date = ?,
                image_url = ?,
                content = ?,
                approved = ?
        WHERE id = ?
        """, (new_post['user_id'], new_post['category_id'], new_post['title'], new_post['publication_date'], new_post['image_url'], new_post['content'], new_post['approved'], id, ))
        
        rows_affected = db_cursor.rowcount
    
    if rows_affected == 0:
        return False
    else:
        return True
    
