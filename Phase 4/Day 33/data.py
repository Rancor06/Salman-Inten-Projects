# data.py
# Storing project info here means projects.html never needs to be
# edited by hand to add/remove a project — you just edit this list.
# Flask/Jinja2 will generate the HTML cards automatically.

projects = [
    {
        "title": "EduTrack",
        "description": "A student dropout risk predictor built as a capstone project, "
                        "combining a trained ML model with a full-stack web app.",
        "tech": "Python, Flask, scikit-learn, React",
        "icon": "fa-solid fa-graduation-cap",
        "link": "https://github.com/Rancor06"
    },
    {
        "title": "Academic Certificate Authenticity Validator",
        "description": "A machine learning system that detects forged or manipulated "
                        "certificates using an OCR and verification pipeline, built for "
                        "Smart India Hackathon.",
        "tech": "Python, OCR, Machine Learning",
        "icon": "fa-solid fa-file-shield",
        "link": "https://github.com/Rancor06"
    },
    {
        "title": "NeuraDocCluster AI",
        "description": "An intelligent hierarchical document organization system, with "
                        "image preprocessing and masking used to test a generative AI "
                        "virtual try-on pipeline.",
        "tech": "Python, Generative AI, Image Processing",
        "icon": "fa-solid fa-layer-group",
        "link": "https://github.com/Rancor06"
    },
    {
        "title": "Flask Portfolio Website",
        "description": "This very site — a multi-page portfolio built with Flask, "
                        "Jinja2 templates, and hand-written CSS.",
        "tech": "Flask, Jinja2, HTML, CSS",
        "icon": "fa-solid fa-globe",
        "link": "https://github.com/Rancor06"
    },
]
