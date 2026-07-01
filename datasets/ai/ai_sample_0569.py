import tkinter as tk
from tkinter import Canvas
import requests

# Window
window = tk.Tk()
window.title('Data Display')
window.geometry('800x600')

# Canvas and Frame
canvas = Canvas(window, bg='white')
canvas.pack()

# Retrieve data
response = requests.get('http://example.com/data.json')
data = response.json()

# Render data onto canvas
# ...

window.mainloop()