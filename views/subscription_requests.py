import sqlite3
import json
from models import Subscription

def get_all_subscriptions():
  """gets all subscriptions"""
  with sqlite3.connect("./db.sqlite3") as conn:
    
    conn.row_factory = sqlite3.Row
    db_cursor = conn.cursor()
    db_cursor.execute("""
    SELECT
        s.id,
        s.follower_id,
        s.author_id,
        s.created_on
    FROM Subscriptions s
    """)

    subscriptions = []

    dataset = db_cursor.fetchall()

    for row in dataset:
        subscription = Subscription(row['id'], row['follower_id'], row['author_id'], row['created_on'])

        subscriptions.append(subscription.__dict__)

  return subscriptions


def create_subscription(new_subscription):
  """creates new subscription"""
  with sqlite3.connect("./db.sqlite3") as conn:
    
      db_cursor = conn.cursor()
      
      db_cursor.execute("""
      INSERT INTO Subscriptions
          ( follower_id, author_id, created_on )
      VALUES
          ( ?, ?, ?);
      """, (new_subscription['follower_id'], new_subscription['author_id'], new_subscription['created_on'], ))
      
      id = db_cursor.lastrowid
  
      new_subscription['id'] = id
  return new_subscription


def delete_subscription(id):
  """deletes subscription"""
  with sqlite3.connect("./db.sqlite3") as conn:
    
      db_cursor = conn.cursor()
      
      db_cursor.execute("""
      DELETE FROM Subscriptions
      WHERE id = ?
      """, (id, ))

