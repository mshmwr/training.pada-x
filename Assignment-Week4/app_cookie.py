from flask import Flask, render_template, request, redirect, make_response
import time

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/member")
def member():
    name = request.cookies.get("username")
    if name:
        return render_template("member.html")
    else:
        return redirect("/")


@app.route("/error")
def error():
    return render_template("error.html")


@app.route("/signin", methods=["POST"])
def signin():
    username = request.form["username"]
    password = request.form["password"]
    if username == "test" and password == "test":
        resp = make_response(redirect("/member"))
        resp.set_cookie(key="username", value=username, expires=time.time() + 1 * 60)
        return resp
    else:
        return redirect("/error")


@app.route("/signout")
def signout():
    resp = make_response(redirect("/"))
    resp.set_cookie(key="username", value="", expires=0)
    return resp


if __name__ == "__main__":
    app.run(port=3000)
