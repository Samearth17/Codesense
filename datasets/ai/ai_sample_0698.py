import tkinter as tk
import pandas as pd
import matplotlib.pyplot as plt

# Load the data
data = {
   'x': [5,6,7,8,9,10],
   'y': [11,5,5,5,5,5]
}

df = pd.DataFrame(data)

# Create the application window
root = tk.Tk()

# Create a figure to display the data
fig = plt.Figure(figsize=(4,4), dpi=100)

ax = fig.add_subplot(111)

ax.plot(df['x'], df['y'])

canvas = FigureCanvasTkAgg(fig, master=root)
canvas.get_tk_widget().pack()

# Run the application
root.mainloop()