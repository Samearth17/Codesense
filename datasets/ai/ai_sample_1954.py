import tkinter
 
def mbutton():
    t = tkinter.Toplevel()
    t.geometry('400x400')
    t.title('New Window')
    tkinter.Button(t, text='Click me').pack()
 
root = tkinter.Tk()
root.geometry('200x200')
b1 = tkinter.Button(root, text='Open new window', command=mbutton)
b2 = tkinter.Button(root, text='Close', command=root.destroy)
b1.pack()
b2.pack() 
root.mainloop()