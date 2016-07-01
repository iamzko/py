# -*- coding: utf-8 -*-
"""
Created on Tue Jun 28 15:39:57 2016

@author: jifangzhuji
"""

from tkinter import *
root1=Tk()
root2=Tk()
Label(root1,text='Hello GUI world!').pack(side=TOP)
Label(root2,text='This is another one.').pack(side=RIGHT)
root1.mainloop()
root2.mainloop()

