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
    

@test.route("/post/<title>",methods=["GET","POST"])
def post(title):
    body = request.form.get("post",None)
    if len(backend.getPosts(title))== 0:
        backend.addPost(title,body)
    else:
        body = backend.getPosts(title)
        commments = backend.getComments(title)
    
    if request.method == "GET":
        if len(backend.getPosts(title))== 0:
            render_template("error.html")
        else:
            body = backend.getPosts(title)
            commments = backend.getComments(title)
            return render_template("post.html", title = title, post = body, comments = comments)
    else:
        
        if len(backedng.getPosts(title))==0:
            backend.addPost(title,body)
        post = request.args.get("Post",None)
        comments = backend.getComments(title)
        if title == None:
            render_template("error.html")
        else:
            backend.addPost(title)
        return render_template("post.html", title = title, post = body, comments = comments)
        

if __name__=="__main__":
    test.debug=True
    test.run()






