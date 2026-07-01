import math
import tkinter as tk

def calculate_area(radius):
 area = math.pi * radius * radius
 return area

root = tk.Tk()

canvas1 = tk.Canvas(root, width=300, height=300)
canvas1.pack()
 
entry1 = tk.Entry (root) 
canvas1.create_window(150, 140, window=entry1)

def getSquareRoot ():  
 root = entry1.get()
 
 label1 = tk.Label(root, text= calculate_area(int(root)))
 canvas1.create_window(150, 230, window=label1)

button1 = tk.Button(text='Calculate Area', command=getSquareRoot)
canvas1.create_window(150, 180, window=button1)
 
root.mainloop()