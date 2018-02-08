from tkinter import *
from tkinter import ttk
root = Tk()
#root.resizable(FALSE,FALSE)
root.minsize(200,100)
root.maxsize(500,500)
little = ttk.Label(root, text="Little")
bigger = ttk.Label(root, text='Much bigger label')
little.grid(column=0,row=0)
bigger.grid(column=0,row=0)
root.after(2000, lambda: little.lift())
root.mainloop()