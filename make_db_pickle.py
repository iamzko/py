# -*- coding: utf-8 -*-
"""
Created on Thu Jun 09 11:24:59 2016

@author: kai
"""

from initdata import db
import pickle
dbfile=open('people-pockle','wb')
pickle.dump(db,dbfile)
dbfile.close()


f=open('people-pockle','rb')
db=pickle.load(f)
for key in db:
    print(key,'=>',db[key])
f.close()
print(db['sue']['name'])
db['tom']['name']='Tom Tom'
db['bob']['pay']*=1.2
f=open('people-pockle','wb')
pickle.dump(db,f)
f.close()
