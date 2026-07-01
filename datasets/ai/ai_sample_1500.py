import tkinter as tk

# create the main GUI window
window = tk.Tk()
window.title("Python Graphing Program")
window.geometry("500x500")

# create a Canvas object
c = tk.Canvas(window, width=480, height=480)
c.pack()

# create the X and Y axes
c.create_line(10, 240, 470, 240)
c.create_line(240, 10, 240, 470)

# create the graph
...