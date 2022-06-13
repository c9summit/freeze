#Harsahil Basra
#07/06/22
#Julie's Party Hire Code
#This program is so Julie can keep a track of which items are being hired

#import tkinter to make a GUI
from tabnanny import check
from tkinter import*
from tkinter import ttk

#these are the global variables 
global hireinfo, entry_customername, entry_receiptnumber, entry_itemhired, entry_noofitems, firstwindow, secondwindow

#Create 1st window for entry
firstwindow = Tk()
firstwindow.title("Julie's Hire Store")
firstwindow.geometry('400x200')



#Create 2nd window and add its components
def windowtwo():
    secondwindow = Toplevel()
    secondwindow.title('Customer Information')
    secondwindow.geometry('500x500')
    #Create empty labels, buttons, entryboxes and putting them in correct grid location
    #Customer's full name text
    Label(secondwindow,text="Customer Full Name").grid(column=0, row=2)
    #Create textbox for customer's fullname where the user can input 
    entry_customername = Entry(secondwindow)
    entry_customername.grid(column=1, row=2)
    #Receipt number's text
    Label(secondwindow, text="Receipt Number").grid(column=0,row=3)
    entry_receiptnumber = Entry(secondwindow)
    entry_receiptnumber.grid(column=1, row=3)
    #Item hired text
    Label(secondwindow, text="Item Hired").grid(column=0, row=4)
    entry_itemhired = Entry(secondwindow)
    entry_itemhired.grid(column=1, row=4)
    #Number Of Items Hired text
    Label(secondwindow, text="No. Of Items Hired").grid(column=0, row=5)
    entry_noofitems = Entry(secondwindow)
    entry_noofitems.grid(column=1, row=5)
    #Add quit button
    def quit():
        firstwindow+secondwindow.destroy()
    Button(secondwindow, text="Close", command=secondwindow.quit).grid(column=3,row=0)
    #Adding append button
    Button(secondwindow, text="Append Info",command=check) .grid(column=2, row=6)
    #Adding Print Button
    Button(secondwindow, text="Print Info",command=check).grid(column=3, row=6)

#Create button to take user to 2nd window
Button(firstwindow, text="Open Second Window", command=windowtwo).pack()




mainloop()
