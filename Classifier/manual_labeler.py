from tkinter import *
from tkinter import ttk

root = Tk()
frm = ttk.Frame(root, padding=10)
frm.grid()
ttk.Label(frm, text="Hello World!").grid(column=0, row=0)
ttk.Button(frm,text ="Good").grid(column=0,row=2)
ttk.Button(frm,text ="Bad").grid(column=1,row=2)
ttk.Button(frm,text ="Neutral").grid(column=2,row=2)
ttk.Button(frm,text ="Win").grid(column=3,row=2)
ttk.Button(frm, text="Quit", command=root.destroy).grid(column=0, row=4)
root.mainloop()