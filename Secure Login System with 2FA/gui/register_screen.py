import customtkinter as ctk
from gui.utils_gui import show_info, show_error, password_strength
from auth.auth_utils import hash_password
from auth.otp_utils import generate_2fa_secret, generate_qr_code
from database.db import execute_query, fetch_query
from PIL import Image
import io, base64

class RegisterScreen(ctk.CTkFrame):
    def __init__(self, master, switch_to_login):
        super().__init__(master)
        self.master = master
        self.switch_to_login = switch_to_login
        self.pack(fill="both", expand=True)
        self.create_widgets()

    def create_widgets(self):
        ctk.CTkLabel(self, text="Register", font=("Roboto", 24)).pack(pady=20)
        self.username = ctk.CTkEntry(self, placeholder_text="Username")
        self.username.pack(pady=5)
        self.email = ctk.CTkEntry(self, placeholder_text="Email")
        self.email.pack(pady=5)
        self.password = ctk.CTkEntry(self, placeholder_text="Password", show="*")
        self.password.pack(pady=5)
        self.password.bind("<KeyRelease>", self.check_password_strength)
        self.confirm_password = ctk.CTkEntry(self, placeholder_text="Confirm Password", show="*")
        self.confirm_password.pack(pady=5)
        self.strength_label = ctk.CTkLabel(self, text="")
        self.strength_label.pack(pady=2)
        ctk.CTkButton(self, text="Register", command=self.register_user).pack(pady=20)
        ctk.CTkButton(self, text="Back to Login", command=self.switch_to_login).pack(pady=5)

    def check_password_strength(self, event=None):
        pwd = self.password.get()
        strength, color = password_strength(pwd)
        self.strength_label.configure(text=f"Strength: {strength}", text_color=color)

    def register_user(self):
        username = self.username.get().strip()
        email = self.email.get().strip()
        pwd = self.password.get()
        confirm_pwd = self.confirm_password.get()

        if not username or not email or not pwd or not confirm_pwd:
            show_error("Error", "All fields are required!")
            return
        if pwd != confirm_pwd:
            show_error("Error", "Passwords do not match!")
            return

        # Check uniqueness
        existing = fetch_query("SELECT id FROM users WHERE username=? OR email=?", (username, email))
        if existing:
            show_error("Error", "Username or Email already exists!")
            return

        hashed = hash_password(pwd)
        secret = generate_2fa_secret()
        execute_query("INSERT INTO users(username,email,password_hash,twofa_secret) VALUES(?,?,?,?)",
                      (username, email, hashed, secret))

        # Show QR code
        qr_base64 = generate_qr_code(username, secret)
        qr_data = base64.b64decode(qr_base64)
        img = Image.open(io.BytesIO(qr_data))
        img.show()  # QR for Google Authenticator

        show_info("Success", "Registration successful! Scan QR for 2FA.")
        self.switch_to_login()
