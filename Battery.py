#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 23 10:09:35 2018

@author: juliana
"""

class Battery(object):
    
    def __init__(self, level, total):
        self.level = level
        self.total = total
        
        
    def incrLevel(self, x):
        self.level += x
        
        
    def decrLevel(self, x):
        self.level -= x
        