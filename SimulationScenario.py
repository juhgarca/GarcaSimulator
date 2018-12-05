#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct  2 14:44:28 2018

@author: juliana
"""
from Node import NodeSimpleP2P as Node
from PhisicalMediumModel import PhisicalMediumModel
from EnergySourceModel import EnergySourceModel
import pandas as pd
import matplotlib.pyplot as plt
   
nodes = [Node(1), Node(2)]
phy = PhisicalMediumModel(nodes)
en_source = EnergySourceModel()
f = open('bateria.csv', 'w')
f.write("round id_node curr_load\r\n")
f.close()

for n in nodes:
    if n._id % 2 == 1:
        n.state = 'send'
    else:
        n.state = 'wait'
   
def runSimulation(nodes):
    
    print("Round: ", time)
            
    for n in nodes:
        en_source.run(n)
        n.run()
        phy.run(n)
        
        with open('bateria.csv', 'a') as f:
            f.write("{} {} {}\r\n".format(time, n._id, n.battery.curr_level))
    
time = 1
while time <= 10:
    
    runSimulation(nodes)
    
    time += 1
    
batt = pd.read_csv('bateria.csv', delimiter=' ')
x = list(range(1, 11))
y1 = batt[batt.id_node == 1]['curr_load']
y2 = batt[batt.id_node == 2]['curr_load']
plt.plot(x, y1)
plt.plot(x, y2)
plt.show()

