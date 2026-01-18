import customtkinter as ctk
from gui.utils_gui import show_error, show_info
from auth.otp_utils import verify_otp
from database.db import fetch_query

class OTPScreen(ctk.CTkFrame):
    def __init__(self, master, user_id, switch_to_dashboard):
        super().__init__(master)
        self.master = master
        self.user_id = user_id
        self.switch_to_dashboard = switch_to_dashboard
        self.pack(fill="both", expand=True)
        self.create_widgets()

    def create_widgets(self):
        ctk.CTkLabel(self, text="Enter OTP", font=("Roboto", 24)).pack(pady=20)
        self.otp_entry = ctk.CTkEntry(self, placeholder_text="6-digit OTP")
        self.otp_entry.pack(pady=5)
        ctk.CTkButton(self, text="Verify OTP", command=self.verify_otp_code).pack(pady=20)

    def verify_otp_code(self):
        otp = self.otp_entry.get().strip()
        secret = fetch_query("SELECT twofa_secret FROM users WHERE id=?", (self.user_id,))
        secret = secret[0][0] if secret else None
        if not secret or not otp:
            show_error("Error", "Invalid OTP or 2FA not setup")
            return
        if verify_otp(secret, otp):
            show_info("Success", "OTP Verified! Logging in...")
            self.switch_to_dashboard(self.user_id)
        else:
            show_error("Error", "Incorrect OTP")
