#Harsahil Basra
#07/06/22
#Julie's Party Hire Code
#This program is so Julie can keep a track of which items are being hired

#import tkinter to make a GUI
from tkinter import*


#Create 1st window for entry
root = Tk()
root.title("Julie's hire store")

def open():
    top = Toplevel()
    top.title('Customer Information')
    btn2 = Button(top, text="close window", command=top.destroy).pack()

#Create button to take user to 2nd window
btn = Button(root, text="Open Second Window", command=open).pack()

root.geometry('400x200')

#Add title of store and other aesthetics such as colour and font






mainloop()
