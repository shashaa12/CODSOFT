import tkinter as tk
from tkinter import messagebox

tasks = []

def update_task_list():
    task_listbox.delete(0, tk.END)
    for task in tasks:
        task_listbox.insert(tk.END, task)

def add_task():
    task = task_entry.get()
    if task.strip():
        tasks.append(task.strip())
        update_task_list()
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Empty Task", "Please enter a task before adding.")

def remove_task():
    selected = task_listbox.curselection()
    if selected:
        index = selected[0]
        tasks.pop(index)
        update_task_list()
    else:
        messagebox.showwarning("No Selection", "Please select a task to remove.")

# GUI Setup
window = tk.Tk()
window.title("To-Do List Manager")
window.geometry("350x400")
window.resizable(False, False)

# Entry and Buttons
tk.Label(window, text="Enter a task:", font=('Arial', 12)).pack(pady=10)
task_entry = tk.Entry(window, width=30, font=('Arial', 12))
task_entry.pack(pady=5)

tk.Button(window, text="Add Task", command=add_task, width=20).pack(pady=5)
tk.Button(window, text="Remove Selected Task", command=remove_task, width=20).pack(pady=5)

# Task List
tk.Label(window, text="Your Tasks:", font=('Arial', 12, 'bold')).pack(pady=10)
task_listbox = tk.Listbox(window, width=45, height=10, font=('Arial', 11))
task_listbox.pack()

# Run the GUI loop
window.mainloop()
