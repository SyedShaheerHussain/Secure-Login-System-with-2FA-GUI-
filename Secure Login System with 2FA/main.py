import customtkinter as ctk
from database.db import initialize_database
from gui.register_screen import RegisterScreen
from gui.login_screen import LoginScreen
from gui.otp_screen import OTPScreen

ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("dark-blue")

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("500x600")
        self.title("SecureLoginPro")
        self.current_frame = None
        initialize_database()  # Create tables
        self.show_login()

    def clear_frame(self):
        if self.current_frame:
            self.current_frame.destroy()

    def show_login(self):
        self.clear_frame()
        self.current_frame = LoginScreen(self, switch_to_register=self.show_register, switch_to_otp=self.show_otp)

    def show_register(self):
        self.clear_frame()
        self.current_frame = RegisterScreen(self, switch_to_login=self.show_login)

    def show_otp(self, user_id):
        self.clear_frame()
        self.current_frame = OTPScreen(self, user_id=user_id, switch_to_dashboard=self.show_dashboard)

    def show_dashboard(self, user_id):
        self.clear_frame()
        ctk.CTkLabel(self, text=f"Welcome User {user_id}", font=("Roboto", 24)).pack(pady=50)

if __name__ == "__main__":
    app = App()
    app.mainloop()
