#test

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
    Button(top, text="Quit", command=top.destroy) .grid(column=400, row=0, sticky=E, padx=365)
    top.geometry('400x200')


#Create button to take user to 2nd window
Button(root, text="Open Second Window", command=open).pack()

#Creating code for labels on the second window



mainloop()
