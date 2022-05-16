#icons on gui

from tkinter import*

root = Tk()
root.title("Using Images")
root.geometry("350x350")

#in order to insert create a folder called icones where your tkinter files are
#saved and save some icons

#create label
lbl_text = Label(root, text="Using Images", font=(("Times"), 18))
lbl_text.pack()

#insert image
logo = PhotoImage(file='globe.png')

#we will create a label to store the image which acts as a container for image
lbl_image = Label(root, image=logo)
lbl_image.pack()

root.mainloop()
