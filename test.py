from flask import Flask, render_template, request

import backend
test = Flask(__name__)


@test.route("/",methods=["GET","POST"])
@test.route("/index",methods=["GET","POST"])
def index():
    posts = backend.getAllPosts()
    
    if request.method=="GET":
        return render_template("index.html", posts=posts)

    else:
        new_title = request.form['title']
        new_post = request.form['post']
        backend.addPost(new_title, new_post)
        posts = backend.getAllPosts()
        return render_template("index.html", posts=posts)
    
\
@test.route("/post/<title>",methods=["GET","POST"])
def post(title):
    comments = backend.getComments(title)
    post = backend.getPosts(title)
    if request.method == "POST":
        new_comment = request.form['comment']
        backend.addComment(title, new_comment)
        comments = backend.getComments(title)
        return render_template("post.html", title = title, post = post, comments = comments)
    elif request.method == "GET":
        return render_template("post.html", title = title, post = post, comments = comments)

if __name__=="__main__":
    test.debug=True
    test.run()






