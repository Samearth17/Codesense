import tkinter as tk

root = tk.Tk()
root.title("GUI Application")

tk.Label(root, text="Enter your name:").grid(row=0, column=0, sticky="W")
name_entry = tk.Entry(root)
name_entry.grid(row=0, column=1)

def on_button_click():
    name = name_entry.get()
    tk.Label(root, text="Hello "+name).grid(row=1, column=1)

tk.Button(root, text="Click Me", command=on_button_click).grid(row=0, column=2)

root.mainloop()