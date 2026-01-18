import os

# Database path
DB_PATH = os.path.join(os.path.dirname(__file__), "secure_app.db")

# App settings
APP_NAME = "SecureLoginPro"

# OTP settings
OTP_EXPIRY = 30           # seconds
MAX_LOGIN_ATTEMPTS = 5
LOCKOUT_TIME = 300        # seconds
