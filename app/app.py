from flask import Flask, request, jsonify, render_template, redirect
import pyodbc, os
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)

def get_conn():
    return pyodbc.connect(os.getenv("AZURE_SQL_CONNECTIONSTRING"))

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/submit", methods=["POST"])
def submit():
    conn = get_conn()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO enrollments (full_name, student_id, email, course, year_level) VALUES (?, ?, ?, ?, ?)",
        (request.form["full_name"], request.form["student_id"], request.form["email"], request.form["course"], request.form["year_level"])
    )
    conn.commit()
    conn.close()
    return redirect("/results")

@app.route("/results")
def results():
    conn = get_conn()
    cursor = conn.cursor()
    cursor.execute("SELECT full_name, student_id, email, course, year_level, submitted_at FROM enrollments ORDER BY submitted_at DESC")
    columns = [col[0] for col in cursor.description]
    rows = [dict(zip(columns, row)) for row in cursor.fetchall()]
    conn.close()
    return render_template("results.html", enrollments=rows)

@app.route("/api/enroll", methods=["POST"])
def enroll():
    data = request.get_json()
    conn = get_conn()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO enrollments (full_name, student_id, email, course, year_level) VALUES (?, ?, ?, ?, ?)",
        (data["full_name"], data["student_id"], data["email"], data["course"], data["year_level"])
    )
    conn.commit()
    conn.close()
    return jsonify({"message": "Enrolled successfully"}), 201

@app.route("/api/enrollments", methods=["GET"])
def get_enrollments():
    conn = get_conn()
    cursor = conn.cursor()
    cursor.execute("SELECT full_name, student_id, email, course, year_level, submitted_at FROM enrollments ORDER BY submitted_at DESC")
    columns = [col[0] for col in cursor.description]
    rows = [dict(zip(columns, row)) for row in cursor.fetchall()]
    conn.close()
    return jsonify(rows), 200

if __name__ == "__main__":
    app.run(debug=True, port=5001)

