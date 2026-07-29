from flask import Blueprint, jsonify, request
from models.schedaule import Schedule
from models.branch import Branch
from models.course import Course

booking = Blueprint("booking" ,__name__)

@booking.route("/booking/schedules")
def get_schedules():
        
     course_id = request.args.get("course_id")
     mode = request.args.get("mode")
     branch_id = request.args.get("branch_id")
     query = Schedule.query.filter_by(
             course_id=course_id,
             mode=mode
        )
     if mode == "offline":
          query = query.filter_by(branch_id=branch_id)


     schedules = query.all()
     data = []
     for schedule in schedules:
          data.append({
               "id": schedule.id,

               "text" : f"{schedule.level} | "
                       f"{schedule.day1} {schedule.time1} - "
                       f"{schedule.day2} {schedule.time2} "
             })
     return jsonify(data)


