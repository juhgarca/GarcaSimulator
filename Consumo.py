#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 24 09:52:50 2018

@author: juliana
"""
from abc import ABCMeta, abstractmethod
import config

class Consumo(object, metaclass=ABCMeta):
    
    def __init__(self):
        self.Eelec = config.E_ELEC
        self.Eamp = config.E_AMP
        self.K = config.K
        
    @abstractmethod
    def energySendMsg(self, d):
        pass
    
    @abstractmethod
    def energyRcvMsg(self):
        pass
    
    # Fazer função para o consumo da agregação de dados
