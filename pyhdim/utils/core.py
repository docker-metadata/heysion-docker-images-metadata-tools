#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
@author: Heysion 
@copyright: 2019 By Heysion <heysions@gmail.com>
@license: GPL v3.0
'''

def Fakee(name,notnull=True):
    fake_key = "_%s"%name
    
    @property
    def faker(self):
        return getattr(self,fake_key,None)

    @faker.setter
    def faker(self,value):
        if value or not notnull:
            setattr(self,fake_key,value)
        else:
            self.msg = "please set %s !"%name
            self.state = False
            logging.debug(self.msg)
            raise self
    return faker

class HEx(Exception):
    def __init__(self,msg):
        super(HEx,self).__init__()
        self._msg = msg
        self._state = False

    @property
    def msg(self):
        return self._msg

    @msg.setter
    def msg(self,value):
        self._msg = value

    @property
    def state(self):
        return self._state

    @state.setter
    def state(self,value):
        self._state = value

# class Branch(object):
#     name = Fakee("name")
#     tag = Fakee("tag")
#     commit = Fakee("commit")

class Base(HEx):
    pass


