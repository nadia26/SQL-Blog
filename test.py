from flask import Flask, render_template, request

test = Flask(__name__)

@test.route("/index",methods=["GET","POST"])
def index():
    if request.method=="GET":
        return render_template("index.html")
    else:
        return render_template("post.html", title=request.form["title"])

@test.route("/post")
def postpage():
    return render_template("post.html", title="Title of Post")

if __name__=="__main__":
    test.debug=True
    test.run()
