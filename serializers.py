from settings  import *
from models import Employee,Team,Note

class EmployeeSchema(ma.Schema):
    class Meta:
        fields = ("id", "fullname","email","date_of_birth","teams","annual_salary_inr","annual_salary_usd")
        model = Employee

employee_schema = EmployeeSchema()
employees_schema = EmployeeSchema(many=True)


class TeamSchema(ma.Schema):
    employees = ma.Nested(EmployeeSchema,many=True)
    class Meta:
        fields = ("id", "team_name","employees")
        model = Team

team_schema = TeamSchema()
teams_schema = TeamSchema(many=True)

class NoteSchema(ma.Schema):
    class Meta:
        fields = ("id", "content","date")
        model = Note

note_schema = NoteSchema()
notes_schema = NoteSchema(many=True)