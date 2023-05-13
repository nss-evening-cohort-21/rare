# import sqlite3
# import json
# from models import SubscriptionPost, Subscription, Post

# def get_all_subscription_posts():
#   # author_id on subscriptions is the user_id of posts 
  
  
#   def get_subscriptions_by_follower_id(follower_id):
#     """gets subscriptions by follower_id"""
#     with sqlite3.connect("./db.sqlite3") as conn:
      
#       conn.row_factory = sqlite3.Row
#       db_cursor = conn.cursor()
      
#       db_cursor.execute("""
#       SELECT
#           s.author_id
#       FROM Subscriptions s
#       WHERE s.follower_id = ?
#       """, ( follower_id, ))          
  
#     subscription_author_ids = []
    
#     dataset = db_cursor.fetchall()
    
#     for row in dataset:
#        subscription = Subscription(row['id'], row['author_id'])
       
#        subscription_author_ids.append(subscription.__dict__)
       
#     for author_id in subscription_author_ids:
      
       
       
       
       
       
       
  
#     return subscription_author_ids
  
  
    
  
  
#   def get_posts_by_subscriptions():
#     """gets posts of user's subscriptions"""
#     with sqlite3.connect("./db.sqlite3") as conn:
      
#       conn.row_factory = sqlite3.Row
#       db_cursor = conn.cursor()
      
#       # db_cursor.execute("""
      
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
#   """gets posts of all user's subscriptions"""
#   with sqlite3.connect("./db.sqlite3") as conn:
    
#     conn.row_factory = sqlite3.Row
#     db_cursor = conn.cursor()
    
#     db_cursor.execute("""
#     SELECT 
#         sp.id,
#         sp.subscription_id,
#         sp.post_id,
#         s.follower_id,
#         s.author_id,
#         s.created_on,
#         p.user_id,
#         p.category_id,
#         p.title,
#         p.publication_date,
#         p.image_url,
#         p.content,
#         p.approved
#     FROM SubscriptionPosts sp
#     JOIN subscriptions s
#           ON s.id = sp.subscription_id
#     JOIN posts p
#           ON p.id = sp.post_id
#     """)
    
#     subscription_posts = []
    
#     dataset = db_cursor.fetchall()
    
#     for row in dataset:
#       subscription_post = SubscriptionPost(row['id'], row['subscription_id'], row['post_id'])
      
#       subscription = Subscription(row['id'], row['follower_id'], row['author_id'], row['created_on'])
      
#       post = Post(row['id'], row['user_id'], row['category_id'], row['title'], row['publication_date'], row['image_url'], row['content'], row['approved'])
      
#       subscription_post.post = post.__dict__

#       subscription_posts.append(subscription_post.__dict__)

#   return subscription_posts

    
    
