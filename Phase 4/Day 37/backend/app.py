from flask import Flask, request, jsonify
from db import get_connection
from werkzeug.security import generate_password_hash

app = Flask(__name__)

# CREATE — add a new project
@app.route("/projects", methods=["POST"])
def create_project():
    data = request.get_json()
    conn = get_connection()
    if not conn:
        return jsonify({"error": "DB connection failed"}), 500
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO projects (title, description, tech_stack) VALUES (%s, %s, %s)",
        (data["title"], data.get("description"), data.get("tech_stack"))
    )
    conn.commit()
    new_id = cursor.lastrowid
    cursor.close()
    conn.close()
    return jsonify({"id": new_id, "message": "Project created"}), 201

# READ — get all projects
@app.route("/api/projects", methods=["GET"])
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

# READ — get a single project by id
@app.route("/projects/<int:project_id>", methods=["GET"])
def get_project(project_id):
    conn = get_connection()
    if not conn:
        return jsonify({"error": "DB connection failed"}), 500
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT id, title, description, tech_stack FROM projects WHERE id = %s", (project_id,))
    project = cursor.fetchone()
    cursor.close()
    conn.close()
    if not project:
        return jsonify({"error": "Not found"}), 404
    return jsonify(project)

# UPDATE — edit an existing project
@app.route("/projects/<int:project_id>", methods=["PUT"])
def update_project(project_id):
    data = request.get_json()
    conn = get_connection()
    if not conn:
        return jsonify({"error": "DB connection failed"}), 500
    cursor = conn.cursor()
    cursor.execute(
        "UPDATE projects SET title=%s, description=%s, tech_stack=%s WHERE id=%s",
        (data["title"], data.get("description"), data.get("tech_stack"), project_id)
    )
    conn.commit()
    updated = cursor.rowcount
    cursor.close()
    conn.close()
    if not updated:
        return jsonify({"error": "Not found"}), 404
    return jsonify({"message": "Project updated"})

# DELETE — remove a project
@app.route("/projects/<int:project_id>", methods=["DELETE"])
def delete_project(project_id):
    conn = get_connection()
    if not conn:
        return jsonify({"error": "DB connection failed"}), 500
    cursor = conn.cursor()
    cursor.execute("DELETE FROM projects WHERE id = %s", (project_id,))
    conn.commit()
    deleted = cursor.rowcount
    cursor.close()
    conn.close()
    if not deleted:
        return jsonify({"error": "Not found"}), 404
    return jsonify({"message": "Project deleted"})

# CREATE — register a new user
@app.route("/register", methods=["POST"])
def register():
    data = request.get_json()
    username = data["username"]
    password_hash = generate_password_hash(data["password"])

    conn = get_connection()
    if not conn:
        return jsonify({"error": "DB connection failed"}), 500
    cursor = conn.cursor()
    try:
        cursor.execute(
            "INSERT INTO users (username, password_hash) VALUES (%s, %s)",
            (username, password_hash)
        )
        conn.commit()
    except Exception:
        return jsonify({"error": "Username already exists"}), 400
    finally:
        cursor.close()
        conn.close()

    return jsonify({"message": "User registered successfully"}), 201

if __name__ == "__main__":
    app.run(debug=True)
    
