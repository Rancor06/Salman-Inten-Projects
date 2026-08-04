# data.py
# Our "database" for this project — just a Python list of dictionaries
# living in memory. No real database is used, as required by the task.
# NOTE: this data resets every time the server restarts, since nothing
# is saved to disk.

projects = [
    {
        "id": 1,
        "title": "EduTrack",
        "description": "Student dropout risk predictor combining a trained "
                        "ML model with a full-stack web app.",
        "tech": "Python, Flask, scikit-learn, React"
    },
    {
        "id": 2,
        "title": "Academic Certificate Authenticity Validator",
        "description": "ML system that detects forged certificates using "
                        "an OCR verification pipeline.",
        "tech": "Python, OCR, Machine Learning"
    },
    {
        "id": 3,
        "title": "NeuraDocCluster AI",
        "description": "Hierarchical document organization system with "
                        "image preprocessing and masking.",
        "tech": "Python, Generative AI, Image Processing"
    },
]


def get_next_id():
    """Returns a new unique id: one higher than the current highest id.
    Used whenever a new project is created via POST."""
    if not projects:
        return 1
    return max(project["id"] for project in projects) + 1
