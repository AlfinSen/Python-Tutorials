import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("Temperature Converter")
root.geometry("360x220")
root.resizable(False, False)
root.configure(bg="#1e1e2e")

tk.Label(root, text="Temperature Converter", font=("Helvetica", 15, "bold"),
         fg="#cdd6f4", bg="#1e1e2e").pack(pady=15)

tk.Label(root, text="Enter Celsius:", font=("Helvetica", 11),
         fg="#a6adc8", bg="#1e1e2e").pack()

celsius_entry = tk.Entry(root, font=("Helvetica", 12), width=20,
                         bg="#313244", fg="#cdd6f4", insertbackground="#cdd6f4",
                         relief=tk.FLAT)
celsius_entry.pack(pady=5)

result_var = tk.StringVar()
result_entry = tk.Entry(root, textvariable=result_var, font=("Helvetica", 12),
                        width=20, bg="#313244", fg="#a6e3a1",
                        state="readonly", relief=tk.FLAT)
result_entry.pack(pady=5)

def convert():
    try:
        celsius = float(celsius_entry.get())
        fahrenheit = round((celsius * 9 / 5) + 32, 2)
        result_var.set(f"{fahrenheit} °F")
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid numeric value for Celsius.")

tk.Button(root, text="Convert to Fahrenheit", command=convert,
          bg="#89b4fa", fg="#1e1e2e", font=("Helvetica", 11, "bold"),
          relief=tk.FLAT, cursor="hand2", width=22).pack(pady=12)

root.mainloop()
