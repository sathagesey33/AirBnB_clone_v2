#!/usr/bin/python3

"""
A Flask application with various routes displaying different messages.
"""

from flask import Flask, abort

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
    return 'C {}'.format(text.replace('_', ' '))


@app.route('/python/', defaults={'text': 'is_cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def display_python(text):
    """
    Route that returns 'Python ' followed by the value of the text variable.
    Underscores in the text are replaced with spaces.
    Default value of text is 'is_cool'.
    """
    return 'Python {}'.format(text.replace('_', ' '))


@app.route('/number/<int:n>', strict_slashes=False)
def display_number(n):
    """
    Route that returns 'n is a number' only if n is an integer.
    """
    return '{} is a number'.format(n)


@app.route('/number/<n>', strict_slashes=False)
def not_an_integer(n):
    """
    Route that aborts the request if n is not an integer.
    """
    abort(404)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
