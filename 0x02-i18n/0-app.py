from flask import Flask, render_template

# Flask app initialization
app = Flask(__name__)


@app.route('/')
def index():
    """render the index page
    """
    return render_template('index.html')