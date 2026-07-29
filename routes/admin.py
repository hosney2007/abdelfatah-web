from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import  current_user, login_required
from extinsion import db
from models.course import Course
from models.branch import Branch
from models.schedaule import Schedule

admin = Blueprint("admin" ,__name__)
# dashboard
@admin.route("/admin")
@login_required
def admin_dashboard():
    if current_user.role != "admin":
        return "ACCESS DENIED", 403
    courses = Course.query.filter_by( is_active=True).all()
    return render_template("admin/admin-dashboard.html" ,user=current_user, course=courses)

#addd coueses

@admin.route("/admin/add-course", methods=["GET", "POST"])
@login_required
def add_course():
    if current_user.role != "admin":
        return "ACCESS DENIED", 403
    if request.method == "POST":

        title = request.form["title"]
        description = request.form["description"]
        course_type = request.form["course_type"]
        price = request.form.get("price")
        if price:
            price =float(price)
        else:
            price = None
        course = Course(
            title = title,
            description= description,
            course_type=course_type,
            price=price
        )  
        db.session.add(course)
        db.session.commit()
        return redirect(url_for("admin.admin_dashboard"))
    return render_template("admin/add-course.html")      

#edit courses

@admin.route("/admin/edit-course/<int:course_id>", methods=["GET", "POST"])
@login_required
def edit_course( course_id ):
    if current_user.role != "admin":
        return "ACCESS DENIED", 403
    course = Course.query.get_or_404(course_id)
    if request.method == "POST":

        course.title = request.form["title"]
        course.description = request.form["description"]
        course.course_type = request.form["course_type"]
        price = request.form.get("price")

        print("price:" ,course.price)

        if course.course_type == "recorded":
           if price:
            course.price =float(price)
           else:
               price = None
        else:
            course.price = None
        print("price:" ,course.price)
        db.session.commit()
        print("price:" ,course.price)
        return redirect(url_for("admin.admin_dashboard"))
    return render_template("admin/edit-course.html", course=course)   



@admin.route("/admin/delete-course/<int:course_id>", methods=["GET", "POST"])
@login_required
def delete_course( course_id ):
    if current_user.role != "admin":
        return "ACCESS DENIED", 403
    course = Course.query.get_or_404(course_id)
    db.session.delete(course)
    db.session.commit()
    return redirect(url_for("admin.admin_dashboard"))

#=============================================================================

@admin.route("/admin/add-group", methods=["GET", "POST"])
@login_required
def add_group():
    if current_user.role != "admin":
        return "ACCESS DENIED", 403
    courses = Course.query.all()
    branches = Branch.query.all()
    if request.method == "POST":

        course_id = request.form.get("course_id")
        level = request.form.get("level")
        mode = request.form.get("mode")
        branch_id = request.form.get("branch_id")
        day1 = request.form.get("day1")
        time1 = request.form.get("time1")
        day2 = request.form.get("day2")
        time2 = request.form.get("time2")
        if mode == "online":
            branch_id = None
        
    
        schedule = Schedule(
            course_id=course_id,
            level=level,
            mode=mode,
            branch_id=branch_id,
            day1=day1,
            time1=time1,
            day2=day2,
            time2=time2

        )  
        db.session.add(schedule)
        db.session.commit()
        return redirect(url_for("admin.admin_dashboard"))
    return render_template("admin/add-group.html", course=courses, branches=branches)      




@admin.route("/admin/add-branch", methods=["GET", "POST"])
@login_required
def add_branch():
    if current_user.role != "admin":
        return "ACCESS DENIED", 403
    if request.method == "POST":

        name = request.form["name"]
        branch = Branch(
            name=name
        )
            
        db.session.add(branch)
        db.session.commit()
        return redirect(url_for("admin.admin_dashboard"))
    return render_template("admin/add-branch.html")  