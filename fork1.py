# -*- coding: utf-8 -*-
"""
Created on Thu Jun 16 10:48:48 2016

@author: jifangzhuji
"""

import os 

def child():
    print('Hello form child',os.getpid())
    os._exit(0)
    
def parent():
    while True:
        newpid = os.fork()
        if newpid == 0:
            child()
        else:
            print('Hello form parent',os.getpid(),newpid)
        if input() == 'q':
            break

parent()