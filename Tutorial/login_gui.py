import tkinter as tk
from tkinter import messagebox

VALID_USERNAME = "admin"
VALID_PASSWORD = "1234"

root = tk.Tk()
root.title("Login")
root.geometry("340x240")
root.resizable(False, False)
root.configure(bg="#1e1e2e")

tk.Label(root, text="Login", font=("Helvetica", 16, "bold"),
         fg="#cdd6f4", bg="#1e1e2e").pack(pady=15)

tk.Label(root, text="Username:", font=("Helvetica", 11),
         fg="#a6adc8", bg="#1e1e2e").pack()
username_entry = tk.Entry(root, font=("Helvetica", 12), width=22,
                          bg="#313244", fg="#cdd6f4", insertbackground="#cdd6f4",
                          relief=tk.FLAT)
username_entry.pack(pady=4)

tk.Label(root, text="Password:", font=("Helvetica", 11),
         fg="#a6adc8", bg="#1e1e2e").pack()
password_entry = tk.Entry(root, font=("Helvetica", 12), width=22, show="*",
                          bg="#313244", fg="#cdd6f4", insertbackground="#cdd6f4",
                          relief=tk.FLAT)
password_entry.pack(pady=4)

def login():
    username = username_entry.get().strip()
    password = password_entry.get().strip()

    if not username or not password:
        messagebox.showwarning("Empty Fields", "Username and Password cannot be empty.")
        return

    if username == VALID_USERNAME and password == VALID_PASSWORD:
        messagebox.showinfo("Success", "Login Successful!")
    else:
        messagebox.showerror("Failed", "Invalid username or password.")

tk.Button(root, text="Login", command=login,
          bg="#a6e3a1", fg="#1e1e2e", font=("Helvetica", 11, "bold"),
          relief=tk.FLAT, cursor="hand2", width=18).pack(pady=14)

root.mainloop()
