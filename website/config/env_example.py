from egauge import webapi

from utils import errhandler, message, syshandler

# Application Settings
FLASK_ENV=''
SECRET_KEY=''

# Egauge Settings
BASE_URI='https://DEV.egaug.es/' #Replace DEV with eGauge meter
EGAUGE_USER=''
EGAUGE_PASS=''

# Parser
dev = webapi.device.Device(BASE_URI, webapi.JWTAuth(EGAUGE_USER, EGAUGE_PASS))

# Testing API Connection
try:
    METER = dev.get('/config/net/hostname')

    # Validating API Connection
    if METER != (None or ""):
        syshandler(f"API connection {METER} established", "api")
        message("[API]... Success")
    else:
        raise ValueError("Invalid response")

except Exception as e:
    errhandler(e, "api")
    syshandler("API connection failed", "api")
    message("[API]... Fail")

