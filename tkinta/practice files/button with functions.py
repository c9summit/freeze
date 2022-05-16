#BUTTONWITHFUNCTIn

from tkinter import*
from tkinter import ttk

root = Tk()

button1 = Button(root,text = "Click Me!")#button cerated using tkinter
button2 =ttk.Button(root,text = "Click Me!")#button created using ttk
#if you run it now you will hace empty gui - the button
#button dont show up
#have to use geometry manager to be able to see the buttons
#here we will use .pack to show out buttons

button1.pack()
button2.pack()

root.geometry("350x300")
root.mainloop()







