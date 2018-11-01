#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 24 09:52:50 2018

@author: juliana
"""

class Consumo(object):
    
    def __init__(self):
        self.consumo = 0
        
        
    def consume(self, x):
        self.consumo += x
        
        
    def run(self, batt):
        batt.decrLevel(self.consumo)