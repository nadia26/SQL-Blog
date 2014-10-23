from flask import Flask, render_template, request

import backend
test = Flask(__name__)


@test.route("/",methods=["GET","POST"])
@test.route("/index",methods=["GET","POST"])
def index():
    posts = backend.getAllPosts()
    
    if request.method=="GET":
        return render_template("index.html", posts=posts)
        '''
    else:
        #not really gonna be this
        return render_template("index.html", postname="POST NAME")
        #actually post the thing
        #meaning add it to the database
        #go to new post's page
        return render_template("index.html", postname="POST NAME")
        '''
    

@test.route("/post/<title>",methods=["GET","POST"])
def post(title):
    title = request.args.get("title",None)
    post = request.args.get("Post",None)
    if request.method == "GET":
        return render_template("post.html", title = title, post = post)

if __name__=="__main__":
    test.debug=True
    test.run()






