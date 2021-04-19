from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)


app.secret_key = "123"  # session 加密的密鑰


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/member")
def member():
    name = session.get("username")  # 取session
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
        session["username"] = "test"
        return redirect("/member")
    else:
        return redirect("/error")


@app.route("/signout")
def signout():
    session["username"] = False
    return redirect("/")


if __name__ == "__main__":
    app.run(port=3000)
