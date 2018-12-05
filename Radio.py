#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct  2 15:33:53 2018

@author: juliana
"""
import math
from decimal import Decimal

class Radio(object):
    
    def __init__(self):
        self.power = 50
        self.in_fifo = list()
        self.out_fifo = list()
        self.gasto_tx = float(Decimal(50*math.pow(10, -9)) * 2000 + Decimal(100*math.pow(10, -12)) * self.power**2)
        self.gasto_rx = 0.0001
    
    def sendPacket(self, pkt):      # coloca pacote na out_fifo
        self.out_fifo.append(pkt)
        #gasto = float(Decimal(50*math.pow(10, -9)) * 2000 + Decimal(100*math.pow(10, -12)) * self.power**2)
        print("Nó", pkt.srcAddr, "enviou", pkt.payload)
        #return gasto
        
    
    def rcvPacket(self):   # tira pacote da in_fifo
        pkt = self.in_fifo.pop(0)
        #gasto = 0.0001 # float(Decimal(50*math.pow(10, -9)) * 2000)
        print("Nó", pkt.destAddr, "recebeu", pkt.payload)
        #return gasto
        
        
    def addPacket(self, pkt):   # coloca pacote na in_fifo
        self.in_fifo.append(pkt)
        
        
    def removePacket(self):     # tira pacote da out_fifo, retorna o destino
        pkt = self.out_fifo.pop(0)
        return pkt
        

