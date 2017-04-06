from flask import Flask, jsonify, render_template, request
from pymongo import MongoClient

app = Flask(__name__)

client = MongoClient()
db = client.test

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/users")
def get_users():
    users_collection = db.usershackaton
    users = [user for user in users_collection.find()]
    for user in users:
        del user["_id"]
    return jsonify({"users": [user for user in users]})

@app.route("/user/<uid>")
def get_user(uid=None):
    users_collection = db.usershackaton
    user = users_collection.find_one({"id": int(uid)})
    del user["_id"]
    return jsonify({"user": user})

@app.route("/create_user", methods=['GET', 'POST'])
def create_user():
    if request.method == 'POST':
        print(request.form)
        return "Se creó!"
    else:
        return render_template('createuser.html')


if __name__ == "__main__":
    app.run()
