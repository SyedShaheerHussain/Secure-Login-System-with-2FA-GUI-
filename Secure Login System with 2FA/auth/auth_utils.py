import bcrypt
import time
from database.db import execute_query, fetch_query
from config import MAX_LOGIN_ATTEMPTS, LOCKOUT_TIME

def hash_password(password: str) -> str:
    return bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()

def verify_password(password: str, hashed: str) -> bool:
    return bcrypt.checkpw(password.encode(), hashed.encode())

def record_failed_login(user_id: int):
    user = fetch_query("SELECT failed_attempts FROM users WHERE id=?", (user_id,))
    if not user: return
    attempts = user[0][0] + 1
    locked_until = 0
    if attempts >= MAX_LOGIN_ATTEMPTS:
        locked_until = int(time.time()) + LOCKOUT_TIME
        attempts = 0
    execute_query("UPDATE users SET failed_attempts=?, locked_until=? WHERE id=?", (attempts, locked_until, user_id))

def is_account_locked(user_id: int) -> bool:
    user = fetch_query("SELECT locked_until FROM users WHERE id=?", (user_id,))
    if not user: return False
    locked_until = user[0][0]
    return locked_until > int(time.time())
