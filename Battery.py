#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 23 10:09:35 2018

@author: juliana
"""

class Battery(object):
    
    def __init__(self, ini_level=0.5, total_level=10):
        self.ini_level = ini_level
        self.curr_level = ini_level
        self.total_level = total_level
        
        
    def incrLevel(self, n_id, x):
        self.curr_level += x
        
        
    def decrLevel(self, n_id, x):
        self.curr_level -= x
        
        
    
        