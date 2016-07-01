# -*- coding: utf-8 -*-
"""
Created on Wed Jun 22 12:23:56 2016

@author: jifangzhuji
"""

import os,glob,sys
dirname=r'c:\python34\Lib' if len(sys.argv) == 1 else sys.argv[1]

allsizes = []
allpy = glob.glob(dirname + os.sep + '*.py')
for filename in allpy:
    filesize = os.path.getsize(filename)
    allsizes.append((filesize,filename))
    
allsizes.sort()
print(allsizes[:2])
print(allsizes[-2:])