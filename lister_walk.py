# -*- coding: utf-8 -*-
"""
Created on Wed Jun 15 20:13:50 2016

@author: kai
"""

import os ,sys
def lister(root):
    for (thisdir,subshere,fileshere) in os.walk(root):
        print('['+thisdir+']')
        for fname in fileshere:
            path = os.path.join(thisdir,fname)
            print(path)
if __name__=='__main__':
    lister(sys.argv[1])