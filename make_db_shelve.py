# -*- coding: utf-8 -*-
"""
Created on Thu Jun 09 11:52:00 2016

@author: kai
"""

from initdata import bob,sue
import shelve
db=shelve.open('people-shelve')
db['bob']= bob
db['sue']= sue
db.close()

db=shelve.open('people-shelve')
for key in db:
    print(key,'=>\n',db[key])
print (db['sue']['name'])
db.close()
