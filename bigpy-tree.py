# -*- coding: utf-8 -*-
"""
Created on Wed Jun 22 12:50:33 2016

@author: jifangzhuji
"""

import sys,os,pprint
trace=False
if sys.platform.startswith('win'):
    dirname = r'c:\python34\Lib'
else:
    dirnaem= '/usr/lib/python'

allsize = []
for (thisDir,subsHere,filesHere) in os.walk(dirname):
    if trace:
        print(thisDir)
    for filename in filesHere:
        if filename.endswith('py'):
            if trace:
                print('...',filename)
            fullname = os.path.join(thisDir,filename)
            fullsize = os.path.getsize(fullname)
            allsize.append((fullsize,fullname))

allsize.sort()
pprint.pprint(allsize[:2])
pprint.pprint(allsize[-2:])