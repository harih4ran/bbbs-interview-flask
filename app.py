from models import *
from serializers import *
from datetime import datetime

@app.route('/employees', methods=['GET'])
@cross_origin()
def employees():
    employee = Employee.query.all()
    if employee is None:
        return 'Employee not found', 404
    return employees_schema.dump(employee)


@app.route('/employee', methods=['POST'])
@cross_origin()
def create_employee():
    data = request.get_json()

    # date convertion
    date_str = data["date_of_birth"]
    date_of_birth = datetime.strptime(date_str, '%Y-%m-%d').date()

    # post request data into employee table

    employee = Employee(
        fullname = data['fullname'],
        date_of_birth = date_of_birth,
        email = data["email"],
        annual_salary_usd = data["annual_salary_usd"],
        annual_salary_inr = data["annual_salary_inr"]
    )
    db.session.add(employee)
    db.session.commit()

    # return inserted data as a json
    return employee_schema.dump(employee),201

@app.route('/employee/<int:id>', methods=['GET'])
@cross_origin()
def get_employee(id):
    employee = Employee.query.get(id)
    if employee is None:
        return 'Employee not found', 404
    return employee_schema.dump(employee),200

@app.route('/employee/<int:id>', methods=['PUT'])
@cross_origin()
def update_employee(id):
    employee = Employee.query.get(id)
    data = request.get_json()

    date_str = data["date_of_birth"]
    date_of_birth = datetime.strptime(date_str, '%Y-%m-%d').date()

    if employee is None:
        return 'Employee not found', 404

    employee.fullname = data['fullname']
    employee.date_of_birth = date_of_birth
    employee.email = data["email"]
    employee.annual_salary_usd = data["annual_salary_usd"]
    employee.annual_salary_inr = data["annual_salary_inr"]

    db.session.commit()
    return employee_schema.dump(employee),200

@app.route('/employee/<int:id>', methods=['DELETE'])
@cross_origin()
def delete_employee(id):
    employee = Employee.query.get(id)
    if employee is None:
        return 'Employee not found', 404
    db.session.delete(employee)
    db.session.commit()
    return '', 204

@app.route('/teams', methods=['GET'])
@cross_origin()
def teams():
    teams = Team.query.all()
    if teams is None:
        return 'Team not found', 404
    return teams_schema.dump(teams)


@app.route('/team', methods=['POST'])
@cross_origin()
def create_team():
    data = request.get_json()
    print(data)

    team = Team(
        team_name = data['team_name'],
    )
    
    for i in data["employees"]:
        emp = Employee.query.get(i)
        team.employees.append(emp)

    db.session.add(team)
    db.session.commit()

    # return inserted data as a json
    return team_schema.dump(team),201

@app.route('/team/<int:id>', methods=['GET'])
@cross_origin()
def get_team(id):
    team = Team.query.get(id)
    if team is None:
        return 'team not found', 404
    return team_schema.dump(team),200

@app.route('/team/<int:id>', methods=['PUT'])
@cross_origin()
def update_team(id):
    team = Team.query.get(id)
    data = request.get_json()

    for i in data["employees"]:
        emp = Employee.query.get(i)
        team.employees.append(emp)

    if team is None:
        return 'Team not found', 404

    team.team_name = data['team_name']

    db.session.commit()
    return team_schema.dump(team),200


@app.route('/team/<int:id>', methods=['DELETE'])
@cross_origin()
def delete_team(id):
    team = Team.query.get(id)
    if team is None:
        return 'Team not found', 404
    db.session.delete(team)
    db.session.commit()
    return '', 204


@app.route('/notes', methods=['GET'])
@cross_origin()
def notes():
    note = Note.query.all()
    if note is None:
        return 'note not found', 404
    return notes_schema.dump(note)


@app.route('/note', methods=['POST'])
@cross_origin()
def create_note():
    data = request.get_json()

    # date convertion
    date_str = data["date"]
    date = datetime.strptime(date_str, '%Y-%m-%d').date()

    # post request data into note table

    note = Note(
        content = data['content'],
        date = date,
    )
    db.session.add(note)
    db.session.commit()

    # return inserted data as a json
    return note_schema.dump(note),201

@app.route('/Note/<int:id>', methods=['GET'])
@cross_origin()
def get_note(id):
    Note = Note.query.get(id)
    if Note is None:
        return 'Note not found', 404
    return note_schema.dump(Note),200

@app.route('/note/<int:id>', methods=['PUT'])
@cross_origin()
def update_note(id):
    note = Note.query.get(id)
    data = request.get_json()

    date_str = data["date"]
    date = datetime.strptime(date_str, '%Y-%m-%d').date()

    if note is None:
        return 'Note not found', 404

    note.content = data['content']
    note.date = date

    db.session.commit()
    return note_schema.dump(note),200

@app.route('/note/<int:id>', methods=['DELETE'])
@cross_origin()
def delete_note(id):
    note = Note.query.get(id)
    if note is None:
        return 'Note not found', 404
    db.session.delete(note)
    db.session.commit()
    return '', 204


if __name__ == '__main__':
    app.run(debug=True)