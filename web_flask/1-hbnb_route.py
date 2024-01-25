#!/usr/bin/python3

"""
A Flask application that displays 'Hello HBNB!' on the root route
and 'HBNB' on the '/hbnb' route.
"""

from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """
    Route that returns 'Hello HBNB!'.
    """
    return 'Hello HBNB!'


@app.route('/airbnb-onepage/', strict_slashes=False)
def display_hbnb():
    """
    Route that returns 'HBNB'.
    """
    return 'HBNB'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
