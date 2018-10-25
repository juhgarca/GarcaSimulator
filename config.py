# -*- coding: utf-8 -*-
'''
Definição das configurações dos nós, rede e simulação
'''

#Definição da área
AREA_LENGHT = 50
AREA_WIDTH = 50

#Número de nós
NB_NODE = 101

# Energia dissipada pelo transceiver
E_ELEC = 50e-9	#Joules/bit

# Energia dissipada pelo amplificador de potência
E_AMP = 10e-12

# Energia dissipada na agregação de dados
#	informação tirada do simulador de wsn
E_AGG = 5e-9	#Joules/bit

# Tamanho do pacote transmitido
K = 2000	#bit
