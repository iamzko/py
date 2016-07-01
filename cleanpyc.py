# -*- coding: utf-8 -*-
"""
Created on Sat Jun 25 20:33:45 2016

@author: wei
"""

import os,sys
findonly= False
rootdir= os.getcwd() if len (sys.argv) ==1 else sys.argv[1]

found = removed=0
for (thisDirLevel,subsHere,filesHere) in os.walk(rootdir):
    for filename in filesHere:
        if filename.endswith('.pyc'):
            fullname= os.path.join(thisDirLevel,filename)
            print('===>',fullname)
            if not findonly:
                try:
                    os.remove(fullname)
                    removed+=1
                except:
                    type,inst = sys.exc_info()[:2]
            found +=1
print('Found ',found ,'files,removed',removed)

                        