import tkinter as tk

root = tk.Tk()
frame = tk.Frame(root)
frame.pack()

button = tk.Button(frame, 
                   text="Click Me!", 
                   fg="blue",
                   command=lambda: print("Hello World!"))
button.pack(side=tk.LEFT)

close = tk.Button(frame, 
                  text="Exit", 
                  fg="red",
                  command=quit)
close.pack(side=tk.LEFT)

root.mainloop()