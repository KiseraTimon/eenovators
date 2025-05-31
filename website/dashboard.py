from flask import Blueprint, render_template, session, redirect, url_for, flash
from .database.connector import dbconnector
from utils import errhandler
from werkzeug.security import generate_password_hash, check_password_hash
import random
import time

dashboard = Blueprint('dashboard', __name__)

# Database Connection
conn = dbconnector()

# Role Access Check
@dashboard.route('/dashboard')
def role_access():
    try:
        # Check if user is logged in
        if 'userID' not in session:
            flash("You are not authorized to access this page", category="error")
            return redirect(url_for('views.homepage'))

        # Capture Role
        role = session.get('role')

        # Render appropriate dashboard based on user role
        if role == 'staff':
            return redirect(url_for('dashboard.staff'))
        elif role == 'admin':
            pass
        elif role == 'user':
            pass
        else:
            flash("You are not authorized to access this page", category="error")
            return redirect(url_for('views.homepage'))

    except Exception as e:
        flash("An error occurred while accessing your dashboard", category="error")
        errhandler(e, "processes/dashboard")
        return redirect(url_for('views.homepage'))

    return redirect(url_for('views.homepage'))

# Staff dashboard route
@dashboard.route('/staff')
def staff():
    #Access Validation
    if 'userID' not in session or session.get('role') != 'staff':
        flash("You are not authorized to access this page", category="error")
        return redirect(url_for('views.homepage'))

    # Extracting Session Data
    user = {
        'userID' : session.get('userID'),
        'fname' : session.get('fname'),
        'lname' : session.get('lname'),
        'email' : session.get('email'),
        'role' : session.get('role')
    }

    try:
        # Imports
        import argparse
        import sys
        from datetime import datetime, timezone

        from egauge.examples import test_common
        from egauge.webapi.device import PhysicalQuantity, Register, UnitSystem

        # Parsers
        parser = argparse.ArgumentParser(
            description="Demonstrate the use of class egauge.webapi.device.Register."
        )
        parser.add_argument(
            "--imperial",
            action="store_true",
            help="Output units in imperial units rather than metric units.",
        )
        args = parser.parse_args()

        # Initializing Register Value Units
        if args.imperial:
            PhysicalQuantity.set_unit_system(UnitSystem.IMPERIAL)

        # Capturing Response
        ret = Register(test_common.dev, {"rate": "", "time": "now,som"})

        ts = ret.ts()

        if ts is None:
            message("Failed to get register data.", file=sys.stderr)
            sys.exit(1)

        # Initial Data timestamp
        init_dt = datetime.fromtimestamp(round(ts), tz=timezone.utc)
        init_time_str = init_dt.strftime("%Y-%m-%d %H:%M:%S %Z")

        #Initial Rates Dictionary
        initial_rates = {}

        # Initial Register Rates
        for regname in ret.regs:
            # Instantananeous Rate
            pq = ret.pq_rate(regname)
            initial_rates[regname] = {
                "value": round(pq.value, 3),
                "unit": pq.unit
            }


        # Calculating deltas (Change in values)
        delta = ret[0] - ret[1]

        # Delta Data Timestamp
        delta_dt = datetime.fromtimestamp(round(ret[1].ts), tz=timezone.utc)
        delta_time_str = delta_dt.strftime("%Y-%m-%d %H:%M:%S %Z")

        # Delta Register Dictionary
        delta_rates = {}

        # Value changes since start of month
        for regname in delta.regs:
            # Accumulated value
            accu = delta.pq_accu(regname)
            avg = delta.pq_avg (regname)

            delta_rates[regname] = {
                "accumulated": round(accu.value, 3),
                "average": round(avg.value, 3),
                "unit": accu.unit
            }

        return render_template(
            'dashboard/staff.html',
            user = user,
            init_time = init_time_str,
            delta_time = delta_time_str,
            initials = initial_rates,
            deltas = delta_rates
            )

    except Exception as e:
        flash("An error occurred while accessing your dashboard", category="error")
        errhandler (e, "processes/staff")
        return redirect(url_for('views.homepage'))

    return render_template('dashboard/staff.html')