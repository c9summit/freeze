#Harsahil Basra
#07/06/22
#Julie's Party Hire Code
#This program is so Julie can keep a track of which items are being hired

#import tkinter to make a GUI
from tkinter import*
from tkinter import ttk


#Create 1st window for entry
root = Tk()
root.title("Julie's Hire Store")
root.geometry('400x200')



#Create 2nd window and add its components
def windowtwo():
    secondwindow = Toplevel()
    secondwindow.title('Customer Information')
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
    #Number Of Items Hired text
    Label(secondwindow, text="No. Of Items Hired").grid(column=0, row=4)
    entry_noofitems = Entry(secondwindow)
    entry_noofitems.grid(column=1, row=4)
    #Add quit button
    Button(secondwindow, text="Quit", command=secondwindow.destroy).grid(column=3,row=0, sticky=N+E, padx=45)



#Create button to take user to 2nd window
Button(root, text="Open Second Window", command=windowtwo).pack()



mainloop()
