import tkinter as tk

# Create window
window = tk.Tk() 
window.title("Input-Output Program") 
window.geometry("400x200") 

#  Create a Label
message_heading = tk.Label(text="Input:") 
message_heading.grid(column=0, row=0)

# Create a text entry box
text_entry = tk.Entry() 
text_entry.grid(column=1, row=0)

# Create a Submit Button
submit_button = tk.Button(text="Submit", command=lambda: submit_input()) 
submit_button.grid(column=2, row=0)

# Output label
output_heading = tk.Label(text="Output:") 
output_heading.grid(column=0, row=2)

output_display = tk.Label()
output_display.grid(column=1, row=2) 

# Submit function
def submit_input(): 
    user_input = text_entry.get()
    output_display['text'] = user_input
    
# Create an event loop
window.mainloop()