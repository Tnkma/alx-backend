#!/usr/bin/env python3
"""Flask app that renders an index page"""
from flask import Flask, render_template


# Flask app initialization
app = Flask(__name__)


@app.route('/')
def index() -> str:
    """render the index page
    """
    return render_template('0-index.html')


if __name__ == "__main__":
    app.run(debug=True)
