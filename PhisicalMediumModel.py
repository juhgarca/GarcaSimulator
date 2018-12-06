#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct  2 15:01:03 2018

@author: juliana
"""

class PhisicalMediumModel(object):
    
    def __init__(self, nodes):
        self.nodes = nodes
        
        with open('coordinates.txt', 'w') as f:
            for n in nodes:
                f.write("{} {} {}\r\n".format(n._id, n.pos_x, n.pos_y))
    
    def run(self, n):
        
        if n.radio.in_fifo:
            n.radio.out_fifo.append(n.radio.in_fifo[0])
            n.radio.in_fifo.pop(0)
            
        if n.radio.out_fifo:
            pacote = n.radio.removePacket()
            dest = pacote.destAddr
            self.nodes[dest-1].radio.addPacket(pacote)
        

            
