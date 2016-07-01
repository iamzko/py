# -*- coding: utf-8 -*-
"""
Created on Mon Jun 20 17:07:54 2016

@author: jifangzhuji
"""

import os 
from multiprocessing import Process, Lock
def whoami(label,lock):
    msg= ' %s:name:%s,pid:%s'
    with lock:
        print(msg%(label,__name__,os.getpid()))

if __name__=='__main__':
    lock =Lock()
    whoami('function call',lock)
    
    p=Process(target=whoami,args=('spqured child',lock))
    p.start()
    p.join
    
    for i in range(5):
        Process(target=whoami,args=(('run process %s'%i),lock)).start()
    
    with lock:
        print('Main process exit.')
    