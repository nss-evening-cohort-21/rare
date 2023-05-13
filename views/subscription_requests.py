import sqlite3
import json
from models import Subscription, Post
from .post_requests import get_post_by_user

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
      
def get_subscriptions_by_follower_id(follower_id):
  """gets all subscription posts"""
  with sqlite3.connect("./db.sqlite3") as conn:
    
    conn.row_factory = sqlite3.Row
    db_cursor = conn.cursor()
    db_cursor.execute("""
    SELECT 
        s.id,
        s.follower_id,
        s.author_id,
        s.created_on,
        s.post_id
    FROM subscriptions s
    WHERE s.follower_id = ?
    """, ( follower_id, ))
    
    follower_subscriptions = []
    subscription_posts = []
    
    dataset = db_cursor.fetchall()
    
    for row in dataset:
      subscription = Subscription(row['id'], row['follower_id'], row['author_id'], row['created_on'], row['post_id'])
      
      subscription_author_id = subscription.author_id
      
      subscription_posts.append(get_post_by_user(subscription_author_id))
        
      subscription.post = subscription_posts
      
      follower_subscriptions.append(subscription.__dict__)
       
  return follower_subscriptions

# def get_all_subscription_posts():
#   """gets all subscription posts"""
#   with sqlite3.connect("./db.sqlite3") as conn:
    
#     conn.row_factory = sqlite3.Row
#     db_cursor = conn.cursor()
#     db_cursor.execute("""
#     SELECT
#         s.id,
#         s.follower_id,
#         s.author_id,
#         s.created_on,
#         s.post_id subscription_post_id,
#         p.id post_id,
#         p.user_id post_user_id,
#         p.category_id post_category_id,
#         p.title post_title,
#         p.publication_date post_publication_date,
#         p.image_url post_image_url,
#         p.content post_content,
#         p.approved post_approved
#     FROM Subscriptions s
#     JOIN Posts p 
#     ON p.user_id = s.author_id
#     """)

#     subscriptions = []

#     dataset = db_cursor.fetchall()

#     for row in dataset:
#         subscription = Subscription(row['id'], row['follower_id'], row['author_id'], row['created_on'], row['post_id'])
        
#         post = Post(row['post_id'], row['post_user_id'], row['post_category_id'], row['post_title'], row['post_publication_date'], row['post_image_url'], row['post_content'], row['post_approved'])

#         subscription.post = post.__dict__
        
#         subscriptions.append(subscription.__dict__)

#   return subscriptions
