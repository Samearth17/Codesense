import tkinter as tk

# Create a window
window = tk.Tk()
window.title("Printed Text Output") 
window.geometry("500x500") 

# Label and Entry to input text
label1 = tk.Label(window, text="Input text:").place(x=50, y=50)
entry = tk.Entry(window)
entry.place(x=120, y=50)

# Print out the text
def print_text():
    userInput = entry.get()
    label2 = tk.Label(window, text="The printed text is: "+userInput, font=("Helvetica", 30))
    label2.place(x=50, y=100)
  
# Button to trigger the printing of text
button = tk.Button(window, text="Print", command=print_text) 
button.place(x=50, y=80)

# Run the window
window.mainloop()