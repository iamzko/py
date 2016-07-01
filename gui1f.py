# -*- coding: utf-8 -*-
"""
Created on Tue Jun 28 16:05:03 2016

@author: jifangzhuji
"""
"""
from tkinter import *
widget=Label()
widget['text']='Hello GUI world!'
widget.pack(side=TOP)
mainloop()
"""
from tkinter import *
root=Tk()
widget=Label(root)
widget.config(text='Hello GUI world!')
widget.pack(side=TOP,expand=YES,fill=BOTH)
root.title('guif.py')
root.mainloop()
