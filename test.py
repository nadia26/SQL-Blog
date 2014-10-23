from flask import Flask, render_template, request

test = Flask(__name__)

@test.route("/index",methods=["GET","POST"])
def index():
    if request.method=="GET":
        return render_template("index.html", postname="POST NAME")
    else:
        #actually post the thing
        #meaning add it to the database
        #go to new post's page



@test.route("/<postname>")
def postpage(postname):
    return render_template("post.html", title=postname, body="BODY")

if __name__=="__main__":
    test.debug=True
    test.run()
