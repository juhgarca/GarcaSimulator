#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct  2 15:33:53 2018

@author: juliana
"""

class Radio(object):
    
    def __init__(self):
        self.in_fifo = list()
        self.out_fifo = list()
        
    
    def sendPacket(self, pkt):      # coloca pacote na out_fifo
        self.out_fifo.append(pkt)
        print(pkt.payload, "sent by node", pkt.srcAddr)
        
    
    def rcvPacket(self):   # tira pacote da in_fifo
        pkt = self.in_fifo.pop(0)
        print(pkt.payload, "rcvd by node", pkt.destAddr)
        
        
    def addPacket(self, pkt):   # coloca pacote na in_fifo
        self.in_fifo.append(pkt)
        
        
    def removePacket(self):     # tira pacote da out_fifo, retorna o destino
        pkt = self.out_fifo.pop(0)
        return pkt
        

