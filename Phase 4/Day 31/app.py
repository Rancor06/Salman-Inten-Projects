from flask import Flask, render_template

# Create the Flask application object.
# __name__ tells Flask where this file lives, so it can find
# the 'templates' and 'static' folders correctly.
app = Flask(__name__)


# The @app.route() decorator connects a URL path to a Python function.
# When someone visits "/", Flask will run the home() function below.
@app.route('/')
def home():
    return render_template('index.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/contact')
def contact():
    return render_template('contact.html')


# This block only runs if you execute "python app.py" directly
# (not if this file is imported elsewhere).
if __name__ == '__main__':
    app.run(debug=True)
