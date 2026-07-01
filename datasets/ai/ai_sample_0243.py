# Create the window
window = tk.Tk()

# Create two entry fields in the window
entry1 = tk.Entry(window)
entry2 = tk.Entry(window)

# Create a function to get inputs from the entry fields and calculate sum
def get_sum():
    num1 = entry1.get()
    num2 = entry2.get()
    sum = int(num1) + int(num2)
    label.config(text="Sum is " + str(sum))

# Create a button to execute the function
button = tk.Button(window, text="Calculate", command=get_sum)

# Create a label to display the result
label = tk.Label(window)

# Pack all widgets
entry1.pack()
entry2.pack()
button.pack()
label.pack()

# Main loop
window.mainloop()