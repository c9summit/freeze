#14 

from tkinter import * # imports everything from TK
from tkinter import ttk

root=Tk()
def callback():
    val1=entry.get()
    val2=entry2.get()
    print("Your name is :" +val1)
    print("Your Password is :" +val2)

#Create entry boxes
entry = ttk.Entry(root, width=30) #size of the field for entry
entry2 = ttk.Entry(root, width=30)
entry.insert(0,"Please enter your name: ")
entry2.insert(0, "Please enter your password: ")

#add a button to the window
button=ttk.Button(root,text='Quit')
button2=ttk.Button(root,text='Print')


lblname = ttk.Label(text='Your Name: ')
lblpass = ttk.Label(text='Your Password: ')
lblname.grid(row=1, column=0, sticky=W)  #W - left
lblpass.grid(row=2, column=0)
entry.grid(row=1, column=1)
entry2.grid(row=2, column=1)
button.grid(row=3, column=1, sticky=W, pady=5)
button2.grid(row=3, column=1, sticky=E, pady=5)



root.geometry("500x300")  # the size of the window
root.mainloop()
