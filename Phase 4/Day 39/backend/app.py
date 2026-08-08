from flask import Flask, jsonify
from db import get_connection

app = Flask(__name__)
app.secret_key = "change-this-to-a-real-secret-key"

@app.route("/")
def home():
    return jsonify({"status": "EduTrack API is running"})

# TODO: /login, /logout, /profile (Day 38 pattern, extended with role field)
# TODO: admin_required decorator (extends login_required with a role check)
# TODO: /admin/students CRUD routes
# TODO: /admin/students/<id>/predict — loads model.pkl, runs prediction, saves dropout_risk
# TODO: /student/dashboard — returns the session's linked student record only

if __name__ == "__main__":
    app.run(debug=True)
