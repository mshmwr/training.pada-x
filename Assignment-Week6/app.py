from flask import Flask, render_template, request, redirect, session, url_for
import mysql.connector

app = Flask(__name__, static_folder="img", static_url_path="/")
app.secret_key = "123"

# DB
mydb = mysql.connector.connect(host="localhost",
                               user="root",
                               password="",
                               database="myusers")
mycursor = mydb.cursor()


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/member")
def member():
    username = request.args["username"]
    name = session.get("username")
    if name:
        return render_template("member.html", username=name)
    else:
        return redirect("/")


@app.route("/error")
def error():
    msg = request.args["message"]
    return render_template("error.html", message=msg)


# 註冊頁面、登入頁面、登出頁面
@app.route("/signup")
def signup():
    return render_template("signUp.html")


@app.route("/signin")
def signin():
    return render_template("signIn.html")


@app.route("/signout")
def signout():
    session["username"] = False
    return redirect("/")


# 註冊帳密、驗證帳密
@app.route("/register", methods=["POST"])
def register():
    name = request.form["name"]
    username = request.form["username"]
    password = request.form["password"]

    # Check the username is registered or not
    sql = "SELECT * FROM users WHERE username = %s"
    adr = (username, )
    mycursor.execute(sql, adr)
    result = mycursor.fetchall()

    if len(result) != 0:
        errMsg = "帳號已經被註冊"
        return redirect(url_for('error', message=errMsg))
    else:
        sql = "INSERT INTO users (name, username, password) VALUES (%s, %s, %s)"
        val = (name, username, password)
        mycursor.execute(sql, val)
        mydb.commit()
        return redirect("/")


@app.route("/verify", methods=["POST"])
def verify():

    username = request.form["username"]
    password = request.form["password"]
    sql = "SELECT * FROM users WHERE username = %s and password= %s"
    adr = (username, password)
    mycursor.execute(sql, adr)
    result = mycursor.fetchall()
    if len(result) == 1:
        username = result[0][1]
        session["username"] = username
        return redirect(url_for('member', username=username))
    else:
        errMsg = "帳號或密碼輸入錯誤"
        return redirect(url_for('error', message=errMsg))


if __name__ == "__main__":
    app.run(port=3001)
