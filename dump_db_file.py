# -*- coding: utf-8 -*-
"""
Created on Thu Jun 09 09:50:08 2016

@author: kai
"""

from make_db_file import loadDbase
db=loadDbase('people-file')
for key in db:
    print(key,'=>\n  ',db[key])
print(db['sue']['name'])