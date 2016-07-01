# -*- coding: utf-8 -*-
"""
Created on Sun Jun 12 16:27:43 2016

@author: jifangzhuji
"""

from tkinter import *
import random
fontsize=30
colors=['red','green','blue','yellow','orange','cyan','purple']
def onSpam():
    popup = Toplevel()
    color = random.choice(colors)
    Label(popup,text='Popup',bg='black',fg=color).pack(fill=BOTH)
    mainLabel.config(fg=color)
    
def onGrow():
    global fontsize
    fontsize +=5
    mainLabel.config(font=('arial',fontsize,'italic'))
    main.after(100,onGrow)

def onFlip():
    mainLabel.config(fg=random.choice(colors))
    main.after(250,onFlip)
    
main=Tk()
mainLabel = Label(main, text='Fun Girl!',relief=RAISED)
mainLabel.config(font=('arial',fontsize,'italic'),fg='cyan',bg='navy')
mainLabel.pack(side=TOP,expand=YES,fill=BOTH)
Button(main,text='spam',command=onSpam).pack(fill=X)
Button(main,text='flip',command=onFlip).pack(fill=X)
Button(main,text='grow',command=onGrow).pack(fill=X)
main.mainloop()