import tkinter as tk

root = tk.Tk()
root.title("Python GUI Demo")
root.geometry("320x160")
root.resizable(False, False)
root.configure(bg="#1e1e2e")

label = tk.Label(
    root,
    text="Python GUI Demo",
    font=("Helvetica", 16, "bold"),
    fg="#cdd6f4",
    bg="#1e1e2e"
)
label.pack(pady=30)

btn_frame = tk.Frame(root, bg="#1e1e2e")
btn_frame.pack()

def on_clear():
    label.config(text="")
    clear_btn.config(state=tk.DISABLED)
    restore_btn.config(state=tk.NORMAL)

def on_restore():
    label.config(text="Python GUI Demo")
    restore_btn.config(state=tk.DISABLED)
    clear_btn.config(state=tk.NORMAL)

clear_btn = tk.Button(
    btn_frame, text="Clear", width=10, command=on_clear,
    bg="#f38ba8", fg="#1e1e2e", font=("Helvetica", 11, "bold"),
    relief=tk.FLAT, cursor="hand2"
)
clear_btn.grid(row=0, column=0, padx=10)

restore_btn = tk.Button(
    btn_frame, text="Restore", width=10, command=on_restore,
    bg="#a6e3a1", fg="#1e1e2e", font=("Helvetica", 11, "bold"),
    relief=tk.FLAT, cursor="hand2", state=tk.DISABLED
)
restore_btn.grid(row=0, column=1, padx=10)

root.mainloop()
