import tkinter as tk
from tkinter import filedialog, Text, Menu

# root window configuration
root = tk.Tk()
root.title("Code Editor")

# text area where code is written
textArea = Text(root, relief="sunken")
textArea.grid(row=0, column = 0, columnspan=3, padx = 5, pady = 5, sticky = "nsew")

# sets the scrollbar x y
scrollbar = tk.Scrollbar(textArea)
textArea.configure(xscrollcommand=scrollbar.set)
scrollbar.config(command=textArea.yview)
scrollbar.grid(row=0, column=3, sticky='nsew')

# open file
def open_file():
    global filename
    filename = filedialog.askopenfilename(defaultextension=".txt", filetypes=[("All Files", "*.*"), ("Text Files", "*.txt")])
    if filename == "":
        filename = None
    else:
        root.title(f"Code Editor - {filename}")
        textArea.delete(1.0, tk.END)
        f = open(filename, "r")
        textArea.insert(1.0, f.read())
        f.close()

# save file
def save_file():
    if filename == None:
        save_as()
    else:
        f = open(filename, "w")
        f.write(textArea.get(1.0, tk.END))
        f.close()

# save as file
def save_as():
    global filename
    filename = filedialog.asksaveasfilename(initialfile="Untitled.txt", defaultextension=".txt", filetypes=[("All Files", "*.*"), ("Text Files", "*.txt")])
    f = open(filename, "w")
    f.write(textArea.get(1.0, tk.END))
    f.close()

# creating the statusbar
statusBar = tk.Label(root, text="Status Bar")
statusBar.grid(row=1, column=0, columnspan=3, sticky="ew")

# creating the menubar
menubar = Menu(root)
root.config(menu=menubar)

# creating the options for the file menu
fileMenu = Menu(menubar)
menubar.add_cascade(label="File", menu=fileMenu)
fileMenu.add_command(label="Open", command=open_file)
fileMenu.add_command(label="Save", command=save_file)
fileMenu.add_command(label="Save As", command=save_as)

# coding syntax highlighting
textArea.configure(bg="grey", fg="white")

# loop to run application
root.mainloop()