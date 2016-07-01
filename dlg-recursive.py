# -*- coding: utf-8 -*-
"""
Created on Wed Jun 29 20:59:40 2016

@author: kai
"""

from tkinter import *
def dialog():
    win=Toplevel()
    Label(win,text='Hard drive reformatted!').pack()
    Button(win,text='ok',command=win.quit).pack()
    win.protocol('WM_DELETE_WINDOW',win.quit)
    
    win.focus_set()
    win.grab_set()
    win.mainloop()
    win.destroy()
    print('dialog exit')
    f=open('dialog.txt','a')
    f.write('yooooo\n')
    f.close()
    
root =Tk()
Button(root,text='POPUP',command=dialog).pack()
root.mainloop()