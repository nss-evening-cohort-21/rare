import sqlite3
import json
from models import Subscription

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
