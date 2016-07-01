# -*- coding: utf-8 -*-
"""
Created on Wed Jun 29 15:31:41 2016

@author: jifangzhuji
"""

from tkinter import *
from tkinter.messagebox import *

class Quitter(Frame):
    def __init__(self,parent=None):
        Frame.__init__(self,parent)
        self.pack()
        widget=Button(self,text='Quit',command=self.quit)
        widget.pack(side=LEFT,expand=YES,fill=BOTH)
    
    def quit(self):
        ans=askokcancel('Verify exit.','"Really quit?')
        if ans:
            Frame.quit(self)
if __name__=='__main__':
    w=Quitter()
    w.mainloop()