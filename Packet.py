#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct  2 15:19:08 2018

@author: juliana
"""

class Packet(object):
    
    pkt_id = 0
    
    def __init__(self, srcAddr, destAddr = 0, tx_pwr):
        
        self.__class__.pkt_id += 1
        self.srcAddr = srcAddr
        self.destAddr = destAddr
        self.payload = 'Pacote ' + str(self.pkt_id)
        self.tx_pwr = tx_pwr
        
        # pensar numa função para tratar o envio em broadcast
        # essa funcção ficaria aqui ou na classe Node??
        
