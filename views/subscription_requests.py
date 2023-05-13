import sqlite3
import json
from models import Subscription, Post

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

def get_all_subscription_posts(follower_id, author_id):
  # author_id on subscriptions is the user_id of posts 
  
  """gets posts of all user's subscriptions"""
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
    WHERE s.follower_id = ?
    """, ( follower_id, ))
    
    subscriptions = []
    dataset = db_cursor.fetchall()
    
    for row in dataset:
      subscription = Subscription(row['id'], row['follower_id'], row['author_id'], row['created_on'])

      subscriptions.append(subscription.__dict__)
      
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
      WHERE p.user_id = ?
      """, ( author_id, ))
    
    posts = []
    dataset = db_cursor.fetchall()
    
    for row in dataset:
      post = Post(row['id'], row['user_id'], row['category_id'], row['title'], row['publication_date'], row['image_url'], row['content'], row['approved'])
      
      posts.append(post.__dict__)

  return posts
    
    
