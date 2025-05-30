from flask import Blueprint, render_template

auth = Blueprint('auth', __name__)

# Logout logic
@auth.route('/logout')
def logout():
    pass

# Signin logic
@auth.route('/signin')
def signin():
    return render_template('auth/signin.html')

# Signup logic
@auth.route('/signup')
def signup():
    return render_template('auth/signup.html')