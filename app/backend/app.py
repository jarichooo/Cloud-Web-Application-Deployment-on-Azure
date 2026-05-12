from flask import Flask, request, redirect, render_template
import pyodbc
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

def get_conn():
    conn_str = os.getenv("AZURE_SQL_CONNECTIONSTRING")
    return pyodbc.connect(conn_str)

def init_db():
    conn = get_conn()
    cursor = conn.cursor()
    cursor.execute("""
        IF NOT EXISTS (SELECT * FROM sysobjects WHERE name='enrollments' AND xtype='U')
        CREATE TABLE enrollments (
            id INT IDENTITY PRIMARY KEY,
            full_name NVARCHAR(100),
            student_id NVARCHAR(20),
            course NVARCHAR(100),
            year_level INT,
            submitted_at DATETIME DEFAULT GETDATE()
        )
    """)
    conn.commit()
    conn.close()

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/submit", methods=["POST"])
def submit():
    full_name = request.form["full_name"]
    email = request.form["email"]
    student_id = request.form["student_id"]
    course = request.form["course"]
    year_level = request.form["year_level"]

    conn = get_conn()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO enrollments (full_name, student_id, email, course, year_level) VALUES (?, ?, ?, ?, ?)",
        (full_name, student_id, email, course, year_level)
    )
    conn.commit()
    conn.close()
    return redirect("/results")

@app.route("/results")
def results():
    conn = get_conn()
    cursor = conn.cursor()
    cursor.execute("SELECT full_name, student_id, course, year_level, submitted_at FROM enrollments ORDER BY submitted_at DESC")
    rows = cursor.fetchall()
    conn.close()
    return render_template("results.html", enrollments=rows)

if __name__ == "__main__":
    init_db()
    app.run(debug=True)

