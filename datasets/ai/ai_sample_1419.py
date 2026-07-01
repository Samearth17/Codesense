import random
from tkinter import Tk, Button

window = Tk()
window.title("Tile Shuffling")

# Set size of window
window.geometry("500x500")

# Create a list of letters
letters = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')

# Create buttons
for i in range(25):
 btn = Button(window, text=letters[i], width="4", height="2")
 btn.grid(row=i//5, column=i%5)

# Function to shuffle the letters
def shuffle():
 random.shuffle(letters)
 # Update button text
 for i in range(25):
 btn = window.grid_slaves(row=i//5, column=i%5)
 btn[0].config(text=letters[i])

btn_shuffle = Button(window, text="Shuffle", command=shuffle)
btn_shuffle.grid(row=5, column=0, columnspan=5)

window.mainloop()