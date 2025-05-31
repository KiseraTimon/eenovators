from flask import Blueprint, render_template, session, redirect, url_for, flash
from .database.connector import dbconnector
from utils import errhandler
from werkzeug.security import generate_password_hash, check_password_hash
import random
import time

dashboard = Blueprint('dashboard', __name__)

# Database Connection
conn = dbconnector()

# Staff dashboard route
@dashboard.route('/staff')
def staff():
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