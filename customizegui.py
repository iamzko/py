# -*- coding: utf-8 -*-
"""
Created on Sun Jun 12 11:28:31 2016

@author: jifangzhuji
"""

from tkinter import mainloop
from tkinter.messagebox import showinfo
from tkinter102 import MyGui

class CustomGui(MyGui):
    def reply(self):
        showinfo('popup','Ouch!')

if __name__=='__main__':
    CustomGui().pack()
    mainloop()