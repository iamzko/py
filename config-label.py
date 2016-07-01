# -*- coding: utf-8 -*-
"""
Created on Wed Jun 29 13:03:49 2016

@author: jifangzhuji
"""

from tkinter import *
root=Tk()
labelfont=('times',20,'bold')
widget=Label(root,text='今天天气不错')
widget.config(bg='blue',fg='red')
widget.config(font=labelfont)
widget.config(height=3,width=20)
widget.config(bd=10,relief=RIDGE,cursor='hand2')
widget.pack(expand=YES,fill=BOTH)
root.mainloop()