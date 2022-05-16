#12 - COMBOBOX2

from tkinter import * #IMPORTED EVERYTHING FROM TKINTER
from tkinter import ttk #SUBMODULE OF TKINTER

root=Tk()

def callback():
    print("Your name: "+entry.get())
    print("Your Password: "+entry2.get())
    if chvar.get()==1: #means checkbox it ticked
        print("Remember me selected")
    else:
        print("not selected")
    print(gender.get()) # this is where to get our gender value
    print(months.get())

#CREATE ENTRY BOXES
entry=ttk.Entry(root, width=30) #size of field for entry
entry2=ttk.Entry(root, width=30)
entry.insert(0, 'Please enter your name') #0 is the index - first character
entry2.insert(0, 'Please enter your password')

#add a button to the window
button=ttk.Button(root, text='ENTER')
button.config(command=callback)
#WHEN YOU PUT INA COMMAND YOU NEED TO WRITE AND FUCTION UNDER ROOT

#add label title
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
chvar=IntVar() #CHECKBOX VARIABLE
chvar.set(0) #set to 0 (zero) - means not checked

#checkbox variable
cbox=Checkbutton(root,text='Remember Me', variable=chvar,
                 font='Arial 16').grid(row=4,column=0,sticky=E,columnspan=2)#in order to get it alighn right

#CREATE ANOTHER VARIABLE
gender=StringVar()

#CREATE RADIOBUTTON
ttk.Radiobutton(root,text='Female',value='Female',var=gender).grid(row=5,column=0)
ttk.Radiobutton(root,text='Male',value='Male',var=gender).grid(row=5,column=1)


#checkbox variable
cbox=Checkbutton(root,text='Remember Me', variable=chvar,
                 font='Arial 16').grid(row=4,column=0,sticky=E,columnspan=2)#in order to get it alighn right

months=StringVar()
ComboBox=ttk.Combobox(root,textvariable = months,
                      values=('Jan', 'Feb','March','April'),state='readonly').grid(row=6,column=0)

year=StringVar()
Spinbox(root,from_=1990, to=2022,textvariable=year).grid(row=6,column=1)

root.geometry('500x450')
root.mainloop()


