import sqlite3
import csv

com= sqlite3.connect('test.db')
c=com.cursor()

BASE="INSERT INTO posts VALUES('%(title)s','%(body)s')"
for l in csv.DictReader(open('posts.csv')):
    print l
    q = BASE%l
    print q
    c.execute(q)

BASE="""
INSERT INTO comments
       VALUES('%(title)s','%(comment)s')
"""
for l in csv.DictReader(open('comments.csv')):
    q = BASE%l
    print q
    c.execute(q)

com.commit()

def getPosts(title):
    q = "SELECT * FROM posts WHERE posts.title='" + title+"'"
    posts = c.execute(q)
    com.commit()
    return posts

def addPost(title, body):
    q = "INSERT INTO posts VALUES('" + title + "','" + body + "')"
    print q
    c.execute(q)
    com.commit()

addPost('testing...', 'need to sanitize commas at least')

a = getPosts('testing...')
for x in a:
    print x
