from flask import Flask, jsonify
from db import get_connection

app = Flask(__name__)

@app.route("/api/projects")
def get_projects():
    conn = get_connection()
    if not conn:
        return jsonify({"error": "DB connection failed"}), 500
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT id, title, description, tech_stack FROM projects")
    projects = cursor.fetchall()
    cursor.close()
    conn.close()
    return jsonify(projects)

if __name__ == "__main__":
    app.run(debug=True)