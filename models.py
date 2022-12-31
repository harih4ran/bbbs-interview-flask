from settings  import *

employee_team = db.Table('employee_team',
    db.Column('employee_id', db.Integer, db.ForeignKey('employee.id')),
    db.Column('team_id', db.Integer, db.ForeignKey('team.id'))
)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255))
    password = db.Column(db.String(255))
    role = db.Column(db.String(15))


class Employee(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user = db.Column('User', db.Integer, db.ForeignKey('user.id'))
    fullname = db.Column(db.String(50))
    date_of_birth = db.Column(db.Date)
    email = db.Column(db.String(255))
    annual_salary_inr = db.Column(db.Float)
    annual_salary_usd = db.Column(db.Float)
    

class Team(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    team_name = db.Column(db.String(255))
    user = db.Column('User', db.Integer, db.ForeignKey('user.id'))
    employees = db.relationship("Employee",secondary = employee_team,backref="employee")

class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    employee = db.Column('Employee', db.Integer, db.ForeignKey('employee.id'))
    content = db.Column(db.String(255))
    date = db.Column(db.Date)

with app.app_context():
    db.create_all()
