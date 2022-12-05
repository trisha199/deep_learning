# -*- coding: utf-8 -*-
"""
Created on Mon Sep 19 21:10:41 2022

@author: shahabhi
"""
#%%
import numpy as np

class LogicGate:
    def __init__(self):
        pass
    
    def do_and(self,x1,x2):
        x = np.array([x1, x2])
        w = np.array([0.5, 0.5])
        b = -0.7

        y = np.sum(x*w)+ b
        
        return 1 if y > 0 else 0
    
    def do_nand(self, x1, x2):
        return 1 if self.do_and(x1,x2) == 0 else 0
    
    def do_or(self,x1,x2):
        x = np.array([x1, x2])
        w = np.array([0.5, 0.5])
        b = -0.2

        y = np.sum(x*w)+ b
        
        return 1 if y > 0 else 0
    
    def do_nor(self,x1,x2):
        return 1 if self.do_or(x1,x2) == 0 else 0
#Combing 2 logic gates
 
    def do_xor(self,x1,x2):
        y1 = self.do_or(x1,x2)
        y2 = self.do_nand(x1, x2)
        y = self.do_and(y1, y2)
        
        return y
    
#%%
if __name__ == '__main__':
    gate = LogicGate()
    
