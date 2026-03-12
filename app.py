from flask import Flask, jsonify, request

app = Flask(__name__)

# Sample student data
student = {
    "name": "Your Name",
    "grade": 10,
    "section": "Zechariah"
}

# Home route
@app.route("/")
def home():
    return "Welcome to my Flask API!"

# GET - view student info
@app.route("/student", methods=["GET"])
def get_student():
    return jsonify(student)

# POST - add student info
@app.route("/student/add", methods=["GET", "POST"])
def add_student():
    data = request.get_json(silent=True) or {}

    student["name"] = data.get("name", student["name"])
    student["grade"] = data.get("grade", student["grade"])
    student["section"] = data.get("section", student["section"])

    return jsonify({
        "message": "Student added successfully!",
        "student": student
    })

# PUT - update student info
@app.route("/student/update", methods=["GET", "PUT"])
def update_student():
    data = request.get_json(silent=True) or {}

    if "name" in data:
        student["name"] = data["name"]
    if "grade" in data:
        student["grade"] = data["grade"]
    if "section" in data:
        student["section"] = data["section"]

    return jsonify({
        "message": "Student information updated!",
        "student": student
    })

# DELETE - remove student
@app.route("/student/delete", methods=["GET", "DELETE"])
def delete_student():
    student.clear()

    return jsonify({
        "message": "Student record deleted!"
    })

if __name__ == "__main__":
    app.run()
