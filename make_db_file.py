# -*- coding: utf-8 -*-
"""
Created on Thu Jun 09 09:24:51 2016

@author: kai
"""

dbfilename='people-file'
ENDDB='enddb'
ENDREC='endrec'
RECSEP='=>'

def storeDbase(db,dbfilename=dbfilename):
    dbfile=open(dbfilename,'w')
    for key in db:
        dbfile.write(key + '\n')
        for (name,value) in db[key].items():
            dbfile.write(name + RECSEP + repr(value)+'\n')
        dbfile.write(ENDREC+ '\n')
    dbfile.write(ENDDB+ '\n')
    dbfile.close()

def loadDbase(dbfilename=dbfilename):
    dbfile=open(dbfilename)#文件对象
    import sys
    sys.stdin=dbfile#重定向I/O流
    db={}
    key=input()
    while key!=ENDDB:
        rec={}
        field=input()
        while field != ENDREC:
            name,value=field.split(RECSEP)
            rec[name]=eval(value)
            field=input()
        db[key]= rec
        key=input()
    return db

if __name__=='__main__':
    from initdata import db
    storeDbase(db)
    loadDbase('people-file')