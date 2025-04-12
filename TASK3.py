import tkinter as tk
from tkinter import messagebox
import random
import string

def generate_password():
    try:
        length = int(length_entry.get())
        if length <= 0:
            raise ValueError
        # Alphanumeric + only $@#
        characters = string.ascii_letters + string.digits + "$@#"
        password = ''.join(random.choice(characters) for _ in range(length))
        result_label.config(text=password)
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a positive integer.")

# GUI Setup
window = tk.Tk()
window.title("Password Generator")
window.geometry("350x250")
window.resizable(False, False)

tk.Label(window, text="Enter password length:", font=('Arial', 12)).pack(pady=10)
length_entry = tk.Entry(window, font=('Arial', 12))
length_entry.pack(pady=5)

tk.Button(window, text="Generate Password", command=generate_password, font=('Arial', 11)).pack(pady=10)

tk.Label(window, text="Your Secure Password:", font=('Arial', 12, 'bold')).pack(pady=10)
result_label = tk.Label(window, text="", font=('Arial', 12), wraplength=300)
result_label.pack()

# Run the GUI loop
window.mainloop()
