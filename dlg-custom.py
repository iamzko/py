# -*- coding: utf-8 -*-
"""
Created on Wed Jun 29 20:36:46 2016

@author: kai
"""

import sys
from tkinter import *
makemodal=(len(sys.argv)>1)
def dialog():
    win=Toplevel()
    Label(win,text='Hard drive reformatted').pack()
    Button(win,text='ok',command=win.destroy).pack()
    if makemodal:
        win.focus_set()
        win.grab_set()
        win.wait_window()
    print('dialog exit')

root=Tk()
Button(root , text='popup',command=dialog).pack(padx=100,pady=100,expand=YES)
root.mainloop()
