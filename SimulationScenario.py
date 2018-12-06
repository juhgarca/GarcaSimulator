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


# =============================================================================
# nodes = []
# num_nodes = 10
# for n in list(range(1,num_nodes+1)):
#     nodes.append(Node(n))
# =============================================================================
nodes = [Node(1), Node(2)]
phy = PhisicalMediumModel(nodes)
en_source = EnergySourceModel()
f = open('bateria.csv', 'w')
f.write("round id_node curr_load\r\n")
f.close()
f = open('log.csv', 'w')
f.write("pkt_id src t_tx dest t_rx\r\n")
f.close()

for n in nodes:
    if n._id % 2 == 1:
        n.state = 'send'
    else:
        n.state = 'wait'
   
def runSimulation(nodes):
    
    #print("Round: ", r)
            
    for n in nodes:
        en_source.run(n)
        n.run(r)
        phy.run(n)
        
        with open('bateria.csv', 'a') as f:
            f.write("{} {} {}\r\n".format(r, n._id, n.battery.curr_level))
    
r = 1
while r <= 8:
    
    runSimulation(nodes)
    
    r += 1
    
# =============================================================================
# batt = pd.read_csv('bateria.csv', delimiter=' ')
# x = list(range(1, 11))
# y1 = batt[batt.id_node == 1]['curr_load']
# y2 = batt[batt.id_node == 2]['curr_load']
# plt.plot(x, y1)
# plt.plot(x, y2)
# plt.show()
# =============================================================================

