# -*- coding: utf-8 -*-
"""
Created on Tue Jun 21 16:20:13 2016

@author: jifangzhuji
"""

import os 
from multiprocessing import Process
def runprogram(arg):
    os.execlp('python','python','child.py',str(arg))

if __name__=='__main__':
    for i in range(5):
        Process(target=runprogram,args=(i,)).start()
    print('parent exit')