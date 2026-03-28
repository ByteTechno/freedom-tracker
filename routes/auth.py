from flask import Blueprint, render_template, request, redirect, session
from models import UserModel

auth_bp = Blueprint('auth', __name__)

@auth_bp.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form.get("username", "").strip()
        password = request.form.get("password", "").strip()

        if not username or not password:
            return "❌ Username and password cannot be empty."

        success, error = UserModel.create(username, password)
        if success:
            return redirect("/login")
        else:
            return f"❌ Registration error: {error}"

    return render_template("register.html")


@auth_bp.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        if username and password and UserModel.verify(username, password):
            session["username"] = username
            return redirect("/")
        
        return render_template("login.html", error="The username or password is incorrect")

    return render_template("login.html")


@auth_bp.route("/logout")
def logout():
    session.clear()
    return redirect("/login")
