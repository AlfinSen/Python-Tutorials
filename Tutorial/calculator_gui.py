import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("Integer Calculator")
root.geometry("360x280")
root.resizable(False, False)
root.configure(bg="#1e1e2e")

tk.Label(root, text="Integer Calculator", font=("Helvetica", 15, "bold"),
         fg="#cdd6f4", bg="#1e1e2e").pack(pady=12)

frame = tk.Frame(root, bg="#1e1e2e")
frame.pack()

tk.Label(frame, text="Number 1:", font=("Helvetica", 11), fg="#a6adc8", bg="#1e1e2e").grid(row=0, column=0, padx=8, pady=4, sticky="e")
num1_entry = tk.Entry(frame, font=("Helvetica", 12), width=12, bg="#313244", fg="#cdd6f4", insertbackground="#cdd6f4", relief=tk.FLAT)
num1_entry.grid(row=0, column=1, pady=4)

tk.Label(frame, text="Number 2:", font=("Helvetica", 11), fg="#a6adc8", bg="#1e1e2e").grid(row=1, column=0, padx=8, pady=4, sticky="e")
num2_entry = tk.Entry(frame, font=("Helvetica", 12), width=12, bg="#313244", fg="#cdd6f4", insertbackground="#cdd6f4", relief=tk.FLAT)
num2_entry.grid(row=1, column=1, pady=4)

tk.Label(frame, text="Result:", font=("Helvetica", 11), fg="#a6adc8", bg="#1e1e2e").grid(row=2, column=0, padx=8, pady=4, sticky="e")
result_var = tk.StringVar()
result_entry = tk.Entry(frame, textvariable=result_var, font=("Helvetica", 12), width=12,
                        bg="#313244", fg="#a6e3a1", state="readonly", relief=tk.FLAT)
result_entry.grid(row=2, column=1, pady=4)

def get_numbers():
    try:
        n1 = int(num1_entry.get())
        n2 = int(num2_entry.get())
        return n1, n2
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter valid integers.")
        return None, None

def add():
    n1, n2 = get_numbers()
    if n1 is not None:
        result_var.set(n1 + n2)

def subtract():
    n1, n2 = get_numbers()
    if n1 is not None:
        result_var.set(n1 - n2)

def multiply():
    n1, n2 = get_numbers()
    if n1 is not None:
        result_var.set(n1 * n2)

def divide():
    n1, n2 = get_numbers()
    if n1 is not None:
        try:
            result_var.set(round(n1 / n2, 4))
        except ZeroDivisionError:
            messagebox.showerror("Math Error", "Cannot divide by zero.")

btn_frame = tk.Frame(root, bg="#1e1e2e")
btn_frame.pack(pady=12)

btn_style = {"font": ("Helvetica", 11, "bold"), "relief": tk.FLAT, "cursor": "hand2", "width": 10}

tk.Button(btn_frame, text="Add", command=add, bg="#89b4fa", fg="#1e1e2e", **btn_style).grid(row=0, column=0, padx=6)
tk.Button(btn_frame, text="Subtract", command=subtract, bg="#f38ba8", fg="#1e1e2e", **btn_style).grid(row=0, column=1, padx=6)
tk.Button(btn_frame, text="Multiply", command=multiply, bg="#fab387", fg="#1e1e2e", **btn_style).grid(row=0, column=2, padx=6)
tk.Button(btn_frame, text="Divide", command=divide, bg="#a6e3a1", fg="#1e1e2e", **btn_style).grid(row=0, column=3, padx=6)

root.mainloop()
