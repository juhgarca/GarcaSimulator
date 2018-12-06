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
    
    def sendPacket(self, pkt, r):      # coloca pacote na out_fifo
        pkt.t_tx = r
        self.out_fifo.append(pkt)
        #gasto = float(Decimal(50*math.pow(10, -9)) * 2000 + Decimal(100*math.pow(10, -12)) * self.power**2)
        print("Nó", pkt.srcAddr, "enviou", pkt.payload, "no tempo", pkt.t_tx)
        #return gasto
        
    
    def rcvPacket(self, r):   # tira pacote da in_fifo
        pkt = self.in_fifo.pop(0)
        pkt.t_rx = r
        #gasto = 0.0001 # float(Decimal(50*math.pow(10, -9)) * 2000)
        print("Nó", pkt.destAddr, "recebeu", pkt.payload, "no tempo", pkt.t_rx)
        with open('log.csv', 'a') as f:
            f.write("{} {} {}\r\n".format(pkt.pkt_id, pkt.srcAddr, pkt.t_tx, pkt.destAddr, pkt.t_rx))
        #return gasto
        
        
    def addPacket(self, pkt):   # coloca pacote na in_fifo
        self.in_fifo.append(pkt)
        
        
    def removePacket(self):     # tira pacote da out_fifo, retorna o destino
        pkt = self.out_fifo.pop(0)
        return pkt
        

