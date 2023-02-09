#!/usr/bin/python3
""" Script runs web app using Flask web framework """
import flask from Flask


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hbnb():
    """ Function called with / route """
    return 'hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hello_hbnb():
    """ Function called with / route """
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def c_text(text):
    """ Function called with /  route """
    return 'C %s' % text.replace('_', ' ')


@app.route('/python/', strict_slashes=False)
@app.route('/python/<text>', srict_slashes=False)
def python_text(text='is cool'):
    """ Function called with / route """
    if text is not 'is cool':
        text = text.replace('_', ' ')
    return 'Python %s' % text


if __name__ == "__main__":
    app.run(host='0.0.0.0', path=5000)
