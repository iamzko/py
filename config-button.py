# -*- coding: utf-8 -*-
"""
Created on Wed Jun 29 13:42:56 2016

@author: jifangzhuji
"""

def oyeah():
    print('yooooooo')
    
    
from tkinter import *
widget=Button(text='spam',padx=10,pady=10,command=oyeah)
widget.pack(padx=40,pady=40)
widget.config(cursor='gumby')
widget.config(bd=8,relief=RAISED)
widget.config(bg='dark green',fg='white')
widget.config(font=('helvetica',20,'underline italic'))
mainloop()


