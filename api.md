curl -X POST -H "Content-Type: application/json" -d '{"fullname": "new one","date_of_birth":"2000-12-01","email":"demo@gmail.com"}'  http://127.0.0.1:5000/employee

curl -X PUT -H "Content-Type: application/json" -d '{"fullname": "updated"}'  http://127.0.0.1:5000/employee/1

curl -X DELETE -H "Content-Type: application/json" http://127.0.0.1:5000/employee/5


curl -X POST -H "Content-Type: application/json" -d '{"team_name": "new one"}'  http://127.0.0.1:5000/team

curl -X PUT -H "Content-Type: application/json" -d '{"team_name": "tech","employees":[1]}'  http://127.0.0.1:5000/team/1
