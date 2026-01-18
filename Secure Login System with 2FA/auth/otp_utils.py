import pyotp, qrcode, io, base64, time
from database.db import execute_query, fetch_query
from config import OTP_EXPIRY

def generate_2fa_secret():
    return pyotp.random_base32()

def generate_qr_code(username, secret):
    totp_uri = pyotp.TOTP(secret).provisioning_uri(name=username, issuer_name="SecureLoginPro")
    qr = qrcode.QRCode(box_size=10, border=2)
    qr.add_data(totp_uri)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    buf = io.BytesIO()
    img.save(buf, format='PNG')
    return base64.b64encode(buf.getvalue()).decode('utf-8')

def verify_otp(secret, otp):
    totp = pyotp.TOTP(secret)
    return totp.verify(otp)

def create_otp_session(user_id, otp):
    expiry = int(time.time()) + OTP_EXPIRY
    execute_query("INSERT INTO otp_sessions(user_id, otp, expiry) VALUES(?,?,?)", (user_id, otp, expiry))

def validate_otp_session(user_id, otp):
    rows = fetch_query("SELECT id, expiry, used FROM otp_sessions WHERE user_id=? AND otp=?", (user_id, otp))
    if not rows: return False
    session_id, expiry, used = rows[0]
    if used or expiry < int(time.time()): return False
    execute_query("UPDATE otp_sessions SET used=1 WHERE id=?", (session_id,))
    return True
