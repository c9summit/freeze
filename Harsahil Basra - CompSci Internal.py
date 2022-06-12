#Harsahil Basra
#07/06/22
#Julie's Party Hire Code
#This program is so Julie can keep a track of which items are being hired

#import tkinter to make a GUI
from tkinter import*


#Create 1st window for entry
root = Tk()
root.title("Julie's Hire Store")
root.geometry('400x200')

#Create 2nd window for entry
def open():
    top = Toplevel()
    top.title('Customer Information')
    Button(top, text="Quit", command=top.destroy).grid(column=3,row=0, sticky=N+E, padx=355)
    top.geometry('400x200')
    #Add customer name text
    Label(top,text="Customer Full Name").grid(column=0, row=1)
    #Add textbox for user to enter the customer's full name
    entry_customername = Entry(top)
    entry_customername.grid(column=1, row=1)

#Create button to take user to 2nd window
Button(root, text="Open Second Window", command=open).pack()


mainloop()
