import tkinter as tk
from tkinter import messagebox
import re

contacts = {}

# Validate phone number (must be 10 digits)
def validate_phone(phone):
    return phone.isdigit() and len(phone) == 10

# Validate email format
def validate_email(email):
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email) is not None

# Add Contact function
def add_contact():
    name = name_entry.get()
    phone = phone_entry.get()
    email = email_entry.get()
    address = address_entry.get()

    # Validate inputs
    if not name or not phone or not email or not address:
        messagebox.showerror("Error", "All fields must be filled out!")
        return

    if not validate_phone(phone):
        messagebox.showerror("Error", "Phone number must be 10 digits!")
        return

    if not validate_email(email):
        messagebox.showerror("Error", "Invalid email address!")
        return

    contacts[name] = {"phone": phone, "email": email, "address": address}
    messagebox.showinfo("Success", "Contact saved successfully!")

# View Contacts function
def view_contacts():
    if not contacts:
        messagebox.showinfo("Info", "No contacts found!")
    else:
        contact_list = "\n".join([f"{name} - {info['phone']}" for name, info in contacts.items()])
        messagebox.showinfo("Contacts", f"Contact List:\n{contact_list}")

# Search Contact function
def search_contact():
    name = name_entry.get()
    if name in contacts:
        info = contacts[name]
        messagebox.showinfo("Contact Found", f"\nName: {name}\nPhone: {info['phone']}\nEmail: {info['email']}\nAddress: {info['address']}")
    else:
        messagebox.showerror("Error", "Contact not found!")

# Update Contact function
def update_contact():
    name = name_entry.get()
    if name in contacts:
        phone = phone_entry.get()
        email = email_entry.get()
        address = address_entry.get()

        # Validate inputs
        if not validate_phone(phone):
            messagebox.showerror("Error", "Phone number must be 10 digits!")
            return

        if not validate_email(email):
            messagebox.showerror("Error", "Invalid email address!")
            return

        contacts[name] = {"phone": phone, "email": email, "address": address}
        messagebox.showinfo("Success", "Contact updated successfully!")
    else:
        messagebox.showerror("Error", "Contact not found!")

# Delete Contact function
def delete_contact():
    name = name_entry.get()
    if name in contacts:
        del contacts[name]
        messagebox.showinfo("Success", "Contact deleted successfully!")
    else:
        messagebox.showerror("Error", "Contact not found!")

# Clear input fields function
def clear_fields():
    name_entry.delete(0, tk.END)
    phone_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)
    address_entry.delete(0, tk.END)

# GUI Setup
window = tk.Tk()
window.title("Contact Book")
window.geometry("400x400")
window.resizable(False, False)

tk.Label(window, text="Name:", font=('Arial', 12)).pack(pady=5)
name_entry = tk.Entry(window, font=('Arial', 12))
name_entry.pack(pady=5)

tk.Label(window, text="Phone (10 digits):", font=('Arial', 12)).pack(pady=5)
phone_entry = tk.Entry(window, font=('Arial', 12))
phone_entry.pack(pady=5)

tk.Label(window, text="Email:", font=('Arial', 12)).pack(pady=5)
email_entry = tk.Entry(window, font=('Arial', 12))
email_entry.pack(pady=5)

tk.Label(window, text="Address:", font=('Arial', 12)).pack(pady=5)
address_entry = tk.Entry(window, font=('Arial', 12))
address_entry.pack(pady=5)

# Button Frame
button_frame = tk.Frame(window)
button_frame.pack(pady=15)

tk.Button(button_frame, text="Add Contact", width=15, command=add_contact).grid(row=0, column=0, padx=5)
tk.Button(button_frame, text="View Contacts", width=15, command=view_contacts).grid(row=0, column=1, padx=5)
tk.Button(button_frame, text="Search Contact", width=15, command=search_contact).grid(row=1, column=0, padx=5)
tk.Button(button_frame, text="Update Contact", width=15, command=update_contact).grid(row=1, column=1, padx=5)
tk.Button(button_frame, text="Delete Contact", width=15, command=delete_contact).grid(row=2, column=0, padx=5)
tk.Button(button_frame, text="Clear Fields", width=15, command=clear_fields).grid(row=2, column=1, padx=5)

# Run the app
window.mainloop()
