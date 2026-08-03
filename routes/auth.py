from flask import Blueprint, render_template, request, redirect, url_for
from werkzeug.security import generate_password_hash , check_password_hash
from flask_login import login_user, logout_user, current_user, login_required
from models.booking import Booking
from models.purchase import Purchase



from extinsion import db
from models.user import User

auth = Blueprint("auth" ,__name__)

#=========REGISTER======///
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
    return render_template("register.html", name="Register")

#=========LOGIN========////
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
    return render_template("login.html", name="Login")

#======DASHBOARD=====///
@auth.route("/dashboard")
@login_required
def dashboard():

    # بيانات الطالب
    user = current_user

    # الكورسات المسجلة (Recorded Courses)
    purchases = Purchase.query.filter_by(
        user_id=current_user.id,
        status="approved"
    ).all()

    # جميع الحجوزات (Offline + Online)
    bookings = Booking.query.filter_by(
        id=current_user.id
    ).order_by(Booking.id.desc()).all()

    # إحصائيات
    total_recorded = len(purchases)
    total_bookings = len(bookings)

    pending_bookings = Booking.query.filter_by(
        id=current_user.id,
        status="pending"
    ).count()

    approved_bookings = Booking.query.filter_by(
        id=current_user.id,
        status="approved"
    ).count()

    return render_template(
        "dashboard.html",
        user=user,
        purchases=purchases,
        bookings=bookings,
        total_recorded=total_recorded,
        total_bookings=total_bookings,
        pending_bookings=pending_bookings,
        approved_bookings=approved_bookings
    )






#=====LOGOUT==//
@auth.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("auth.login"))            

