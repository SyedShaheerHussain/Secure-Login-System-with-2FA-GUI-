# 🔐 Secure Login System with Two-Factor Authentication (2FA)

A secure authentication system that protects user accounts using password-based login combined with two-factor authentication. It enhances security by verifying user identity through an additional one-time code, reducing unauthorized access and improving data protection.
A **Python-based Desktop Secure Authentication System** implementing real-world security practices such as **bcrypt password hashing**, **email-based OTP verification**, and **Two-Factor Authentication (2FA)** with a modern GUI.

This project is suitable for:
- Final Year Project (FYP)
- Cyber Security / Python Portfolio
- Secure Desktop Application Demonstration
- Authentication System Learning

---

## 🚀 Project Overview

This application provides a **secure login and registration system** with:
- Modern desktop GUI (Dark / Light Mode)
- Encrypted password storage
- OTP-based login verification
- Database-backed authentication
- Real-world security workflow

The system ensures that **even if a password is compromised, login is impossible without OTP verification**.

---

## ✨ Key Features

### 🔑 Authentication
- Secure **user registration & login**
- **bcrypt password hashing** (no plain-text passwords)
- Password strength indicator with color-based feedback
- Input validation with user-friendly messages

### 🔐 Two-Factor Authentication (2FA)
- Email-based **One-Time Password (OTP)**
- OTP validity with expiration
- OTP verification screen before dashboard access
- Secure OTP storage and verification logic

### 🖥️ User Interface
- Desktop application (Python)
- Modern GUI using **CustomTkinter**
- Dark & Light mode support
- Smooth screen transitions
- Splash screen (optional)

### 🗄️ Database
- SQLite database
- Structured tables:
  - `users`
  - `otp_sessions`
  - `security_logs`
- Unique email constraint
- Secure database handling

### 📊 Dashboard
- User profile display
- Last login time
- Security status
- Logout functionality

---

## 🛠️ Technologies Used

| Category | Technology |
|--------|------------|
| Language | Python 3.10+ |
| GUI | CustomTkinter |
| Database | SQLite |
| Security | bcrypt |
| OTP | pyotp |
| Email | smtplib (SMTP) |
| Architecture | Modular (MVC-style) |

---



## ⚙️ Installation Guide

### 1️⃣ Clone Repository
```
git clone https://github.com/yourusername/SecureLoginSystem.git
cd SecureLoginSystem
```

## 2️⃣ Create Virtual Environment (Recommended)

```
python -m venv venv
source venv/bin/activate   # Linux / Mac
venv\Scripts\activate      # Windows
```
▶️ How to Run the Application

```
python main.py
```
The application will:

Initialize database tables automatically

Open the Login screen

Allow new user registration

🔄 Application Flow (Start to End)
📝 Registration

User opens Sign Up

Enters:

Username

Email

Strong Password

Password is hashed using bcrypt

User is saved in the database

User proceeds to login

🔐 Login + OTP Verification

User enters email + password

Password is verified

OTP is generated

OTP is sent to user's email

User enters OTP on OTP screen

OTP is verified

Dashboard opens

📧 OTP Email Configuration (Important)

⚠️ OTP will NOT work unless email settings are configured manually by the user.

Why?

For security reasons, email credentials are NOT included in the project.

✅ Steps to Enable OTP Email
Step 1: Enable 2-Step Verification (Gmail)

Google Account → Security

Enable 2-Step Verification

Step 2: Generate App Password

Google Account → Security → App Passwords

App: Mail

Device: Windows

Generate password

Step 3: Configure config.py
```
EMAIL_ADDRESS = "your_email@gmail.com"
EMAIL_PASSWORD = "your_app_password_here"
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 465
```
⚠️ Never use your real Gmail password
⚠️ Always use App Password

🔒 Security Notes

Passwords are never stored in plain text

OTP expires after limited time

Email credentials are excluded from repository

User email is unique (prevents duplicate accounts)

Modular codebase for easy extension

🚧 Future Improvements (Optional)

Google Authenticator (TOTP) support

OTP resend timer

Account lockout after failed attempts

Login history & device info

Password reset via email

Admin panel

📌 Disclaimer

This project is created for educational and portfolio purposes.
Before using in production:

Use environment variables

Use encrypted database

Implement HTTPS for network-based versions

👨‍💻 Author

Syed Shaheer Hussain
Python | Cyber Security | Secure Systems

⭐ Support

If you like this project:

Star ⭐ the repository

Fork 🍴 it

Share with others
