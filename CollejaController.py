#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 11 18:58:33 2017

@author: victor
"""

import os


class collejaController:
    
    PATH='counter/counter.bin'
    PATH_DIR='counter'
    num=0
    
    def __init__(self):
        if not os.path.exists(self.PATH_DIR):
            os.mkdir(self.PATH_DIR)
            self.write_Counter(self.num)
            
    
    def read_Counter(self):
        num=0
        with open(self.PATH,'r') as f:
            num=f.read()
        return int(num)
    
    def write_Counter(self,data):
        os.remove(self.PATH)
        with open(self.PATH,'w') as f:
            f.write(str(data))
            
pass

