import tkinter as tk

root = tk.Tk()
root.title('Sum Application')

num1 = tk.StringVar()
num2 = tk.StringVar()

def calculate():
    try:
        result = int(num1.get()) + int(num2.get())
        sumLabel.configure(text="The sum is %d" % result)
    except ValueError:
        sumLabel.configure(text="Please enter numbers")

num1Field = tk.Entry(root, width=10, textvariable=num1)
num2Field = tk.Entry(root, width=10, textvariable=num2)

sumButton = tk.Button(root, text="Sum", command=calculate)
sumLabel = tk.Label(root, text="")

num1Field.grid(row=0, column=0)
num2Field.grid(row=0, column=1)
sumButton.grid(row=1, column=0, columnspan=2)
sumLabel.grid(row=2, column=0, columnspan=2)

root.mainloop()