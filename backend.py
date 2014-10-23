import sqlite3
import csv
import time

com= sqlite3.connect('test.db')
c=com.cursor()
'''
BASE="INSERT INTO posts VALUES('%(title)s','%(body)s')"
for l in csv.DictReader(open('posts.csv')):
    #print l
    q = BASE%l
    #print q
    c.execute(q)

BASE="""
INSERT INTO comments
       VALUES('%(title)s','%(comment)s')
"""
for l in csv.DictReader(open('comments.csv')):
    q = BASE%l
    #print q
    c.execute(q)

com.commit()

'''


def addPost(title, body):
    q = "INSERT INTO posts VALUES('" + title + "','" + body + "','" + str(time.time()) + "')"
    print q
    c.execute(q)
    com.commit()

def addComment(title, comment):
    q = "INSERT INTO comments VALUES('" + title + "','" + comment + "','" + str(time.time()) + "')"
    print q
    c.execute(q)
    com.commit()


def getPosts(title):
    '''returns a one-element array containing a tuple (body, timestamp)
    '''
    q = "SELECT * FROM posts WHERE posts.title='" + title+"'"
    posts = c.execute(q)
    com.commit()
    temp = [x[1:3] for x in posts]
    return temp


def getComments(title): #need to add sanitization on add and get: sanitize at the beginning of add and in temp
    #but tuples are immutable, so put it in the list comprehension perhaps? not really sure, may need to do more stuff. D:
    '''returns an array of tuples (comment, timestamp)
    '''
    q = "SELECT * FROM comments WHERE comments.title='" + title + "'"
    comments = c.execute(q)
    com.commit()
    temp = [x[1:3] for x in comments]
    return timeSort(temp)
#    return comments

def timeSort(blurbs): #blurps is an array of tuples, with the first element in the tuple being the text and the second being the time
    blurbs = sorted(blurbs, key = lambda tstamp: tstamp[1])
    
    return blurbs

if (__name__ == '__main__'):
    addPost('pieeeeeeeeeeeeeeeeeeeeeeeee', 'I love pie!')
    time.sleep(1)
    addPost('testing...', 'Is anybody here?')
    time.sleep(1)
    addComment('pieeeeeeeeeeeeeeeeeeeeeeeee', 'need to sanitize commas at least')
    time.sleep(1)
    addComment('pieeeeeeeeeeeeeeeeeeeeeeeee', 'cake is better')
    time.sleep(1)
    addComment('testing...', 'testing123')
    time.sleep(1)
    
    a = getPosts('testing...')
    b = getComments('pieeeeeeeeeeeeeeeeeeeeeeeee')
    #print a
    print a
    print b
    

