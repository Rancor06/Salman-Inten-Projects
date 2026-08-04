from flask import Flask, render_template

# Import our project list from data.py. This keeps app.py focused on
# routing, and keeps the actual content (project info) in one clean place.
from data import projects

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/about')
def about():
    return render_template('about.html')


# This route passes 'projects' (a list of dictionaries) into the template.
# render_template() takes any keyword argument and makes it available
# inside the HTML file under that same name — so inside projects.html,
# we'll be able to write {% for project in projects %}.
@app.route('/projects')
def projects_page():
    return render_template('projects.html', projects=projects)


@app.route('/contact')
def contact():
    return render_template('contact.html')


if __name__ == '__main__':
    app.run(debug=True)
