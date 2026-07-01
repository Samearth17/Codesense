import tkinter as tk
 
# create a main window
window = tk.Tk()
window.title("Email Client")  
    
# add labels and entry fields
lbl_from = tk.Label(window, text="From:")
lbl_from.grid(padx=10, pady=10, row=0, column=0, sticky="W")
ent_from = tk.Entry(window,width=50)
ent_from.grid(padx=10, pady=10, row=0, column=1)
 
lbl_to = tk.Label(window, text="To:")
lbl_to.grid(padx=10, pady=10, row=1, column=0, sticky="W")
ent_to = tk.Entry(window,width=50)
ent_to.grid(padx=10, pady=10, row=1, column=1) 
 
lbl_subject = tk.Label(window, text="Subject:")
lbl_subject.grid(padx=10, pady=10, row=2, column=0, sticky="W")
ent_subject = tk.Entry(window,width=50)
ent_subject.grid(padx=10, pady=10, row=2, column=1)
 
lbl_body = tk.Label(window, text="Body:")
lbl_body.grid(padx=10, pady=10, row=3,column=0, sticky="W")
txt_body = tk.Text(window, height=10, width=50)
txt_body.grid(padx=10, pady=10, row=3, column=1)
 
# enter main loop
window.mainloop()