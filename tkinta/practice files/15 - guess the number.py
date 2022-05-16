#15 - guess the number

from tkinter import * # imports everything from TK
from tkinter import ttk
import random

root=Tk()

#Create entry boxes
entry = ttk.Entry(root, width=15) #size of the field for entry
entry.insert(0," ")

#add a button to the window
button=ttk.Button(root,text='Quit')
button2=ttk.Button(root,text='Check')


lblname = ttk.Label(text='Guess the number: ')
lblname.grid(row=3, column=0, sticky=W)
entry.grid(row=3, column=1)
button.grid(row=1, column=0, sticky=W, pady=5)
button2.grid(row=1, column=1,sticky=E, pady=5)

def quit():
    main_window.destroy()

def number_guess():
    secret_number - numbers['secret number']
    print(secret_number)
    if int(entry_guess_number.get()) == secret_number:
        print("You guessed correctly")
    else:
        print("Try Again")


root.geometry("275x66")
root.mainloop()
