# -*- coding: utf-8 -*-
"""
Created on Sat Jun 25 21:00:45 2016

@author: wei
"""

import os,sys,find
count= 0
for filename in find.find('*.pyc',sys.argv[1]):
    count+=1
    print(filename)
    os.remove(filename)

print('Remove %d .pyc files '% count)