#!/usr/bin/env python3

""" Internalization """

from flask import Flask, render_template, request
from flask_babel import Babel


class Config:
    """Configures the babel extension"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app = Flask(__name__)
app.config.from_object(Config)

babel = Babel(app)


@app.localeselector
def get_locale():
    """ Configures language translation to get best match  """
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def index():
    """Landing page"""
    return render_template('1-index.html')


if __name__ == '__main__':
    app.run()
