from flask import Flask, render_template, request, redirect, make_response
import time
import hashlib

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/member")
def member():
    name = request.cookies.get("username")
    print("name: " + name)
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

        #  do encrypt
        m = hashlib.md5()  # 建立 MD5 物件
        data = "%s-%s" % (username, password)  # 要計算 MD5 雜湊值的資料
        m.update(data.encode("utf-8"))  # 先將資料編碼，再更新 MD5 雜湊值
        h = m.hexdigest()  # 取得 MD5 雜湊值

        resp.set_cookie(key="username", value=h, expires=time.time() + 1 * 60)
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
