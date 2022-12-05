# -*- coding: utf-8 -*-
"""
Created on Mon Sep 19 21:23:39 2022

@author: shahabhi
"""
# Calling upon the function from the Logicgate file
from logicgate import LogicGate

gate = LogicGate()

xs = [(0,0),(0,1),(1,0),(1,1)]

for x in xs:
    y = gate.do_xor(x[0],x[1])
    print("If you do_xor with {} and {}, you will have {}".format(x[0],x[1],y))

for x in xs:
    y = gate.do_and(x[0],x[1])
    print("If you do_and with {} and {}, you will have {}".format(x[0],x[1],y))
    
for x in xs:
    y = gate.do_or(x[0],x[1])
    print("If you do_or with {} and {}, you will have {}".format(x[0],x[1],y))

for x in xs:
    y = gate.do_nand(x[0],x[1])
    print("If you do_nand with {} and {}, you will have {}".format(x[0],x[1],y))

for x in xs:
    y = gate.do_nor(x[0],x[1])
    print("If you do_nor with {} and {}, you will have {}".format(x[0],x[1],y))