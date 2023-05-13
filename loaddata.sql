CREATE TABLE "Users" (
  "id" INTEGER PRIMARY KEY AUTOINCREMENT,
  "first_name" varchar,
  "last_name" varchar,
  "email" varchar,
  "bio" varchar,
  "username" varchar,
  "password" varchar,
  "profile_image_url" varchar,
  "created_on" date,
  "active" bit
);

CREATE TABLE "DemotionQueue" (
  "action" varchar,
  "admin_id" INTEGER,
  "approver_one_id" INTEGER,
  FOREIGN KEY(`admin_id`) REFERENCES `Users`(`id`),
  FOREIGN KEY(`approver_one_id`) REFERENCES `Users`(`id`),
  PRIMARY KEY (action, admin_id, approver_one_id)
);


CREATE TABLE "Subscriptions" (
  "id" INTEGER PRIMARY KEY AUTOINCREMENT,
  "follower_id" INTEGER,
  "author_id" INTEGER,
  "created_on" date,
  FOREIGN KEY(`follower_id`) REFERENCES `Users`(`id`),
  FOREIGN KEY(`author_id`) REFERENCES `Users`(`id`)
);

CREATE TABLE "Posts" (
  "id" INTEGER PRIMARY KEY AUTOINCREMENT,
  "user_id" INTEGER,
  "category_id" INTEGER,
  "title" varchar,
  "publication_date" date,
  "image_url" varchar,
  "content" varchar,
  "approved" bit,
  FOREIGN KEY(`user_id`) REFERENCES `Users`(`id`)
);

CREATE TABLE "Comments" (
  "id" INTEGER PRIMARY KEY AUTOINCREMENT,
  "post_id" INTEGER,
  "author_id" INTEGER,
  "content" varchar,
  FOREIGN KEY(`post_id`) REFERENCES `Posts`(`id`),
  FOREIGN KEY(`author_id`) REFERENCES `Users`(`id`)
);

CREATE TABLE "Reactions" (
  "id" INTEGER PRIMARY KEY AUTOINCREMENT,
  "label" varchar,
  "image_url" varchar
);

CREATE TABLE "PostReactions" (
  "id" INTEGER PRIMARY KEY AUTOINCREMENT,
  "user_id" INTEGER,
  "reaction_id" INTEGER,
  "post_id" INTEGER,
  FOREIGN KEY(`user_id`) REFERENCES `Users`(`id`),
  FOREIGN KEY(`reaction_id`) REFERENCES `Reactions`(`id`),
  FOREIGN KEY(`post_id`) REFERENCES `Posts`(`id`)
);

CREATE TABLE "Tags" (
  "id" INTEGER PRIMARY KEY AUTOINCREMENT,
  "label" varchar
);

CREATE TABLE "PostTags" (
  "id" INTEGER PRIMARY KEY AUTOINCREMENT,
  "post_id" INTEGER,
  "tag_id" INTEGER,
  FOREIGN KEY(`post_id`) REFERENCES `Posts`(`id`),
  FOREIGN KEY(`tag_id`) REFERENCES `Tags`(`id`)
);

CREATE TABLE "Categories" (
  "id" INTEGER PRIMARY KEY AUTOINCREMENT,
  "label" varchar
);

CREATE TABLE "SubscriptionPosts" (
  "id" INTEGER PRIMARY KEY AUTOINCREMENT,
  "subscription_id" INTEGER,
  "post_id" INTEGER,
  FOREIGN KEY(`subscription_id`) REFERENCES `Subscriptions`(`id`),
  FOREIGN KEY(`post_id`) REFERENCES `Posts`(`id`)
);

INSERT INTO Categories ('label') VALUES ('News');
INSERT INTO Tags ('label') VALUES ('JavaScript');
INSERT INTO Reactions ('label', 'image_url') VALUES ('happy', 'https://pngtree.com/so/happy');

INSERT INTO Categories ('label') VALUES ('Opinion');
INSERT INTO Categories ('label') VALUES ('Random');

INSERT INTO Users VALUES (null, 'Ryan', 'Bigelow', 'ryan@nss.com', 'yadda yadda', 'ryan', 'password', 'image.com', null, null);
INSERT INTO Users VALUES (null, 'Allison', 'Blumenthal', 'allison@nss.com', 'blah blah blah', 'allison', '123cookie', 'picture.com', null, null);
INSERT INTO Users VALUES (null, 'Erin', 'Stephens', 'erin@nss.com', 'ok', 'erin', 'trickortreat', 'photo.com', null, null);
INSERT INTO Users VALUES (null, 'DeDe', 'Hill', 'deandre@nss.com', 'yea na, na na yea', 'dede', 'motomotomoto', 'moto.com', null, null);

INSERT INTO Subscriptions VALUES (null, 1, 2, CURRENT_DATE);
INSERT INTO Subscriptions VALUES (null, 2, 3, CURRENT_DATE);
INSERT INTO Subscriptions VALUES (null, 3, 4, CURRENT_DATE);
INSERT INTO Subscriptions VALUES (null, 4, 1, CURRENT_DATE);


INSERT INTO Posts VALUES (null, 1, 1, 'Job Growth In Tech', CURRENT_DATE, 'image.com', 'news', true);
INSERT INTO Posts VALUES (null, 2, 2, 'NSS Is Great', CURRENT_DATE, 'nss.com', 'info', true);
INSERT INTO Posts VALUES (null, 3, 3, 'I cannot see my forehead', CURRENT_DATE, 'damn.com', 'shower thoughts', true);
INSERT INTO Posts VALUES (null, 4, 1, 'New Developments in AI', CURRENT_DATE, 'news.com', 'news', true);

INSERT INTO Comments VALUES (null, 1, 2, 'Great news!');
INSERT INTO Comments VALUES (null, 2, 3, 'tru');
INSERT INTO Comments VALUES (null, 3, 4, 'wait yeah...');
INSERT INTO Comments VALUES (null, 4, 1, 'Uh oh!');

INSERT INTO Tags VALUES (null, 'Education');
INSERT INTO Tags VALUES (null, 'Random');
INSERT INTO Tags VALUES (null, 'AI');

INSERT INTO PostTags VALUES (null, 1, 1);
INSERT INTO PostTags VALUES (null, 2, 2);
INSERT INTO PostTags VALUES (null, 3, 3);
INSERT INTO PostTags VALUES (null, 4, 4);

INSERT INTO SubscriptionPosts VALUES (null, 1, 1);
INSERT INTO SubscriptionPosts VALUES (null, 2, 2);


-- test selects

SELECT 
    sp.id,
    sp.subscription_id,
    sp.post_id,
    s.follower_id,
    s.author_id,
    s.created_on,
    p.user_id,
    p.category_id,
    p.title,
    p.publication_date,
    p.image_url,
    p.content,
    p.approved
FROM SubscriptionPosts sp
JOIN subscriptions s
      ON s.id = sp.subscription_id
JOIN posts p
      ON p.id = sp.post_id
