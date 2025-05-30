from flask import Blueprint

processes = Blueprint('processes', __name__)

@processes.route('/api')
def api():
    return '<h1>API endpoint is accessible</h1>'