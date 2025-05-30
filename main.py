# Modules
from website import create_app

# Initializing Application
app = create_app()

# Starting Application Server
if __name__ == '__main__':
    app.run(debug=True, port=9090)