import tkinter

def on_submit():
 print(user_input.get())

# Create the main window
root = tkinter.Tk()
root.geometry("300x200")

# Create a textbox
user_input = tkinter.Entry(root)
user_input.pack()

# Create the submit button
submit_button = tkinter.Button(root, text="Submit", command=on_submit)
submit_button.pack()

# Run the main loop
root.mainloop()