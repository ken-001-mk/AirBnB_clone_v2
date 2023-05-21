#!/usr/bin/python3
"""script that starts a Flask web application"""

from flask import Flask

app = Flask(__name__)

@app.route('/', strict_slashes=False)
def hello_hbnb():
    return 'Hello HBNB!'

@app.route('/hbnb', strict_slashes=False)
def hbnb():
    return 'HBNB'

@app.route('/c/<text>', strict_slashes=False)
def c(text):
    text = text.replace('_', '')
    return 'C {}'.format(text)

@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python(text='is cool'):
    text = text.replace('_', '')
    return 'Python {}'.format(text)

@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    return '{} is a number'.format(n)

@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    return render_template('number.html', n=n)

@app.route('/number_odd_or_even/<int:n', strict_slashes=False)
def number_odd_or_even(n):
    if n % 2 == 0:
       number_type = 'even'
    else:
       number_type = 'odd'
    return render_template('number_odd_or_even.html', n=n, number_type=number_type)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
