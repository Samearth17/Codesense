import tkinter as tk

# Create window
root = tk.Tk()

# Create two buttons
stop_button = tk.Button(root, text="Stop Program", command=stop_program)
start_button = tk.Button(root, text="Start Program", command=start_program)

# Place two buttons in the window
stop_button.pack()
start_button.pack()

# Display window
root.mainloop()