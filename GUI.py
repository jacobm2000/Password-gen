from tkinter import *
from Generator import *
def getPass():
    pout.delete(1.0,"end")
    p=genCheck()
    pout.insert(END,p)
    print(p)
   
window = Tk()
# set window title
window.title("Password Generator")
# set window width and height
window.configure(bg='lightgray')
var=StringVar()
l=Label(window,textvariable=var,bg='lightgray')
var.set("Password Generator")
l.pack()
# set window background color

pout=Text(window,height=1,width=25)
pout.insert(INSERT,"")
#this line prevents users from typing in box
#pout.bind("<Key>", lambda e: "break")
pout.pack(pady=100)

window.geometry("300x300")


b=Button(window,text="Get Pass", command=getPass)
b.pack()


window.mainloop()
