#7-GRIDMANAGER2
#FORMATTING OUT TITLE, LABEL AD BUTTON PLACEMENTS

from tkinter import * #IMPORTED EVERYTHING FROM TKINTER
from tkinter import ttk #SUBMODULE OF TKINTER

root=Tk()

#create entries
entry = ttk.Entry(root, width=30)
entry2 = ttk.Entry(root, width=30)

#create placeholder
entry.insert(0, 'Please enter your name')
entry2.insert(0, 'Please enter your password')

#create buttons and labels
button=ttk.Button(root, text='Enter')
lbltitle=ttk.Label(text='Our title here',font=(('Arial'),30))
lblname=ttk.Label(text='Your Name: ')
lblpass=ttk.Label(text='Your Password: ')

#positon of the button, labels and entries as outcome
lbltitle.grid(row=0, column=0, columnspan=2, pady=10) #move title to 2nd column
lblname.grid(row=1, column=0, sticky=W) #W = LEFT
lblpass.grid(row=2, column=0)

entry.grid(row=1, column=1)
entry2.grid(row=2, column=1)
button.grid(row=3, column=1, sticky=E+W)
#button.grid(row=3,column=1,sticky=E) will have button on right
#button.grid(row=3,column=1,sticky=W) will have button on left
#button.grid(row=3,column=1,sticky=E,pady=5) give you a bit of a gap between 2 rows
root.geometry('500x450')
root.mainloop()
