#!/usr/bin/env python3
"""Flask app that renders an index page"""
from flask import Flask, render_template, request, session, g
from flask_babel import Babel
from typing import Union, Dict


class Config:
    """Config class for our application
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


# Flask app initialization
app = Flask(__name__)
app.config.from_object(Config)
app.secret_key = 'your_secret_key_here'
app.config['BABEL_DEFAULT_LOCALE'] = 'en'
app.config['BABEL_DEFAULT_TIMEZONE'] = 'UTC'
app.config['BABEL_TRANSLATION_DIRECTORIES'] = 'translations'
babel = Babel(app)


users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
    5: {"name": "Godswill", "locale": "fr", "timezone": "Africa/Lagos"}
}


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
   # Check if 'locale' is in the query parameters and if it is a valid language
    locale = request.args.get('locale')
    if locale in app.config['LANGUAGES']:
        return locale

    # Check if a user is logged in and if they have a preferred locale set
    user = getattr(g, 'user', None)
    if user and user.get('locale') in app.config['LANGUAGES']:
        return user['locale']

    # Check the 'locale' in the request headers if it is a valid language
    header = request.headers.get('locale')
    if header in app.config['LANGUAGES']:
        return header

    # Fall back to the best match from the request's Accept-Language header
    return request.accept_languages.best_match(app.config['LANGUAGES'])


babel.init_app(app, locale_selector=get_locale)


def get_user() -> Union[Dict, None]:
    """get the user from the session for login
    """
    # we get the user_id from the query string
    user_id = request.args.get('login_as')
    # if user exist, then
    if user_id:
        # use the user_id to login the user
        returned_user_id = users.get(int(user_id))
        # print(returned_user_id)
        return returned_user_id
    return None


@app.before_request
def before_request():
    user = get_user()
    if user:
        g.user = user


@app.route('/')
def index() -> str:
    """render the index page
    """
    return render_template('6-index.html')


if __name__ == "__main__":
    app.run(debug=True)
