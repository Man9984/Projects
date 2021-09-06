# -*- coding: utf-8 -*-
"""
Created on Wed Jun 30 14:17:56 2021

@author: MANJEET KUMAR YADAV
"""


import cv2
from tkinter import *

root=Tk()
root.title("This is title")
root.geometry("700x350")
root.configure(background="lightgreen")
Label(root,text="CONVERTER",font=("arial",20,"bold")).place(x=260,y=20)
root.resizable(False,False)

def func1():
    v1 = var1.get()
    ex1 = var2.get()
    name=var3.get()    
    img = cv2.imread(v1)
    cv2.imwrite(r"C:\Users\MANJEET KUMAR YADAV\Desktop\{}.{}".format(name,ex1),img)
    var1.set("")
    var2.set("")
    var3.set("")
    
lb1=Label(root,text="Enter The File Path ",font=1,bg="lightgreen")
lb1.place(x=70,y=90)

var1=StringVar()
var1.set("")
ent1=Entry(root,font=1,textvariable=var1, width=25)
ent1.place(x=220,y=90)

lb2=Label(root,text="Convert Into",font=1, bg="lightgreen")
lb2.place(x=70,y=130)

var2=StringVar()
var2.set("")
ent2=Entry(root,font=1,textvariable=var2, width=25)
ent2.place(x=220,y=130)

lb3=Label(root,text="Enter The File Name",font=1, bg="lightgreen")
lb3.place(x=70,y=170)

var3=StringVar()
var3.set("")
ent3=Entry(root,font=1,textvariable=var3, width=25)
ent3.place(x=220,y=170)

Label(root,text="File Saved On Desktop",font=("arial",15,"bold")).place(x=190,y=230)

btn1=Button(root,text="Save",command=func1, width=10,bg="red")
btn1.place(x=270,y=290)
root.mainloop()
