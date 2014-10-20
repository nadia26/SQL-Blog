import sqlite3 as sqlite
com = sqlite.connect("test.db")
c = com.cursor()
q = "CREATE TABLE POSTS(body TEXT, title TEXT)"
c.execute(q)
q = "CREATE TABLE COMMENTS(comments TEXT, title TEXT)"
c.execute(q)
com.commit()
