# -*- coding: utf-8 -*-
"""
Created on Sat May 22 07:48:39 2021

@author: MANJEET KUMAR YADAV
"""



#--------------------- Tkinter -----------------------------
from tkinter import *
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

root=Tk()
root.title("Cancer Prediction")
root.geometry("600x250+1000+100")
root.configure(background="lightgreen")

def func1():
    
    from sklearn.datasets import load_breast_cancer
    dataset=load_breast_cancer()
    
    X = dataset.data
    y = dataset.target
    
    from sklearn.svm import SVC
    model=SVC(kernel="linear")
    model.fit(X,y)

    t=var1.get()
    v=t+1
    a=X[t:v,0:]
    X_test=a[0]
    y_pred =model.predict([X_test])
    Label(root,text=dataset.target_names[y_pred[0]],font=("arial",15,"bold"),bg="red").place(x=260,y=160)
    
def func2():
    root.destroy()
    
def func3():
    var1.set("")
        
    
    
#----------------------------- Label Widget ----------------------------
lb1=Label(root,text="Enter the Number  :",font=1,bg="lightgreen")
lb1.place(x=60,y=40)

lb1=Label(root,text="Types of Cancer is  :",font=1,bg="lightgreen")
lb1.place(x=60,y=160)



var1=IntVar()
ent1=Entry(root,font=1,textvariable=var1,width=32)
ent1.place(x=220,y=40)

btn1=Button(root,text="Result",command=func1,width=8)
btn1.place(x=100,y=90)


btn2=Button(root,text="Exit",command=func2,width=8)
btn2.place(x=200,y=90)


btn2=Button(root,text="Cancel",command=func3,width=8)
btn2.place(x=300,y=90)



root.mainloop()

















