from flask import Blueprint, render_template, request, redirect, url_for
from werkzeug.security import generate_password_hash , check_password_hash
from flask_login import login_user, logout_user, current_user, login_required


from extinsion import db
from models.user import User

auth = Blueprint("auth" ,__name__)

@auth.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        password = request.form["password"]

        existing_user = User.query.filter_by(email=email).first()
        if existing_user:
            return "Email already registered"
        hashed_password = generate_password_hash(password)
        user = User(
            name=name,
            email=email,
            password=hashed_password
        )

        db.session.add(user)
        db.session.commit()
        return redirect(url_for("auth.login"))
    return render_template("register.html")
@auth.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]   
        user = User.query.filter_by(email=email).first()
        if user and check_password_hash(user.password, password):
            login_user(user)
            if user.role == "admin":
                return redirect(url_for("admin.admin_dashboard"))
            return redirect(url_for("auth.dashboard"))
        return "invaild email or password"
    return render_template("login.html")
@auth.route("/dashboard")
@login_required
def dashboard():
    return render_template("dashboard.html" ,user=current_user)


@auth.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("auth.login"))            

