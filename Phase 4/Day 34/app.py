import logging

from flask import Flask, render_template, request, jsonify

from data import projects, get_next_id

app = Flask(__name__)


# ============================================================
# LOGGING SETUP
# ============================================================
# basicConfig configures Python's built-in logging module once,
# for the whole app: every log message will include a timestamp.
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(message)s"
)
logger = logging.getLogger("day34-api")


# ============================================================
# LOGGING MIDDLEWARE
# ============================================================
# Flask lets you "hook into" every request using before_request
# and after_request decorators — this runs your function on EVERY
# incoming request/outgoing response, automatically, without you
# adding logging code inside each individual route. This is the
# beginner-friendly way to build middleware-like behavior in Flask
# (real WSGI middleware classes exist too, but these hooks are the
# standard, recommended approach for most Flask apps).

@app.before_request
def log_request_info():
    # Runs BEFORE every route function executes.
    # request.method = "GET"/"POST"/etc, request.path = the URL requested
    logger.info(f"Incoming request: {request.method} {request.path}")


@app.after_request
def log_response_info(response):
    # Runs AFTER every route function executes, right before the
    # response is sent. Must return the response object unchanged
    # (or modified) so Flask can actually send it to the client.
    logger.info(f"Responded: {request.method} {request.path} -> {response.status_code}")
    return response


# ============================================================
# HOME PAGE — a simple HTML docs page, NOT part of the API itself
# ============================================================
@app.route('/')
def home():
    return render_template('index.html')


# ============================================================
# HELPER FUNCTION
# ============================================================
def find_project(project_id):
    """Searches the in-memory 'projects' list for a matching id.
    Returns the project dict if found, otherwise None."""
    return next((p for p in projects if p["id"] == project_id), None)


# ============================================================
# CRUD: READ  (GET)
# ============================================================

@app.route('/projects', methods=['GET'])
def get_projects():
    # jsonify() converts a Python list/dict into a proper JSON HTTP
    # response, and sets the Content-Type header to application/json.
    return jsonify(projects), 200


@app.route('/projects/<int:project_id>', methods=['GET'])
def get_project(project_id):
    # <int:project_id> tells Flask to extract the id from the URL
    # and convert it to an integer automatically.
    project = find_project(project_id)
    if project is None:
        return jsonify({"error": "Project not found"}), 404
    return jsonify(project), 200


# ============================================================
# CRUD: CREATE  (POST)
# ============================================================

@app.route('/projects', methods=['POST'])
def create_project():
    # request.get_json() reads and parses the JSON body the client sent.
    # silent=True makes it return None instead of crashing if the body
    # is missing or isn't valid JSON.
    data = request.get_json(silent=True)

    if not data or "title" not in data or "description" not in data:
        return jsonify({"error": "title and description are required"}), 400

    new_project = {
        "id": get_next_id(),
        "title": data["title"],
        "description": data["description"],
        "tech": data.get("tech", "")   # optional field, defaults to ""
    }
    projects.append(new_project)
    return jsonify(new_project), 201   # 201 = Created


# ============================================================
# CRUD: UPDATE  (PUT)
# ============================================================

@app.route('/projects/<int:project_id>', methods=['PUT'])
def update_project(project_id):
    project = find_project(project_id)
    if project is None:
        return jsonify({"error": "Project not found"}), 404

    data = request.get_json(silent=True)
    if not data:
        return jsonify({"error": "Request body must be JSON"}), 400

    # .get(key, project[key]) means: use the new value if the client
    # sent one, otherwise keep the existing value unchanged.
    project["title"] = data.get("title", project["title"])
    project["description"] = data.get("description", project["description"])
    project["tech"] = data.get("tech", project["tech"])

    return jsonify(project), 200


# ============================================================
# CRUD: DELETE  (DELETE)
# ============================================================

@app.route('/projects/<int:project_id>', methods=['DELETE'])
def delete_project(project_id):
    project = find_project(project_id)
    if project is None:
        return jsonify({"error": "Project not found"}), 404

    projects.remove(project)
    return jsonify({"message": f"Project {project_id} deleted"}), 200


if __name__ == '__main__':
    app.run(debug=True)
