"""
This code creates a GUI calculator using Python and Tkinter.

Step 1: Create a main window using tkinter.

import tkinter as tk

root = tk.Tk()
root.title("Calculator")
root.geometry("400x500")

Step 2: Add all the necessary buttons for the calculator.

# Create all button widgets
btn_zero = tk.Button(root, text="0", bg="black", fg="white")
btn_one = tk.Button(root, text="1", bg="black", fg="white")
btn_two = tk.Button(root, text="2", bg="black", fg="white")
btn_three = tk.Button(root, text="3", bg="black", fg="white")
btn_four = tk.Button(root, text="4", bg="black", fg="white")
btn_five = tk.Button(root, text="5", bg="black", fg="white")
btn_six = tk.Button(root, text="6", bg="black", fg="white")
btn_seven = tk.Button(root, text="7", bg="black", fg="white")
btn_eight = tk.Button(root, text="8", bg="black", fg="white")
btn_nine = tk.Button(root, text="9", bg="black", fg="white")
btn_decimal = tk.Button(root, text=".", bg="black", fg="white")
btn_clear = tk.Button(root, text="Clear", bg="black", fg="white")
btn_plus = tk.Button(root, text="+", bg="black", fg="white")
btn_minus = tk.Button(root, text="-", bg="black", fg="white")
btn_multiply = tk.Button(root, text="*", bg="black", fg="white")
btn_divide = tk.Button(root, text="/", bg="black", fg="white")
btn_equals = tk.Button(root, text="=", bg="black", fg="white")

Step 3: Use a grid layout to position all the widgets on the screen.

# Use grid layout to position all buttons
btn_zero.grid(row=4, column=1)
btn_one.grid(row=3, column=0)
btn_two.grid(row=3, column=1)
btn_three.grid(row=3, column=2)
btn_four.grid(row=2, column=0)
btn_five.grid(row=2, column=1)
btn_six.grid(row=2, column=2)
btn_seven.grid(row=1, column=0)
btn_eight.grid(row=1, column=1)
btn_nine.grid(row=1, column=2)
btn_decimal.grid(row=4, column=0)
btn_clear.grid(row=4, column=2)
btn_plus.grid(row=5, column=0)
btn_minus.grid(row=5, column=1)
btn_multiply.grid(row=5, column=2)
btn_divide.grid(row=6, column=0)
btn_equals.grid(row=6, column=1, columnspan=2)

Step 4: Add functionality to the calculator.

# Function to calculate result
def calculate():
    
    # Get the user input
    user_input = text_input.get()

    # Try and evaluate the user input
    try:
        result = eval(user_input)
        text_input.delete(0, "end")
        text_input.insert(0, result)
    except:
        pass

# Create a text entry box for input
text_input = tk.Entry(root, width=50, bg="white")
text_input.grid(row=0, column=0, columnspan=4)

# Add command to all button widgets
btn_zero.config(command=lambda: text_input.insert(tk.END, "0"))
btn_one.config(command=lambda: text_input.insert(tk.END, "1"))
btn_two.config(command=lambda: text_input.insert(tk.END, "2"))
btn_three.config(command=lambda: text_input.insert(tk.END, "3"))
btn_four.config(command=lambda: text_input.insert(tk.END, "4"))
btn_five.config(command=lambda: text_input.insert(tk.END, "5"))
btn_six.config(command=lambda: text_input.insert(tk.END, "6"))
btn_seven.config(command=lambda: text_input.insert(tk.END, "7"))
btn_eight.config(command=lambda: text_input.insert(tk.END, "8"))
btn_nine.config(command=lambda: text_input.insert(tk.END, "9"))
btn_decimal.config(command=lambda: text_input.insert(tk.END, "."))
btn_clear.config(command=lambda: text_input.delete(0, tk.END))
btn_plus.config(command=lambda: text_input.insert(tk.END, "+"))
btn_minus.config(command=lambda: text_input.insert(tk.END, "-"))
btn_multiply.config(command=lambda: text_input.insert(tk.END, "*"))
btn_divide.config(command=lambda: text_input.insert(tk.END, "/"))
btn_equals.config(command=calculate)

# Mainloop
root.mainloop()
"""