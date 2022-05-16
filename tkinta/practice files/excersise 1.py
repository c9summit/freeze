#tkinta

from tkinter import * #imports everything from tk - tkinter is a module
from tkinter import ttk #ttk is a sub module of tkinta

root = Tk() #Top level window
#create label widget
label = Label(root, text="Hello Python") #what you see on screen
#font colour, config is for properties
label.config(text="Hello Python", fg="red")
label.config(bg="yellow") #background colour
label.config(font = 'Times 20')

label.config(text='Python is a great program and we can do lots with it')
label.config(wraplength='150') #wrap text if 
label.config(justify="right")

#showing it on screen
label.pack()
root.geometry("300x250")

root.mainloop() #gui is always looping -
#when you run your mouse over you can click
