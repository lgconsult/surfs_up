# create a new python file and import the flask dependency
from flask import Flask

# create a new flask app instance

app = Flask(__name__)

# create flask routes

@app.route('/')

# create a function called hello_world()
def hello_world():
    return 'Hello world'

# run the following commands in terminal to run the flask app
# export FLASK_APP=app.py
# set FLASK_APP=app.py
# flask run
