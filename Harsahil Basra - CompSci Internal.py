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
    secondwindow = Toplevel()
    secondwindow.title('Customer Information')
    Button(secondwindow, text="Quit", command=secondwindow.destroy).grid(column=3,row=0, sticky=N+E, padx=355)
    secondwindow.geometry('400x200')
    #Customer's full name text
    Label(secondwindow,text="Customer Full Name").grid(column=0, row=1)
    #Create textbox for customer's fullname where the user can input 
    entry_customername = Entry(secondwindow)
    entry_customername.grid(column=1, row=1)
    #Receipt number's text
    Label(secondwindow, text="Receipt Number").grid(column=0,row=2)
    entry_receiptnumber = Entry(secondwindow)
    entry_receiptnumber.grid(column=1, row=2)
    #Item hired text
    Label(secondwindow, text="Item Hired").grid(column=0, row=3)
    entry_itemhired = Entry(secondwindow)
    entry_itemhired.grid(column=1, row=3)
    



#Create button to take user to 2nd window
Button(root, text="Open Second Window", command=open).pack()



mainloop()
