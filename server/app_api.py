from flask import Flask, jsonify, render_template, request
from pymongo import MongoClient
from random import randint

app = Flask(__name__)

client = MongoClient()
db = client.test


@app.route("/")
def hello():
    return "Hello World!"

@app.route("/users")
def get_users():
    users_collection = db.users
    users = [user for user in users_collection.find()]
    for user in users:
        del user["_id"]
    return jsonify({"users": [user for user in users]})

@app.route("/user/<uid>")
def get_user(uid=None):
    users_collection = db.users
    user = users_collection.find_one({"id": int(uid)})
    del user["_id"]
    return jsonify({"user": user})

@app.route('/teacher/<uid>')
def get_teacher(uid=None):
    teachers_collection = db.teachers
    users_collection = db.users
    teacher = teachers_collection.find_one({'id':int(uid)})
    user = users_collection.find_one({"id": int(uid)})
    teacher.update(user)
    del teacher['_id']
    return jsonify({'teacher': teacher})

@app.route('/teachers/<sigla>')
def get_teachers_by_course(sigla):
    courses_collection = db.courses
    teachers = db.teachers
    users_collection = db.users
    results = []
    course = courses_collection.find_one({'sigla':sigla})
    for teacher_id in course['teachers']:
        teacher = teachers.find_one({'id':int(teacher_id)})
        user = users_collection.find_one({"id": int(teacher_id)})
        teacher.update(user)
        del teacher['_id']
        results.append(teacher)
    return jsonify({"teachers": results})

@app.route('/silicitud/<course>/<teacher_id>/<student_id>')
def create_solicitude(course, teacher_id, student_id):
    id_solicitud = randint(00000000, 99999999)
    db.solicitudes.insert_one({'course':course, 'user_id':student_id,
                               'teacher_id':teacher_id,
                               'id': id_solicitud,
                               'state':'PENDING'})
    return jsonify({'id_solicitud':id_solicitud})

@app.route("/create_user", methods=['GET', 'POST'])
def create_user():
    if request.method == 'POST':
        print(request.form)
        return "Se creó!"
    else:
        return render_template('createuser.html')


if __name__ == "__main__":
    app.run()
