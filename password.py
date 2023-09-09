from tkinter import * 
from random import *

root = Tk()
root.title("Password Generator" )
root.geometry("500x300")
root.resizable(False , False)
root.configure(bg = "black")

password = chr(randint(33 , 126)) #33 to 126 are the ASCII values where we can take values from 1 to 32 as they include characters which wil be invaldid for creating a password


#functions
def new_random():
    pw_entry.delete(0 , END)
    pw_entry.length = int(entry.get())
    my_password = ''

    for x in range(pw_entry.length):
        my_password +=chr(randint(33 , 126))
    pw_entry.insert(0 , my_password)    
def clipper():
    root.clipboard_clear()
    root.clipboard_append(pw_entry.get())

#Label frame
lf = LabelFrame(root , text="Number of characters to generate password" ,fg = "white" , bg ="black")
lf.pack(pady =20)

#Entry Box
entry = Entry(lf , font= ("Helvetica" , 30 ) , bg = "black" , fg = "yellow")
entry.pack(pady =20 , padx= 20)
#Password entry box
pw_entry = Entry(root , text = '' , font = ("Helvetica" , 30) , bg = "black", fg = "yellow")
pw_entry.pack(pady = 20)
#frame for password
pw_frame = Frame(root , bg  = "black")
pw_frame.pack(pady = 20)

#create buttons
button = Button(pw_frame , text = "Generate a strong password" , command=new_random , bg = "green")
button.grid(row = 0 , column = 0 , padx = 20)

clip_button = Button(pw_frame , text = ("Copy to clipboard") , command = clipper , bg = "green")
clip_button.grid(row= 0,column=1 , padx = 20 )

root.mainloop()
