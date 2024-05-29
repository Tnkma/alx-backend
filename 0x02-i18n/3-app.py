#!/usr/bin/env python3
"""Flask app that renders an index page"""
from flask import Flask, render_template, request
from flask_babel import Babel

class Config:
    """Config class for our application
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


# Flask app initialization
app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


@app.route('/')
def index() -> str:
    """render the index page
    """
    return render_template('3-index.html')

@babel.localeselector
def get_locale() -> str:
    """gets the best matching language for the user

    Returns:
        str: the best matching language for the user
    """
    return request.accept_Languages.best_match(app.config['LANGUAGES'])


if __name__ == "__main__":
    app.run(debug=True)
