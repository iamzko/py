# -*- coding: utf-8 -*-
"""
Created on Mon Jun 13 10:15:09 2016

@author: jifangzhuji
"""

"""
分割字符串或者文本文件并交互地进行分页
"""

def more(text,numlines=15):
    lines= text.splitlines()
    while lines:
        chunk = lines[:numlines]
        lines = lines[numlines:]
        for line in chunk:
            print(line)
        if lines and input('More?') not in ['y','Y']:
            break
if __name__=='__main__':
    import sys
    more(sys.__doc__,10)
        