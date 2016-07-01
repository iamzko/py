# -*- coding: utf-8 -*-
"""
Created on Tue Jun 28 16:13:13 2016

@author: jifangzhuji
"""
"""
from tkinter import *
import sys
widget=Button(None,text='Hello widget world!',command=sys.exit)
widget.pack()
widget.mainloop()
"""

"""
from tkinter import *
root=Tk()
Button(root,text='press',command=root.quit).pack(side=LEFT,expand=YES,fill=BOTH)
root.mainloop()
"""
"""
from tkinter import *
import sys

def quit():
    print('Hello , I must be going...')
    sys.exit()

widget=Button(None,text='Hell event world!',command=quit)
widget.pack()
widget.mainloop()
"""
"""
import sys
from tkinter import *
widget = Button(
                 None,
                 text='Hello event world',
                 command=(lambda:print('Hello lambda world ') or sys.exit()))
widget.pack()
widget.mainloop()
"""
"""
import sys
from tkinter import *

class HelloClass:
    def __init__(self):
        widget= Button(None,text='Hello event world',command=self.quit)
        widget.pack()
    
    def quit(self):
        print('Hello class method world')
        sys.exit()

HelloClass()
mainloop()
"""
"""
import sys
from tkinter import *
class HelloCallable:
    def __init__(self):
        self.msg='Hello  __call__ world!'
        
    def __call__(self):
        print(self.msg)
        sys.exit()

widget= Button(None,text='Hell event world.',command=HelloCallable())
widget.pack()
widget.mainloop()
"""
"""
#use bind() 
import sys
from tkinter import *
def hello(event):
    print('Press twice to exit.')
    
def quit(event):
    print('Hello ,I must be going...')
    sys.exit()

widget=Button(None,text='Hello event world')
widget.pack()
widget.bind('<Button-1>',hello)
widget.bind('<Double-1>',quit)
widget.mainloop()
"""
"""
from tkinter import *
def greetint():
    print('Hello stdout world!')
    
win = Frame()
win.pack(side=TOP,expand=YES,fill=BOTH)
Button(win,text='Hello',command=greetint).pack(side=LEFT,anchor=N)
Button(win,text='Quit',command=win.quit).pack(side=RIGHT)
Label(win,text='Hello container world').pack(side=TOP)


win.mainloop()
"""

from tkinter import *
class HelloButton(Button):
    def __init__(self,parent=None,**config):
        Button.__init__(self,parent,**config)
        self.pack()
        self.config(command=self.callback)
        
    def callback(self):
        print('Goodbye world...')
        self.quit()

class MyButton(HelloButton):
    def callback(self):
        print('Ignoring press!')
    
if __name__=='__main__':
    MyButton(None,text='Hello subclass world').mainloop()
"""
class ThemedButton(Button):
    def __init__(self,parent=None,**config):
        Button.__init__(self,parent,**config)
        self.pack()
        self.config(fg='red',bg='black',font=('courier',12),relief=RAISED,bd=5)
        
B1=ThemedButton(text='spam',command=onSpam)
B2=ThemedButton(text='eggs')
B2.pack(expand=YES,fill=BOTH)
"""
