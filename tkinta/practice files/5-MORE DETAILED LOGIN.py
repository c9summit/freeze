#5 - MORE DETAILED LOGIN

from tkinter import * #IMPORTED EVERYTHING FROM TKINTER
from tkinter import ttk #SUBMODULE OF TKINTER

root=Tk()
def callback():
    val1=entry.get()
    val2=entry2.get()
    print("Your name is :" +val1)
    print("Your password is :" +val2)

entry = ttk.Entry(root,width=30) #size of the field
entry2 = ttk.Entry(root, width=30) 
entry.insert(0,'Please enter your name')#0 is the index - first charcter
entry2.config(show='*')#this will hiss pw or the text entered

#ADD A BUTTON TO THE WINDOW
button=ttk.Button(root,text='Click Me!',command=callback)
#WHEN YOU PUT IN A COMMAND YOU NEED TO WRITE A FUNCTION U

entry.pack()
entry2.pack()
button.pack() #MUST BE AFTER ENTRYPACK

root.geometry("300x300")
root.mainloop()
    
