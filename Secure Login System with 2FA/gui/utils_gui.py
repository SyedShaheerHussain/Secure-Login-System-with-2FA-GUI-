import customtkinter as ctk
from tkinter import messagebox

def show_info(title, msg):
    messagebox.showinfo(title, msg)

def show_error(title, msg):
    messagebox.showerror(title, msg)

def show_warning(title, msg):
    messagebox.showwarning(title, msg)

def password_strength(password: str):
    length = len(password)
    has_upper = any(c.isupper() for c in password)
    has_lower = any(c.islower() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_symbol = any(not c.isalnum() for c in password)
    score = sum([length>=8, has_upper, has_lower, has_digit, has_symbol])
    if score <=2: return "Weak", "red"
    elif score <=4: return "Medium", "orange"
    else: return "Strong", "green"
