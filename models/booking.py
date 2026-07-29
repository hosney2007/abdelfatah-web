from extinsion import db

class Schedule(db.Model):
    __tablename__ ="bookings"
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user_id"), nullable=False )
    course_id = db.Column(db.Integer, db.ForeignKey("courses_id"), nullable=False )
    schedule_id = db.Column(db.Integer, db.ForeignKey("branches_id"), nullable=False )
    status = db.Column(db.String(20), default="pending" ,nullable=False)

user = db.relationship("User", backref="bookings")
course = db.relationship("Course", backref="bookings")
schedule = db.relationship("Schedule", backref="bookings")