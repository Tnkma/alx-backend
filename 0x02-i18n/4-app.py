#!/usr/bin/env python3
"""Flask app that renders an index page"""
from flask import Flask, render_template, request, session
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
    return render_template('4-index.html')


# @babel.localeselector
def get_locale() -> str:
    """gets the best matching language for the user

    Returns:
        str: the best matching language for the user
        We can say 'locale = request.args.get('locale')' to get the locale
        but its also good i learned to use lambda function to get the locale
    # queries = request.query_string.decode('utf-8').split('&')
    # query_table = dict(map(
        # lambda x: (x if '=' in x else '{}='.format(x)).split('='),
        # queries,
    # ))
    # if 'locale' in query_table:
        # if query_table['locale'] in app.config["LANGUAGES"]:
            # return query_table['locale']
    """
    locale = request.args.get('locale')
    if locale in app.config['LANGUAGES']:
        session[locale] = locale
        return locale
    if 'locale' in session:
        return session['locale']
    return request.accept_Languages.best_match(app.config['LANGUAGES'])


babel.init_app(app, get_locale)


if __name__ == "__main__":
    app.run(debug=True)
