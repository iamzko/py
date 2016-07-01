# -*- coding: utf-8 -*-
"""
Created on Wed Jun 29 15:56:40 2016

@author: jifangzhuji
"""

from tkinter.filedialog import askopenfilename
from tkinter.colorchooser import askcolor
from tkinter.messagebox import askquestion,showerror
from tkinter.simpledialog import askfloat

demos={
       'Open':askopenfilename,
       'Color':askcolor,
       'Query':lambda:askquestion('Warning','you typed "rm *"\nConfirm?'),
       'Input':lambda:askfloat('Entry','Enter credit card number')
       }