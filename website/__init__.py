# Modules
from flask import Flask

def create_app():

    # Initializing application
    app = Flask(__name__)

    # Configuring secret key
    app.config['SECRET_KEY'] = 'testapp'

    # Importing blueprints
    from .auth import auth
    from .processes import processes
    from .views import views
    # from .dashboard import dashboard

    # Registering blueprints
    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')
    app.register_blueprint(processes, url_prefix='/')

    return app