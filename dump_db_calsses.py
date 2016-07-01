# -*- coding: utf-8 -*-
"""
Created on Sat Jun 11 18:24:18 2016

@author: kai
"""

import shelve
db=shelve.open('class-shelve')
for key in db:
    print(key,'=>','\n',db[key].name,db[key].pay)

bob=db['bob']
print(bob.lastName())
print(db['tom'].lastName())
