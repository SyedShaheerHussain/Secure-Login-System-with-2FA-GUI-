# 🔐 Secure Login System with Two-Factor Authentication (2FA)

A secure authentication system that protects user accounts using password-based login combined with two-factor authentication. It enhances security by verifying user identity through an additional one-time code, reducing unauthorized access and improving data protection.
A **Python-based Desktop Secure Authentication System** implementing real-world security practices such as **bcrypt password hashing**, **email-based OTP verification**, and **Two-Factor Authentication (2FA)** with a modern GUI.

This project is suitable for:
- Final Year Project (FYP)
- Cyber Security / Python Portfolio
- Secure Desktop Application Demonstration
- Authentication System Learning

## 🚀 Project Overview

This application provides a **secure login and registration system** with:
- Modern desktop GUI (Dark / Light Mode)
- Encrypted password storage
- OTP-based login verification
- Database-backed authentication
- Real-world security workflow

The system ensures that **even if a password is compromised, login is impossible without OTP verification**.

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

## ⚙️ Installation Guide

### 1️⃣ Clone Repository
```
git clone https://github.com/SyedShaheerHussain/Secure-Login-System-with-2FA-GUI-.git

```
```
cd SecureLoginSystem

```

### 2️⃣ Create Virtual Environment (Optional)

```
python -m venv venv

```
```
source venv/bin/activate   # Linux / Mac

```
```
venv\Scripts\activate      # Windows

```
### ▶️ How to Run the Application

```
python main.py
```
*The application will:*

* Initialize database tables automatically

* Open the Login screen

* Allow new user registration

### 🔄 Application Flow (Start to End)

## 📝 Registration

1. User opens Sign Up

2. Enters:

3. Username

4. Email

5. Strong Password

6. Password is hashed using bcrypt

7. User is saved in the database

8. User proceeds to login

## 🔐 Login + OTP Verification

1. User enters email + password

2. Password is verified

3. OTP is generated

4. OTP is sent to user's email

5. User enters OTP on OTP screen

6. OTP is verified

7. Dashboard opens

**📧 OTP Email Configuration [!Important]**

*⚠️ OTP will NOT work unless email settings are configured manually by the user.*

**Why?**

*For security reasons, email credentials are NOT included in the project.*

## ✅ Steps to Enable OTP Email

### Step 1: Enable 2-Step Verification (Gmail)

1. Google Account → Security

2. Enable 2-Step Verification

### Step 2: Generate App Password

1. Google Account → Security → App Passwords

2. App: Mail

3. Device: Windows

4. Generate password

### Step 3: Configure config.py

```
EMAIL_ADDRESS = "your_email@gmail.com"
EMAIL_PASSWORD = "your_app_password_here"
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 465

```
> [!Important]
> **⚠️ Never use your real Gmail password**

> **⚠️ Always use App Password**

## 🔒 Security Notes

1. Passwords are never stored in plain text

2. OTP expires after limited time

3. Email credentials are excluded from repository

4. User email is unique (prevents duplicate accounts)

5. Modular codebase for easy extension

## 🚧 Future Improvements (Optional)

1. Google Authenticator (TOTP) support

2. OTP resend timer

3. Account lockout after failed attempts

4. Login history & device info

5. Password reset via email

6. Admin panel

## 📌 Disclaimer

> [!Note]
> This project is created for educational and portfolio purposes.
> 
> **Before using in production:**
> 
> 1. Use environment variables
> 2. Use encrypted database
> 3. Implement HTTPS for network-based versions

## 👨‍💻 Author

© Syed Shaheer Hussain
Python | Cyber Security | Secure Systems

## ⭐ Support

**If you like this project:**

**Star ⭐ the repository**

**Fork 🍴 it**

**Share with others**
