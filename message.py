# -*- coding: utf-8 -*-
"""
Created on Thu Jun 30 09:39:08 2016

@author: jifangzhuji
"""

from tkinter import *
"""
msg= Message(text='Oh by the way,which one"s Pink?')
msg.config(bg='pink',font=('times',16,'italic'))
msg.pack(fill=X,expand=YES)
mainloop()
"""
from quitter import Quitter
def fetch():
    print('Input => "%s"' % ent.get())

root=Tk()
ent=Entry(root)
ent.insert(0,'')
ent.config(show='*')
ent.pack(side=TOP,fill=X)

ent.focus()
ent.bind('<Return>',(lambda event:fetch()))
btn= Button(root,text='Fetch',command=fetch)
btn.pack(side=LEFT)
Quitter(root).pack(side=RIGHT)
root.mainloop()
