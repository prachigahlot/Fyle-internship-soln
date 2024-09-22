# Fyle Backend Challenge





#Technologies 
Flask: For creating RESTful APIs.
SQLAlchemy: ORM for interacting with the database.
Marshmallow: For data serialization and validation.
Docker: For containerizing the application.

#API Endpoints
Principal APIs
GET /principal/assignments: List all submitted and graded assignments.
POST /principal/assignments/grade: Grade an assignment.
Teacher APIs
GET /teacher/assignments: List all assignments created by the teacher.
POST /teacher/assignments/grade: Grade a specific assignment.
Student APIs
GET /student/assignments: List all assignments for a student.
POST /student/assignments/submit: Submit an assignment for grading.

# for Missing API
made changes in core/apis/assignment/principal.py file 
made changes in server.py 
made changes in schema.py file created schema for teachers
made changes in __init__.py file


# For correcting error in the file
Added filter to the API of Assignment/Teachers  for checking condition that the assignment submitted to that teacher is deplayed
Added Filter to the API of Assignment/Teachers/grade for checking condition.






# List all assignments for a principal
curl -X GET http://127.0.0.1:8000/principal/assignments -H 'X-Principal: {"user_id":5, "principal_id":1}'

# Grade an assignment as a principal
curl -X POST http://127.0.0.1:8000/principal/assignments/grade -H 'X-Principal: {"user_id":5, "principal_id":1}' -d '{"id": 1, "grade": "A"}'

# List all assignments created by a teacher
curl -X GET http://127.0.0.1:8000/teacher/assignments -H 'X-Teacher: {"









## Who is this for?

This challenge is meant for candidates who wish to intern at Fyle and work with our engineering team. You should be able to commit to at least 6 months of dedicated time for internship.

## Why work at Fyle?

Fyle is a fast-growing Expense Management SaaS product. We are ~40 strong engineering team at the moment. 

We are an extremely transparent organization. Check out our [careers page](https://careers.fylehq.com) that will give you a glimpse of what it is like to work at Fyle. Also, check out our Glassdoor reviews [here](https://www.glassdoor.co.in/Reviews/Fyle-Reviews-E1723235.htm). You can read stories from our teammates [here](https://stories.fylehq.com).


## Challenge outline

**You are allowed to use any online/AI tool such as ChatGPT, Gemini, etc. to complete the challenge. However, we expect you to fully understand the code and logic involved.**

This challenge involves writing a backend service for a classroom. The challenge is described in detail [here](./Application.md)


## What happens next?

You will hear back within 48 hours from us via email. 


## Installation

1. Fork this repository to your github account
2. Clone the forked repository and proceed with steps mentioned below

### Install requirements

```
virtualenv env --python=python3.8
source env/bin/activate
pip install -r requirements.txt
```
### Reset DB

```
export FLASK_APP=core/server.py
rm core/store.sqlite3
flask db upgrade -d core/migrations/
```
### Start Server

```
bash run.sh
```
### Run Tests

```
pytest -vvv -s tests/

# for test coverage report
# pytest --cov
# open htmlcov/index.html
```
