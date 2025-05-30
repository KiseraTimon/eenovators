# Custom Error Handling Module
from utils import errhandler

try:
    # Importing App Initializer
    from website import create_app

    # Initializing Application
    app = create_app()

    # Starting Application Server
    if __name__ == '__main__':
        app.run(debug=True, port=8080)

except Exception as e:
    errhandler(e, 'main/main')