import requests
from flask import Blueprint, render_template, redirect, url_for, request, session, flash
from .database.connector import dbconnector

from utils import errhandler, message

processes = Blueprint('processes', __name__)

conn = dbconnector()

@processes.route('/newsletter', methods=['POST'])
def newsletter():
    if request.method == 'POST':
        email = request.form.get('email')

        # Validating Email
        if not email or ('@' not in email) or ('.' not in email.split('@')[-1]):
            # Error Message
            message('Invalid email address provided', category='error')

            # Redirecting to Homepage
            return redirect(request.url)

        try:
            # Query Cursor
            cursor = conn.cursor()

            # Checking If The Email Already Exists
            cursor.execute("SELECT email FROM newsletters WHERE email = %s", (email,))
            accounts = cursor.fetchone()

            # Checking if Email is Associated With an Active Account
            cursor.execute("SELECT email FROM users WHERE email = %s", (email,))
            profile = cursor.fetchone()

            if accounts and accounts != None:
                # Error Message
                flash("An active similar email is already registered for the newsletters", category='error')

                # Redirecting
                return redirect(url_for(request.url))

            if profile and profile != None:
                user = True
            else:
                user = False

            # Inserting Email Into Database
            cursor.execute("INSERT INTO newsletters (email, user) VALUES (%s, %s)", (email, user))
            conn.commit()

            #Success Message
            flash("Thank you for signing up for our mail. Check your emails for notifications", category='success')

            return redirect(url_for('views.homepage'))
        except Exception as e:
            flash("An unexpected error occured. Please try again later", category='error')
            errhandler(e, "processes/newsletters")

    else:
        flash("Invalid access of service", category='error')

    return redirect(url_for('views.homepage'))
