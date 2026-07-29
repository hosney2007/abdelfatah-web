from flask import Flask , render_template
from config import Config
from models.user import User
from routes.auth import auth
from routes.courses import course
from routes.booking import booking
from models.branch import Branch
from routes.admin import admin
from extinsion import db, login_manager
import click
from werkzeug.security import generate_password_hash
from models.course import Course
app = Flask(__name__)
app.register_blueprint(auth)
app.register_blueprint(admin)
app.register_blueprint(course)
app.register_blueprint(booking)





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




app.config.from_object(Config)
db.init_app(app)
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


@app.route("/booking")
def booking():
    courses = Course.query.all()
    branches = Branch.query.all()
    return render_template('booking.html', name = 'booking', course=courses, branches=branches )   


@app.route("/contact")
def contact():
    return render_template('contact.html', name = 'contact')    


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=9000 ,debug=True)