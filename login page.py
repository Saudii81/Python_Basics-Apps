
from tkinter import *
pswd = Tk()
e = Entry(pswd)
e.pack(side = BOTTOM)

def callback():
    print(e.get())

#b = Button(pswd, text="password",width=20,command=callback)
#b.pack(side = BOTTOM)



pas = "password"

user = {"username": " ","password": " "}
if user == pas :
    print("sucess")
else:
    print("error")
    
mainloop()





