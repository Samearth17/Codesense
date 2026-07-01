import tkinter as tk

window = tk.Tk()
window.title('Calculator')
window.geometry('300x150')

# Create the input field
input_field = tk.Entry(
 window,
 font=('Courier', 20),
 width=15,
 borderwidth=5
)
input_field.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Function to return the value of the button clicked
def button_pressed(value):
 current = input_field.get()
 input_field.delete(0, tk.END)
 input_field.insert(0, str(current) + str(value))

# Create button object
button_0 = tk.Button(window, text='0', padx=40, pady=20, command=lambda: button_pressed(0))
button_1 = tk.Button(window, text='1', padx=40, pady=20, command=lambda: button_pressed(1))
button_2 = tk.Button(window, text='2', padx=40, pady=20, command=lambda: button_pressed(2))
button_3 = tk.Button(window, text='3', padx=40, pady=20, command=lambda: button_pressed(3))
button_4 = tk.Button(window, text='4', padx=40, pady=20, command=lambda: button_pressed(4))
button_5 = tk.Button(window, text='5', padx=40, pady=20, command=lambda: button_pressed(5))
button_6 = tk.Button(window, text='6', padx=40, pady=20, command=lambda: button_pressed(6))
button_7 = tk.Button(window, text='7', padx=40, pady=20, command=lambda: button_pressed(7))
button_8 = tk.Button(window, text='8', padx=40, pady=20, command=lambda: button_pressed(8))
button_9 = tk.Button(window, text='9', padx=40, pady=20, command=lambda: button_pressed(9))
button_add = tk.Button(window, text='+', padx=39, pady=20, command=lambda: button_pressed('+'))
button_sub = tk.Button(window, text='-', padx=41, pady=20, command=lambda: button_pressed('-'))
button_mul = tk.Button(window, text='*', padx=40, pady=20, command=lambda: button_pressed('*'))
button_div = tk.Button(window, text='/', padx=41, pady=20, command=lambda: button_pressed('/'))

# Place all the buttons
button_0.grid(row=4, column=0)
button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)
button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)
button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)
button_add.grid(row=4, column=3)
button_sub.grid(row=3, column=3)
button_mul.grid(row=2, column=3)
button_div.grid(row=1, column=3)

# Run the mainloop
window.mainloop()