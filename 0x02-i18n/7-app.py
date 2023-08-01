#!/usr/bin/env python3

""" Internalization """

from flask import Flask, render_template, request, g
from flask_babel import Babel
import pytz


users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


class Config:
    """Configures the babel extension"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app = Flask(__name__)
app.config.from_object(Config)

babel = Babel(app)


@babel.localeselector
def get_locale():
    """ Configures language translation to get best match  """
    locale = request.args.get('locale')
    if locale in app.config['LANGUAGES']:
        return locale
    if g.user:
        locale = g.user.get('locale')
        if locale and locale in app.config['LANGUAGES']:
            return locale
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@babel.timezoneselector
def get_timezone():
    """Return the user timezone."""
    timezone = request.args.get('timezone')
    if timezone:
        try:
            tzone = pytz.timezone(timezone)
            return tzone.zone
        except pytz.exceptions.UnknownTimeZoneError:
            return None
    if g.user:
        timezone = g.user.get('timezone')
        try:
            tzone = pytz.timezone(timezone)
            return tzone.zone
        except pytz.exceptions.UnknownTimeZoneError:
            return None


def get_user():
    """ Gets valid user based on mock data. """
    user_id = request.args.get('login_as')
    if user_id and int(user_id) in users:
        return users.get(int(user_id))
    return None


@app.before_request
def before_request():
    """Runs this at the start of the app and logs user in."""
    user = get_user()
    g.user = user


@app.route('/')
def index():
    """Landing page"""
    return render_template('5-index.html')


if __name__ == '__main__':
    app.run()
