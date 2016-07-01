# -*- coding: utf-8 -*-
"""
Created on Wed Jun 29 15:14:38 2016

@author: jifangzhuji
"""

from tkinter import *
from tkinter.messagebox import *
def callback():
    if askyesno('verify','Do you really want to quit?'):
        showwarning('yes','Quit not yet implemented')
    else:
        showinfo('No','Quit has been cancelled')

errmsg='Sorry , no spam allowed!!'
Button(text='Quit',command=callback).pack(fill=X)
Button(text='Spam',command=(lambda:showerror('Spam',errmsg))).pack(fill=X)
mainloop()