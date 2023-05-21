#!usr/bin/python3

from flask import Flask, render_template
from models import storage
from models.state import State
from models.city import City

app = Flask(__name__)


@app.route('/states', strict_slashes=False)
def list_states():
    states = storage.all(State).values()
    return render_template('9-states.html', states=sorted_states)


@app.route('/states/<id>', strict_slashes=False)
def states_id(id):
    for state in storage.all('State').values(): 
        if state.id == id:
            return render_template('9-states.html', state=state)


@app.teardown_appcontext
def teardown_session(exception=None):
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
