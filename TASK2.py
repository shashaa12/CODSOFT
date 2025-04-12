import tkinter as tk
from tkinter import messagebox

def add():
    try:
        x, y = float(entry1.get()), float(entry2.get())
        result_label.config(text=f"Result: {x + y}")
    except ValueError:
        messagebox.showerror("Invalid input", "Please enter valid numbers.")

def subtract():
    try:
        x, y = float(entry1.get()), float(entry2.get())
        result_label.config(text=f"Result: {x - y}")
    except ValueError:
        messagebox.showerror("Invalid input", "Please enter valid numbers.")

def multiply():
    try:
        x, y = float(entry1.get()), float(entry2.get())
        result_label.config(text=f"Result: {x * y}")
    except ValueError:
        messagebox.showerror("Invalid input", "Please enter valid numbers.")

def divide():
    try:
        x, y = float(entry1.get()), float(entry2.get())
        if y == 0:
            result_label.config(text="Cannot divide by zero!")
        else:
            result_label.config(text=f"Result: {x / y}")
    except ValueError:
        messagebox.showerror("Invalid input", "Please enter valid numbers.")

# GUI Setup
window = tk.Tk()
window.title("Python Calculator")
window.geometry("300x300")
window.resizable(False, False)

# Labels and Entries
tk.Label(window, text="Enter first number:").pack(pady=5)
entry1 = tk.Entry(window)
entry1.pack()

tk.Label(window, text="Enter second number:").pack(pady=5)
entry2 = tk.Entry(window)
entry2.pack()

# Operation Buttons
tk.Button(window, text="Add", command=add).pack(pady=5)
tk.Button(window, text="Subtract", command=subtract).pack(pady=5)
tk.Button(window, text="Multiply", command=multiply).pack(pady=5)
tk.Button(window, text="Divide", command=divide).pack(pady=5)

# Result Label
result_label = tk.Label(window, text="Result: ", font=('Arial', 12, 'bold'))
result_label.pack(pady=20)

# Run the GUI loop
window.mainloop()
