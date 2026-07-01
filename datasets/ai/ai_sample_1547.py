import tkinter as tk
import pandas as pd

root= tk.Tk() 
canvas1 = tk.Canvas(root, width = 300, height = 300,  relief = 'raised')
canvas1.pack()

df = pd.DataFrame({'Product':['Apple','Banana','Orange'],'Price':[10,20,30]})

table = tk.LabelFrame(root, text='Product Table')
table.place(relx = 0.1, rely = 0.1, relwidth = 0.8, relheight = 0.8)

table_body = tk.Frame(table) 
table_body.place(relx = 0.1, rely = 0.1, relwidth = 0.8, relheight = 0.8)

data = df.values.tolist() 
column_headings = list(df.columns.values) 

frame_header = tk.Frame(table_body)
frame_header.pack(fill='both', expand='yes')

for col_h in column_headings:
    label=tk.Label(frame_header,text=str(col_h),font="Helvetica 10 bold")
    label.pack(fill='both', pady=10, padx=10, side='left')

frame_table=tk.Frame(table_body)   
frame_table.pack(fill='both', expand='yes')

row_num = 0

for row in data:
    col_num = 0
    for col in row:
        label = tk.Label(frame_table,text=str(col), relief='solid', width=10)
        label.grid(column=col_num, row=row_num)
        col_num += 1
    row_num += 1

root.mainloop()