from flask import Flask, jsonify, request

app = Flask(__name__)

student = {
    "name": "Your Name",
    "grade": 10,
    "section": "Zechariah"
}

@app.route("/", methods=["GET"])
def home():
    return "Welcome to my Flask API!"

@app.route("/student", methods=["GET"])
def get_student():
    return jsonify(student)

@app.route("/student/add", methods=["POST"])
def add_student():
    data = request.get_json()
    student["name"] = data.get("name", student["name"])
    student["grade"] = data.get("grade", student["grade"])
    student["section"] = data.get("section", student["section"])
    return jsonify({"message": "Student added/updated!", "student": student})

@app.route("/student/update", methods=["PUT"])
def update_student():
    data = request.get_json()
    student["name"] = data.get("name", student["name"])
    student["grade"] = data.get("grade", student["grade"])
    student["section"] = data.get("section", student["section"])
    return jsonify({"message": "Student updated!", "student": student})

@app.route("/student/delete", methods=["DELETE"])
def delete_student():
    student.clear()
    return jsonify({"message": "Student deleted!"})

if __name__ == "__main__":
    app.run()
