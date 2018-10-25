#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct  2 14:52:32 2018

@author: juliana
"""
import numpy as np
import config
from abc import ABCMeta, abstractmethod
from Radio import Radio
from Battery import Battery
from Packet import Packet

class Node(object, metaclass=ABCMeta):
    
    def __init__(self, _id, state='alive'):
        self._id = _id
        self.radio = Radio()
        self.state = state
        #self.bateria = Battery()
        self.pos_x = np.random.uniform(0, config.AREA_WIDTH)
        self.pos_y = np.random.uniform(0, config.AREA_LENGHT)
    
    @abstractmethod
    def run(self):
        pass
    

class NodeSimpleP2P(Node):
    
    def __init__(self, _id, state=''):
        super().__init__(_id, state)
		
        if self._id % 2 == 0:
            self.dest = self._id-1
        else:
            self.dest = self._id+1
            
        
    def run(self):
            
        if self.state == 'send':
            pkt = Packet(self._id, self.dest, 50)
            self.radio.sendPacket(pkt)
            self.state = 'wait'
        elif self.state == 'wait':
            if self.radio.in_fifo:
                self.radio.rcvPacket()
                self.state = 'send'
