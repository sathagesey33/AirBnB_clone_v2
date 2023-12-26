#!/usr/bin/python3
"""
A Flask application that displays different messages based on routes.
"""

from flask import Flask
from werkzeug.utils import escape

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """
    Route that returns 'Hello HBNB!'.
    """
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def display_hbnb():
    """
    Route that returns 'HBNB'.
    """
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def display_c(text):
    """
    Route that returns 'C ' followed by the value of the text variable.
    Underscores in the text are replaced with spaces.
    """
    return 'C {}'.format(escape(text).replace('_', ' '))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
