# -*- coding: utf-8 -*-
"""
Created on Wed Jun 29 16:36:19 2016

@author: jifangzhuji
"""

from tkinter import *
from dialogTable import demos
from quitter import Quitter

class Demo(Frame):
    def __init__(self,parent=None):
        Frame.__init__(self,parent)
        self.pack()
        Label(self,text="basic demos").pack()
        for key in demos:
            func=(lambda key=key:self.printit(key))
            Button(self,text=key,command=func).pack(side=TOP,fill=BOTH)
        Quitter(self).pack(side=TOP,fill=BOTH)
    
    def printit(self,name):
        print(name,'return=>',demos[name]())

if __name__=='__main__':
    Demo().mainloop()
    