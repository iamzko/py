# -*- coding: utf-8 -*-
"""
Created on Sat Jun 11 17:31:51 2016

@author: kai
"""

from person import Person
class Manager(Person):
    def giveRaise(self,percent,bonus=0.1):
        self.pay*=(1.0+percent+bonus)
    def __str__(self):
        return '<%s=>%s>'%(self.__class__.__name__,self.name)
if __name__=='__main__':
    tom=Manager(name='Tom Doe',age=50,pay=50000)
    print(tom.lastName())
    tom.giveRaise(.20)
    print(tom.pay)
    print(tom)