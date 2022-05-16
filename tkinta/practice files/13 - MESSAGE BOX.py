#13 - MESSAGE BOX


from tkinter import *
from tkinter import ttk

root = Tk()
textEditor = Text(root, width=30, height=10, wrap=WORD) # 1st parameter is root
textEditor.grid(row=0, column=0, pady=20, padx=40)


button = Button(root, text='Save')#can use height and width properties
#for our button - button = Button(root, text='Save', width=10, height=1)
button.config(fg="blue", font='Times 20')
root.config(bg="yellow")

button.grid(row=3, column=0)

textEditor.insert(INSERT, 'Hello I am learning about tkinter widgets')

root.geometry("550x550")
root.mainloop()
