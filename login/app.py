
from flask import Flask, request, Response, url_for, session, redirect


app = Flask(__name__)
app.secret_key = "supersecret"


@app.route("/", methods=["GET","POST"])
def login():
    if request.method =="POST":
        username = request.form.get("username")
        password = request.form.get("password")
         
        if username =='admin' and password == '123':
            session['user'] = username #store in session
            return redirect(url_for("welcome"))
        else:
            return Response("in-valid credentials. try again", mimetype="text/plain")
        
    return"""
            <h2>Login Page</h2>
            <Form method = "POST">
            username: <input type="text" name="username"><br>
            password: <input type="text" name="password"><br>
            <input type = "submit" value = "login">
            </form>
"""


# welcome page after login
@app.route("/Welcome")
def welcome():
    if 'user' in session:
        return f""" 
        <h2>Welcome,{session['user']}!</h2>
        <a href={url_for("logout")}>logout</a>
"""
    return redirect(url_for("login"))


#logout
@app.route("/logout")
def logout():
    session.pop("user")    #session["user"] = "tanish"
    return redirect(url_for("login"))


if __name__ == "__main__":
    app.run(debug=True)