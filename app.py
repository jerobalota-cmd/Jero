from flask import Flask, jsonify, request

app = Flask(__name__)

# Student data
student = {
    "name": "Your Name",
    "grade": 10,
    "section": "Zechariah"
}

# Home route
@app.route("/", methods=["GET"])
def home():
    return "Welcome to my Flask API!"

# GET student info
@app.route("/student", methods=["GET"])
def get_student():
    return jsonify(student)

# Add or update student info (works with GET for browser, POST for API)
@app.route("/student/add", methods=["GET", "POST"])
def add_student():
    data = request.get_json(silent=True) or {}
    student["name"] = data.get("name", student["name"])
    student["grade"] = data.get("grade", student["grade"])
    student["section"] = data.get("section", student["section"])
    return jsonify({
        "message": "Student added/updated successfully!",
        "student": student
    })

# Update student info
@app.route("/student/update", methods=["GET", "PUT"])
def update_student():
    data = request.get_json(silent=True) or {}
    student["name"] = data.get("name", student["name"])
    student["grade"] = data.get("grade", student["grade"])
    student["section"] = data.get("section", student["section"])
    return jsonify({
        "message": "Student information updated!",
        "student": student
    })

# Delete student info
@app.route("/student/delete", methods=["GET", "DELETE"])
def delete_student():
    student.clear()
    return jsonify({
        "message": "Student record deleted!"
    })

if __name__ == "__main__":
    app.run()
