#!/usr/bin/python3

"""
A Flask application that displays different messages based
on routes and handles HTML templates.
"""

from flask import Flask, render_template

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
    Route that returns 'C ' followed by the
    value of the text variable.
    Underscores in the text are replaced with spaces.
    """
    return 'C {}'.format(text.replace('_', ' '))


@app.route('/python/', defaults={'text': 'is_cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def display_python(text):
    """
    Route that returns 'Python ' followed by
    the value of the text variable.
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


@app.route('/number_template/<int:n>', strict_slashes=False)
def display_number_template(n):
    """
    Route that displays an HTML page
    with "Number: n" inside the <h1> tag if n is an integer.
    """
    if isinstance(n, int):
        return render_template('number_template.html', n=n)
    else:
        return 'Not Found', 404


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def display_number_odd_or_even(n):
    """
    Route that displays an HTML page with "Number: n is even|odd"
    inside the <h1> tag if n is an integer.
    """
    if isinstance(n, int):
        odd_even = 'even' if n % 2 == 0 else 'odd'
        return render_template('number_odd_or_even.html',
                               n=n, odd_even=odd_even)
    else:
        return 'Not Found', 404


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
