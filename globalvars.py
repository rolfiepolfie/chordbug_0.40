# -*- coding: utf-8 -*-
"""
Created on Sat Jul 22 15:07:38 2023

@author: rolfe
"""

class Globals:
    '''
    This class contains variables utilized during a live session
    these are read before a live session and not supposed to be serialized
    '''    
    global_chord = [0,4,7]
    global_chord_root = 64    #bass note index
        
    global_bassdown = False #bass note is down/up = TRUE/FALSE
    
    controls = []   #being invoked during session
    
    
    global_Control_disable_chord_root = False # this is a control 
    
    
    

