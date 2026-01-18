import customtkinter as ctk
from gui.utils_gui import show_error
from auth.auth_utils import verify_password, is_account_locked, record_failed_login
from database.db import fetch_query

class LoginScreen(ctk.CTkFrame):
    def __init__(self, master, switch_to_register, switch_to_otp):
        super().__init__(master)
        self.master = master
        self.switch_to_register = switch_to_register
        self.switch_to_otp = switch_to_otp
        self.pack(fill="both", expand=True)
        self.create_widgets()

    def create_widgets(self):
        ctk.CTkLabel(self, text="Login", font=("Roboto", 24)).pack(pady=20)
        self.email = ctk.CTkEntry(self, placeholder_text="Email")
        self.email.pack(pady=5)
        self.password = ctk.CTkEntry(self, placeholder_text="Password", show="*")
        self.password.pack(pady=5)
        ctk.CTkButton(self, text="Login", command=self.login_user).pack(pady=20)
        ctk.CTkButton(self, text="Register", command=self.switch_to_register).pack(pady=5)

    def login_user(self):
        email = self.email.get().strip()
        pwd = self.password.get()
        user = fetch_query("SELECT id, password_hash FROM users WHERE email=?", (email,))
        if not user:
            show_error("Error", "User not found")
            return
        user_id, hashed = user[0]
        if is_account_locked(user_id):
            show_error("Error", "Account temporarily locked. Try later.")
            return
        if not verify_password(pwd, hashed):
            record_failed_login(user_id)
            show_error("Error", "Incorrect password")
            return
        # Login correct → go to OTP
        self.switch_to_otp(user_id)
