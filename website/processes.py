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

# Extracting Registers Data
@processes.route('/registers')
def registers():

    try:
        # Modules
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

        # Initial Rates Dictionary
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
            'report/report.html',
            init_time = init_time_str,
            delta_time = delta_time_str,
            initials = initial_rates,
            deltas = delta_rates
            )

    except Exception as e:
        errhandler (e, "processes")
        return redirect(url_for('views.homepage'))

    return render_template('report/report.html')