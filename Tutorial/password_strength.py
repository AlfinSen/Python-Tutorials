import tkinter as tk
import string

root = tk.Tk()
root.title("Password Strength Checker")
root.geometry("360x220")
root.resizable(False, False)
root.configure(bg="#1e1e2e")

tk.Label(root, text="Password Strength Checker", font=("Helvetica", 14, "bold"),
         fg="#cdd6f4", bg="#1e1e2e").pack(pady=15)

tk.Label(root, text="Enter Password:", font=("Helvetica", 11),
         fg="#a6adc8", bg="#1e1e2e").pack()
password_entry = tk.Entry(root, font=("Helvetica", 12), width=24, show="*",
                          bg="#313244", fg="#cdd6f4", insertbackground="#cdd6f4",
                          relief=tk.FLAT)
password_entry.pack(pady=6)

result_var = tk.StringVar()
result_label = tk.Label(root, textvariable=result_var, font=("Helvetica", 13, "bold"),
                        bg="#1e1e2e")
result_label.pack(pady=6)

def check_strength():
    pwd = password_entry.get()
    has_digit = any(c.isdigit() for c in pwd)
    has_special = any(c in string.punctuation for c in pwd)
    length = len(pwd)

    if length >= 8 and has_digit and has_special:
        result_var.set("Strong 💪")
        result_label.config(fg="#a6e3a1")
    elif length >= 6 and (has_digit or has_special):
        result_var.set("Moderate ⚠️")
        result_label.config(fg="#f9e2af")
    else:
        result_var.set("Weak ❌")
        result_label.config(fg="#f38ba8")

tk.Button(root, text="Check Strength", command=check_strength,
          bg="#89b4fa", fg="#1e1e2e", font=("Helvetica", 11, "bold"),
          relief=tk.FLAT, cursor="hand2", width=18).pack(pady=6)

root.mainloop()
