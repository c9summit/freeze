#list box 3

from tkinter import*
from tkinter import ttk

root = Tk()

#below we will ad single/double or multiple/extended browse mode
#which lets you choose on or multiple items from list

#single selectrion from list
listBox=Listbox(root, width=40, height=15, selectmode=MULTIPLE)
#once you have run the program with single, change the mode to MULTIPLE
#and run it again and select the items of the list

listBox.insert(0, "Python") #0, 1, 2, ... are the index numbers
listBox.insert(1, "C++")
listBox.insert(2, "C#")
listBox.insert(3, "PHP")
listBox.pack(pady=25)

#create buttons
button = ttk.Button(root, text='Print', command=print_me).place(x=300, y=300)
button.config(command=callback)
button2 = ttk.Button(root, text='Delete', command=delete_me).place(x=350, y=300)
button2.config(command=callback)
#for these you need callback function and I want you to figure out
#how to write this out and ensure you are able to print and also delete items from the lsit

def callback():
    print("Your details: "+print_me.get())
    print("Deleted: "+delete_me.get())


root.geometry("650x650+650+200")
root.mainloop()
