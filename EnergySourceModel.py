#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov  1 15:54:22 2018

@author: juliana
"""

class EnergySourceModel(object):
    
    def __init__(self):
        self.load = 0.5     #Joules
        
        
    def run(self, node):
        node.battery.incrLevel(self.load)
    