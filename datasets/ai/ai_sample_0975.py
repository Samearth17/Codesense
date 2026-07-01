import tkinter

# Create the main window 
window = tkinter.Tk() 

# Set window title 
window.title('My Application') 

# Create a Label 
lbl = tkinter.Label(window, text ="Hello World!") 

# Set the position of Label 
lbl.grid(column = 0, row = 0) 

# Create a button 
btn = tkinter.Button(window, text ="Click Me") 

# Set the position of button 
btn.grid(column = 1, row = 0) 

# Create an event handler for button click 
def btn_clicked(): 
    lbl.configure(text ="You clicked the button!") 

# Add event handler for button click 
btn.configure(command =btn_clicked) 

# Just to keep window open 
window.mainloop()