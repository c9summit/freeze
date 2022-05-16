#using while loop
j_names = ["Jaxon","James","Jesika","Jim","Jilly"]

print(j_names[2])
print("*")

name_counter = 0
while name_counter < len(j_names) :
    print(j_names[name_counter])
    name_counter += 1


#using for loop
"""

j_names = ["Jaxon","James","Jesika","Jim","Jilly"]
print(j_names[2])
print("*****")

for x in range(len(j_names)) :
    print(x,j_names[x])"""


#nested lists
"""
j_names = [["Jaxon","15"],["James","16"],["Jesika","12"],["Jim","14"],["Jilly","17"]]
name_count = 0
while name_count < 5 :
    print(j_names[name_count][0])
    name_count += 1

print("")
name_count = 0
while name_count <5 :
    print(j_names[name_count][1])
    name_count += 1

print('')
name_count = 0
while name_count < 5 :
    print(j_names[name_count][0],j_names[name_count][1])
    name_count += 1"""


#added another name to lsit and add another column for male/female
"""
j_names = [["Jaxon","15","Male"],["James","16","Male"],["Jesika","12","Female"],["Jim","14","Male"],["Jilly","17","Female"],["Manveer","16","Female"]]
name_count = 0
while name_count < 6 :
    print(j_names[name_count][0])
    name_count += 1

print("")
name_count = 0
while name_count < 6 :
    print(j_names[name_count][1])
    name_count += 1

print("")
name_count = 0
while name_count < 6 :
    print(j_names[name_count][0],j_names[name_count][1])
    name_count += 1

print("")
name_count = 0
while name_count < 6 :
    print(j_names[name_count][0],j_names[name_count][1],j_names[name_count][2])
    name_count += 1"""


#gui
'''
from tkinter import *

def quit():
    main_window.destroy()

def print_names ():
    global j_names, total_entries
    name_count = 0
    Label(main_window, font='bold',text="Name").grid(column=0,row=5)
    Label(main_window, font='bold',text="Age").grid(column=1,row=5)
    Label(main_window, font='bold',text="Gender").grid(column=2,row=5)
    while name_count < total_entries :
        Label(main_window, text=(j_names[name_count][0])).grid(column=0, row=name_count+6)
        Label(main_window, text=(j_names[name_count][1])).grid(column=1, row=name_count+6)
        Label(main_window, text=(j_names[name_count][2])).grid(column=2, row=name_count+6)
        name_count += 1

def append_name ():
    global j_names, entry_name, entr_age, entry_gender, total_entries
    j_names.append([entry_name.get(),entry_age.get(),entry_gender.get()])
    entry_name.delete(0,'end')
    entry_age.delete(0,'end')
    entry_gender.delete(0,'end')
    total_entries += 1

def setup_buttons():
    global j_names, entry_name, entry_age, entry_gender, total_entries
    Button(main_window, text="Quit",command=quit).grid(column=1, row=0)
    Button(main_window, text="Append Details",command=append_name).grid(column=0, row=1)
    Button(main_window, text="Print Details",command=print_names).grid(column=1, row=1)
    Label(main_window, text="Name").grid(column=0,row=2)
    entry_name = Entry(main_window)
    entry_name.grid(column=1,row=2)
    Label(main_window, text="Age").grid(column=0,row=3)
    entry_age = Entry(main_window)
    entry_age.grid(column=1,row=3)
    Label(main_window, text="Gender").grid(column=0,row=4)
    entry_gender = Entry(main_window)
    entry_gender.grid(column=1,row=4)

def main():
    global main_window
    global j_names, entry_name, entry_age, entry_gender, total_entries
    j_names = []
    total_entries = 0
    main_window = Tk()
    setup_buttons()
    main_window.mainloop()

main()''' 
