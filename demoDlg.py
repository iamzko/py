# -*- coding: utf-8 -*-
"""
Created on Wed Jun 29 16:02:35 2016

@author: jifangzhuji
"""

from tkinter import *
from dialogTable import demos
from quitter import Quitter

class Demo(Frame):
    def __init__(self,parent=None,**options):
        Frame.__init__(self,parent,**options)
        self.pack()
        Label(self,text='Basic demos').pack()
        for (key,value) in demos.items():
            Button(self,text=key,command=value).pack(side=TOP,fill=BOTH)
        Quitter(self).pack(side=TOP,fill=BOTH)
if __name__=='__main__':
    Demo().mainloop()