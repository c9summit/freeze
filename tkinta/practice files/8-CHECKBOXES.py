#8 - CHECKBOXES

from tkinter import * #IMPORTED EVERYTHING FROM TKINTER
from tkinter import ttk #SUBMODULE OF TKINTER

root=Tk()

def callback():
    val1=entry,get()
    val2=entry2.get()
    print("Your name is: " +val1)
    print('Your password is: ' +val2)

#create entry boxes
entry=ttk.Entry(root, width=30) #size of field for entry
entry2=ttk.Entry(root, width=30)
entry.insert(0, 'Please enter your name')
entry2.insert(0, 'Please enter your password')

#add button
button=ttk.Button(root,text='Enter')

#add labels
lbltitle = ttk.Label(text='Out title Goes Here',font=(('Arial'),22))
lblname=ttk.Label(text='Your Name: ')
lblpass=ttk.Label(text='Your Password: ')
lbltitle.grid(row=0, column=0, columnspan=2) 
lblname.grid(row=1, column=0, sticky=W)
lblpass.grid(row=2, column=0)
entry.grid(row=1, column=1)
entry2.grid(row=2, column=1)
button.grid(row=3, column=1, sticky=E+W, pady=5)

#checkbox
chvar=IntVar() #checkbox variable
chvar.set(0) #set to 0 - means not checker

#checkbox variable
cbox=Checkbutton(root,text='Remember Me', variable=chvar, font='Arial 16').grid(row=4,column=0)
#sticky=E, columnspan=2 #in order to get it align right

root.geometry('500x450')
root.mainloop()
