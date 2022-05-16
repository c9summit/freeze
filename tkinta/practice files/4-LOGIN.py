#4-LOGIN

from tkinter import * #IMPORTED EVERYTHING FROM TKINTER
from tkinter import ttk #SUBMODULE OF TKINTER

root = Tk()

entry = ttk.Entry(root,width=30) #size of the field
entry2 = ttk.Entry(root, width=30) 
entry.insert(0,'Please enter your name')#0 is the index - first charcter
entry2.config(show='*')#this will hiss pw or the text entered

entry.pack()
entry2.pack()

root.geometry("300x300")
root.mainloop()
