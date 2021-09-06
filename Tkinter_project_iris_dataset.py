# -*- coding: utf-8 -*-
"""
Created on Fri May 21 11:56:55 2021

@author: MANJEET KUMAR YADAV
"""
from tkinter import *  

root=Tk()
root.geometry("800x500+1000+100")
root.title("Plant_Types")
root.configure(background="lightgreen")

def result():
    from sklearn.datasets import load_iris 
    dataset = load_iris()
    X=dataset.data
    y=dataset.target
    flower_type =dataset.target_names
    
    from sklearn.neighbors import KNeighborsClassifier
    knn=KNeighborsClassifier()
    knn.fit(X,y)
    
    sl=ent1.get()
    sw=ent2.get()
    pl=ent3.get()
    pw=ent4.get()
   
    X_test = [sl,sw,pl,pw]
    y_pred =knn.predict([X_test,])
    t=flower_type[y_pred]
    var5.set(t[0])


#-------------------------------- Label Widget -------------------------------------

lb1=Label(root,text="Enter the Sepal Length :",font=1,bg="lightgreen")
lb1.place(x=90,y=60)

lb2=Label(root,text="Enter the Sepal Width  :",font=1,bg="lightgreen")
lb2.place(x=90,y=100)

lb3=Label(root,text="Enter the Petal Length  :",font=1,bg="lightgreen")
lb3.place(x=90,y=140)

lb4=Label(root,text="Enter the Petal Width    :",font=1,bg="lightgreen")
lb4.place(x=90,y=180)

lb5=Label(root,text="Result    :",font=1,bg="lightgreen")
lb5.place(x=90,y=280)


#-------------------------------------- Entery Widget -----------------------------------

var1=IntVar()
var1.set("")
var2=IntVar()
var2.set("")
var3=IntVar()
var3.set("")
var4=IntVar()
var4.set("")
var5=StringVar()
ent1=Entry(root,font=1,textvariable=var1)
ent1.place(x=280,y=60)

ent2=Entry(root,font=1,textvariable=var2)
ent2.place(x=280,y=100)

ent3=Entry(root,font=1,textvariable=var3)
ent3.place(x=280,y=140)

ent4=Entry(root,font=1,textvariable=var4)
ent4.place(x=280,y=180)

ent5=Entry(root,font=1,textvariable=var5)
ent5.place(x=280,y=280)


#------------------------- Button widget ################

bt1=Button(root,text="submit",font=1,bg="orange",width=6,command=result)
bt1.place(x=280,y=230)

root.mainloop()
