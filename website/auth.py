from flask import Blueprint

auth = Blueprint('auth', __name__)

# Logout logic
@auth.route('/logout')
def logout():
    pass

# Signin logic
@auth.route('/signin')
def signin():
    pass

# Signup logic
@auth.route('/signup')
def signup():
    pass