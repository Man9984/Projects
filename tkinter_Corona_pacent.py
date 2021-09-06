# -*- coding: utf-8 -*-
"""
Created on Fri May 21 16:23:10 2021

@author: MANJEET KUMAR YADAV
"""


from tkinter import *
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import sklearn as sns

# -----------------------------------------------------------------------------------------
root=Tk()
root.geometry("600x600+1200+200")
root.configure(background="lightgreen")
root.title("Corona_virus_Prediction_System :")
root.resizable(0,0)

#-------------------------------- Label Widget -------------------------------------

label=Label(root,text="Corona_virus_Prediction_App",font=("arial",15,"bold"),bg="light green",fg="black")
label.place(x=85,y=20)


lb1=Label(root,text="Enter the Body_tempreture in F",font=1,fg="black",relief="solid",width=25)
lb1.place(x=50,y=80)

lb2=Label(root,text="Enter the Person_Age",font=1,fg="black",relief="solid",width=25)
lb2.place(x=50,y=120)

lb3=Label(root,text="Enter the Breath_Problem",font=1,fg="black",relief="solid",width=25)
lb3.place(x=50,y=160)

lb4=Label(root,text="Enter the Running_Nose",font=1,fg="black",relief="solid",width=25)
lb4.place(x=50,y=200)

lb5=Label(root,text="Enter the Body_Pain",font=1,fg="black",relief="solid",width=25)
lb5.place(x=50,y=240)

lb6=Label(root,text="Result Analysis",fg="black",relief="solid",width=25,font=1,height=1)
lb6.place(x=50,y=280)

lb7=Label(root,text="Variable Enery Info",fg="black",relief="solid",width=25,font=1,height=1)
lb7.place(x=50,y=320)

#--------------------------- Entry Widget ---------------------------------------
var1=IntVar()
var1.set("")
var2=IntVar()
var2.set("")
var3=IntVar()
var3.set("")
var4=IntVar()           
var4.set("")
var5=IntVar()
var5.set("")
var6=IntVar()
var6.set("")

ent1=Entry(root,font=1,textvariable=var1)
ent1.place(x=290,y=80)

ent2=Entry(root,font=1,textvariable=var2)
ent2.place(x=290,y=120)

ent3=Entry(root,font=1,textvariable=var3)
ent3.place(x=290,y=160)

ent4=Entry(root,font=1,textvariable=var4)
ent4.place(x=290,y=200)

ent5=Entry(root,font=1,textvariable=var5)
ent5.place(x=290,y=240)


#------------------------- Button Widget ######################
def info():
    win=Tk()
    win.geometry("350x270+800+200")
    win.title("Info")
    lb1=Label(win,text="Body tempreture in Degree Foregnhigt",font=1).pack()
    lb2=Label(win,text="person Age",font=1).pack()
    lb3=Label(win,text="Body pain Yes 1 No 0 ",font=1).pack()
    lb4=Label(win,text="Running Nose Yes 1 No 0",font=1).pack()
    lb5=Label(win,text="Body pain Yes 1 No 0",font=1).pack()
    
    win.mainloop()

def model():
    Dataset=pd.read_excel(r"F:\Data Science\ML(Abhisek sir)\New folder (2)\data_corna.xlsx",sheet_names="data_type1")
    X=Dataset.iloc[:,[1,2,4,5,6]]
    y=Dataset.iloc[:,-1]
    
    from sklearn.impute import SimpleImputer
    sm = SimpleImputer(missing_values=np.nan,strategy="median")
    X=sm.fit_transform(X)
    X=pd.DataFrame(X)
    
    from sklearn.linear_model import LogisticRegression
    lr = LogisticRegression()
    lr.fit(X,y)

    temp =float(ent1.get())
    age = float(ent2.get())
    breath_Problem =float(ent3.get())
    Run_nose =float(ent4.get())
    body_Pain =float(ent5.get())    
    
    X_test = [temp,age,breath_Problem,Run_nose,body_Pain]
    y_pred = lr.predict([X_test,])
    Label(root,text=str(y_pred[0]),bg="red",font=1,width=8).place(x=290,y=280)

    
def terminate():
    root.destroy()

btn1=Button(root,text="INFO",width=15, command=info)
btn1.place(x=290,y=320)

btn2=Button(root,text="Prediction",width=12, command=model ,font=1)
btn2.place(x=150,y=370)

btn3=Button(root,text="Termination",width=15, command=terminate ,font=1)
btn3.place(x=300,y=370)

root.mainloop()
