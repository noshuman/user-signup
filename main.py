from flask import Flask, request, redirect, render_template
import cgi
app= Flask(__name__)
app.config ['DEBUG'] = True
@ app.route ("/", methods= ['POST'])

def error():
    username = request.form["username"] 
    password = request.form["password"]
    verifypassword = request.form["verifypassword"]
    email = request.form["email"]

    username_error = ""
    password_error = ""
    verifypassword_error = ""
    email_error = ""

    if len(username) == 0:
        username_error = "Please enter a username."

    if len(username)  <=3 or len(username) >=20:
       username_error = "Your username does not meet the length requirements, usernames must be at least 3 characters long and cannot exeed 20 charaters."

    if username.count(" ") != 0:
       username_error = "Spaces are invalid for usernames, please re-enter your username without any spaces."   

    if len(password) == 0:
       password_error = "Please enter a password"

    if len(password)  <=3 or len(password) >=20:
       password_error = "Your password does not meet the length requirements, usernames must be at least 3 characters long and cannot exeed 20 charaters."

    if password.count(" ") !=0: 
       pasword_error = "Spaces are invalid for passwords, please re-enter your password without any spaces"  

    if len(verifypassword) == 0:
       verifypassword_error = "Please verify your password."

    if password != verifypassword:
       password_error ="Your entry does not match your password entry, please re-enter your password."

    if len(email) == 0:
       email_error = ""
    else:

       if len(email) <=3 or len(email) >=20 or email.count("@") != 1 or email.count(".") != 1 or email.count(" ") != 0:
          email_error = "You have entered an invaild email, please make sure that you have entered a working email address."   

    if len(username_error) != 0 or len(password_error) !=0  or len(verifypassword_error) != 0 or len(email_error) != 0:
        return render_template("index.html", username_error=username_error, password_error=password_error, verifypassword_error=verifypassword_error, email_error=email_error)
    else: 
        return render_template("welcome.html", username=username)    

@ app.route("/")
def index():
    username = request.args.get("username")
    return render_template("index.html", username=username)

app.run()