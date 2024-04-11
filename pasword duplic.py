# Password Generator
from tkinter import*

import random

#its has two methods copy(), paste()
import pyperclip
#creating a window
w=Tk()
#size of the window
w.geometry('400x400')
#window background color
w.configure(bg="cyan")
#password format to store
pswd=StringVar()
#password lenght to store
pslen=IntVar()

#password_generator loop to iterate to the password for given lenght

def paswordgenerator():
    characters="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNPQRSTUVWXYZ1234567890!@#$%^&*()"
    password=''
    if pslen.get()>=8:
        for i in range(pslen.get()):
            password+=random.choice(characters)
        pswd.set(password)

 # to copy the password
   
def clipboard():
    clip=pswd.get()
    pyperclip.copy(clip)
    Label(w,text="copied the password",bg="red").pack(ipadx=50,ipady=10)
#label shows 
Label(w,text="Enter lenght below to get the Password",bg="magenta",foreground="black").pack(ipadx=120,ipady=20)

#type the lenght it can retrive the langht given
Entry(w, textvariable=pslen,bg="yellow").pack(pady=9)

#click the button to get password for given lenght
Button(w,text="Generate password",command=paswordgenerator,bg="white").pack(ipadx=90,ipady=10)

#shows the password Generated
Entry(w,text=pswd,bg="pink",fg="black").pack(pady=5)

#to copy the password click the button below
Button(w,text="copy to clipboard",command=clipboard,bg="black",fg="white").pack(ipadx=80,ipady=7)

# To Display the created Window
w.mainloop()