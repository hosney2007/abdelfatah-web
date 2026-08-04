from flask import Flask , render_template, redirect,request,url_for,flash
from config import Config
from models.user import User
from routes.auth import auth
from routes.courses import course
from routes.scheddules import schedule
from routes.recorded import recorded
from routes.booking import booking
from models.booking import Booking
from models.branch import Branch
from routes.admin import admin
from extinsion import db, login_manager, mail
import click
from werkzeug.security import generate_password_hash
from models.course import Course
app = Flask(__name__)
app.register_blueprint(auth)
app.register_blueprint(admin)
app.register_blueprint(course)
app.register_blueprint(booking)
app.register_blueprint(schedule)
app.register_blueprint(recorded)
import os






@app.cli.command("create-admin")
@click.option("--name", prompt="admin name")
@click.option("--email", prompt="admin email")
@click.option("--password", prompt=True, hide_input=True, confirmation_prompt=True)
def create_admin(name,email,password):
    existing_user = User.query.filter_by(email=email).first()
    if existing_user:
        print("Email already registered.")
        return
    admin = User(
         name=name,
         email=email,
         password=generate_password_hash(password),
         role="admin"
     )
    db.session.add(admin)
    db.session.commit()
    print("Admin account crated successfuly")



app.config["SECRET_KEY"] = "YOUR SECRET KEY"
app.config.from_object(Config)
os.makedirs(app.config["UPLOAD_FOLDER"], exist_ok=True)
db.init_app(app)
mail.init_app(app)
login_manager.init_app(app)
login_manager.login_view = "auth.login"
@login_manager.user_loader
def load_user(user_id):
    return db.session.get(User, int(user_id))

    
with app.app_context():
    db.create_all()




@app.route('/')
def home():
    return render_template('index.html', name = 'Home')

@app.route("/about")
def about():
    return render_template('about.html', name = 'ABOUT')    


@app.route("/courses")
def curses():
    return render_template('courses.html', name = 'courses')    


@app.route("/booking", methods=["POST", "GET"])
def booking():
    if request.method == "POST":
         booking=Booking(
          student_name = request.form["student_name"],
          student_number = request.form["student_number"],
          parent_number = request.form["parent_number"],
          grade = request.form["grade"],
          mode = request.form["mode"],
          course_id = request.form["exam"],
          branch_id = request.form.get("branch_id"),
          schedule_id = request.form["schedule_id"],
         )
         db.session.add(booking)
         db.session.commit()
         flash("your booking has been confirmed")
         return redirect(url_for("booking"))  
    courses = Course.query.all()
    branches = Branch.query.all()
    return render_template('booking.html', name = 'booking', course=courses, branches=branches )   


@app.route("/contact")
def contact():
    return render_template('contact.html', name = 'contact')    


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=9000 ,debug=True)