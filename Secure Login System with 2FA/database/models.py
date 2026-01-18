from db import execute_query

# Users table
execute_query("""
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT UNIQUE NOT NULL,
    email TEXT UNIQUE NOT NULL,
    password_hash TEXT NOT NULL,
    twofa_secret TEXT,
    failed_attempts INTEGER DEFAULT 0,
    locked_until INTEGER DEFAULT 0,
    last_login TIMESTAMP
)
""")

# Security logs
execute_query("""
CREATE TABLE IF NOT EXISTS security_logs (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER,
    action TEXT,
    status TEXT,
    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
    ip_address TEXT,
    FOREIGN KEY(user_id) REFERENCES users(id)
)
""")

# OTP sessions
execute_query("""
CREATE TABLE IF NOT EXISTS otp_sessions (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER,
    otp TEXT,
    expiry INTEGER,
    used INTEGER DEFAULT 0,
    FOREIGN KEY(user_id) REFERENCES users(id)
)
""")
