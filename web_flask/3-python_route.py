#!/usr/bin/python3
"""
a script that starts a Flask web application:
    - web application must be listening on 0.0.0.0, port 5000
    - Routes:
        * '/'
        * '/hbnb'
        * /c/<text>
        * /python/(<text>)
"""

from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_hbnb():
    """ returns 'hellow HBNB!' when GET root route """
    return 'Hello HBNB!'


@app.route('/hbnb')
def hbnb():
    """ returns 'HBNB' when GET /hbnb """
    return 'HBNB'


@app.route('/c/<text>')
def C_is_fun(text):
    """ returns 'C + text' what ever text
    passed when calling the route /c/<text>"""
    return 'C %s' % text.replace('_', ' ')

@app.route('/python/')
@app.route('/python/<text>')
def python_is_cool(text='is cool'):
    """ 
    display “Python ”, followed by the value of the text variable
    """
    return 'Python %s' % text.replace('_', ' ')


if __name__ == '__main__':
    app.url_map.strict_slashes = False
    app.run(host='0.0.0.0', port=5000)
