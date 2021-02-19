from tkinter import * 
from PIL import ImageTk, Image
import os
window = Tk()

def save_details():
    with open('information.txt', 'w') as f:

        f.write(
            f'\n\nThe name of the student is:- {name_entry.get()}\n'
            f'The date of birth of student is:- {date_entry.get()}\n'
            f'The instrument played by student is:- {intrument_entry.get()}\n'
            f'The phone number of the student is:-- {phone_entry.get()}\n'
            )

window.geometry('945x400')
window.minsize(945,400)
window.maxsize(945,400)
window.title("SAIYAM'S MUSIC CLASS")


f1 = Frame(window,bg='red', borderwidth=20,relief=RIDGE)
f1.pack(side=TOP)

tile = Label(f1,text='WELCOME TO SAIYAM MUSIC CLASSES', fg='blue',font=('cosmicsansm', 35, 'bold'))
tile.pack(side=TOP,fill=X)

f2 = Frame(window, bg='blue', borderwidth=20, relief=SUNKEN)
f2.pack(side=LEFT, fill=Y)

f3 = Frame(window, borderwidth=15, relief=SUNKEN,bg='red')
f3.pack(side=RIGHT, fill=Y)

img = ImageTk.PhotoImage(Image.open("Picture.png"))
panel = Label(f3, image = img)
panel.pack(side = "bottom", fill = "both", expand = "yes")

photo = ImageTk.PhotoImage(Image.open("Picture2.png"))
pan = Label(window, image = photo)
pan.pack(side = 'bottom', fill = "both", expand = "yes")

# This function will take the input of name. 

name = Label(f2,bg='grey', fg='black',text='Name')
name.grid(row=1)
namevalue = StringVar
name_entry = Entry(f2, textvariable=namevalue)
name_entry.grid(row=1, column=2)

# This function will take the input of date of birth.

date_of_birth = Label(f2,bg='grey', fg='black',text='Date Of Birth') 
date_of_birth.grid(row=3)
datevalue =StringVar
date_entry = Entry(f2, textvariable=StringVar)
date_entry.grid(row=3, column=2)
# This function will take the input of instrument

instrument =Label(f2,bg='grey', fg='black',text='Instrument')
instrument.grid(row=5)
instrumentvalue = StringVar
intrument_entry = Entry(f2,textvariable=instrumentvalue )
intrument_entry.grid(row=5, column=2)

# This function will take the input of phone number

phone_number = Label(f2,bg='grey', fg='black',text='Phone Number')
phone_number.grid(row=7)
phonevalue =StringVar
phone_entry = Entry(f2, textvariable=phonevalue)
phone_entry.grid(row=7, column=2)

Button(f2, bg='red',text='Enter',command=save_details).grid(row=9)
window.mainloop()