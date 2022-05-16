#BUTTONTHATWORKS


from tkinter import * #IMPORTED EVERYTHING FROM TKINTA

root=Tk()#TOP LEVEL WINDOW
def callback():
    label.config(text='You clicked me!', fg='red', bg='yellow')
#HERE I HAVE ADDED FONT COLOUR AND BACKGROUND ON COLOUR ON CLICK

#CREATE LABEL
label = Label(root, text="Hello Python")
label.pack()

#CREATE BUTTON(WITH COMMAND FUNCTION
button =Button(root,text = 'Click Me!', command=callback)
button['state']='disabled' #can disable button
button['state']='normal' #back to normal
button.pack()

root.geometry("350x300")
root.mainloop()
