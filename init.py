import sqlite3


com= sqlite3.connect('test.db')
c=com.cursor()
q = "CREATE TABLE posts(title TEXT UNIQUE, body TEXT)"
c.execute(q)
q = "CREATE TABLE comments(title TEXT, comment TEXT)"
c.execute(q)
com.commit()

