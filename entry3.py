# -*- coding: utf-8 -*-
"""
Created on Thu Jun 30 10:49:58 2016

@author: jifangzhuji
"""

from tkinter import *
from quitter import Quitter
fields='Name','Job','Pay'

def fetch(variables):
    for variable in variables:
        print('Input => "%s"'%variable.get())

def makeform(root,fields):
    form=Frame(root)
    left=Frame(form)
    rite=Frame(form)
    form.pack(fill=X)
    left.pack(side=LEFT)
    rite.pack(side=RIGHT,expand=YES,fill=X)
    
    variables=[]
    for field in fields:
        lab=Label(left,width=5,text=field)
        ent=Entry(rite)
        lab.pack(side=TOP)
        ent.pack(side=TOP,fill=X)
        var=StringVar()
        ent.config(textvariable=var)
        var.set('enter here')
        variables.append(var)
    return variables

if __name__=='__main__':
    root=Tk()
    vars=makeform(root,fields)
    Button(root,text='fetch',command=(lambda:fetch(vars))).pack(side=LEFT)
    Quitter(root).pack(side=RIGHT)
    root.bind('<Return>',(lambda event:fetch(vars)))
    root.mainloop()