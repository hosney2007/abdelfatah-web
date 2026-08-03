from flask import Blueprint, render_template,redirect,url_for

from models.schedaule import Schedule
from extinsion import db

schedule = Blueprint("schedule", __name__)
#======= SHOW GROUPS===///
@schedule.route("/admin/schedule")
def show_schedules():
    schedules = Schedule.query.all()
    print(schedules)
    return render_template("admin/schedules.html" , schedule=schedules, name="Groups")

#=====DELTE GROUPS=======//
@schedule.route("/admin/schedule/<int:schedule_id>/delete")
def delete_schedule(schedule_id):
    schedule = Schedule.query.get_or_404(schedule_id)
    db.session.delete(schedule)
    db.session.commit()
    return redirect(url_for("schedule.show_schedules"))


