# Modules
from flask import Flask

def create_app():

    # Initializing application
    app = Flask(__name__)

    # Configuring secret key
    app.config['SECRET_KEY'] = 'testapp'

    return app