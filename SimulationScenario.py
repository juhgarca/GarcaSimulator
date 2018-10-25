#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct  2 14:44:28 2018

@author: juliana
"""
from Node import NodeSimpleP2P as Node
from PhisicalMediumModel import PhisicalMediumModel
   
nodes = [Node(1), Node(2)]
phy = PhisicalMediumModel(nodes)

for n in nodes:
    if n._id % 2 == 1:
        n.state = 'send'
    else:
        n.state = 'wait'
   
def runSimulation():
            
    for n in nodes:
        n.run()
        phy.run(n)
    
times = 0 
while times < 4:
    
    runSimulation()
    
    times += 1