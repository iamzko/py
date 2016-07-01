# -*- coding: utf-8 -*-
"""
Created on Tue Jun 28 22:36:48 2016

@author: kai
"""

from tkinter import *
class Hello(Frame):
    def __init__(self,parent=None):
        Frame.__init__(self,parent)
        self.pack()
        self.data=42
        self.make_widget()
    
    def make_widget(self):
        widget=Button(self,text='Hello frame world!',command=self.message)
        widget.pack(side=LEFT)
    
    def message(self):
        self.data+=1
        print('Hello frame world %s'%self.data)


from sys import exit
"""
parent=Frame(None)
parent.pack()
Hello(parent).pack(side=RIGHT)
Button(parent,text='Attach',command=exit).pack(side=LEFT)
parent.mainloop()
"""
class HelloContainer(Frame):
    def __init__(self,parent=None):
        Frame.__init__(self,parent)
        self.pack()
        self.makeWidgets()
    
    def makeWidgets(self):
        Hello(self).pack(side=RIGHT)
        Button(self,text='Attach',command=self.quit).pack(side=LEFT)
    """    
if __name__=='__main__':
    HelloContainer().mainloop()
   """ 
class HelloExtender(Hello):
    def make_widget(self):
        Hello.make_widget(self)
        Button(self,text='Extend',command=self.quit).pack(side=RIGHT)
    
    def message(self):
        print('Hello',self.data)
if __name__=='__main__':
    HelloExtender().mainloop()        
