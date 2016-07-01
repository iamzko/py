# -*- coding: utf-8 -*-
"""
Created on Sun Jun 12 11:23:20 2016

@author: jifangzhuji
"""

from tkinter import *
from tkinter102 import MyGui

mainwin=Tk()
Label(mainwin,text=__name__).pack()

popup=Toplevel()
Label(popup,text='Attach').pack(side=LEFT)
MyGui(popup).pack(side=RIGHT)
mainwin.mainloop()
