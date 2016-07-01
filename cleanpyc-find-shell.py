# -*- coding: utf-8 -*-
"""
Created on Sat Jun 25 20:47:54 2016

@author: wei
"""

import os,sys

rundir = sys.argv[1]
if sys.platform[:3] == 'win':
    findcmd = r'c:\cygwin\bin\find %s -name "*.pyc"  -print' %rundir
else:
    findcmd= 'find %s  -name "*.pyc"   -print' %rundir
print(findcmd)

count= 0
for fileline in os.popen(findcmd):
    count+=1
    print(fileline,end='')
    os.remove(fileline.rstrip())
print('Removed %d .pyc files'%count)
