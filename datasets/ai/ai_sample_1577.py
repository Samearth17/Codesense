import tkinter as tk

#Create root window
window = tk.Tk()
window.title('Python Code Selector')

#Create a selection frame
selection_frame = tk.Frame(window, bd=2, relief=tk.SUNKEN)
selection_frame.pack(fill = tk.X)

languages = ['Python 2.7', 'Python 3.4', 'Python 3.6', 'Python 3.7']

#Create a variable to store current language
language_var = tk.StringVar(selection_frame)
language_var.set(languages[0])

#Create a pull down menu
language_dropdown = tk.OptionMenu(selection_frame, language_var, *languages)
language_dropdown.pack(side=tk.LEFT)

#Create a button to accept the selection
accept_button = tk.Button(selection_frame, text='Accept', command=accept_selection)
accept_button.pack(side=tk.RIGHT)

#Create a function to accept the selection
def accept_selection():
	print(language_var.get())

window.mainloop()