#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct  2 14:44:28 2018

@author: juliana
"""
from Node import NodeSimpleP2P as Node
from PhisicalMediumModel import PhisicalMediumModel
from EnergySourceModel import EnergySourceModel
   
nodes = [Node(1), Node(2)]
phy = PhisicalMediumModel(nodes)
en_source = EnergySourceModel()

for n in nodes:
    if n._id % 2 == 1:
        n.state = 'send'
    else:
        n.state = 'wait'
   
def runSimulation(nodes):
            
    for n in nodes:
        en_source.run(n)
        n.run()
        phy.run(n)
    
times = 0 
while times < 3:
    
    runSimulation(nodes)
    
    times += 1