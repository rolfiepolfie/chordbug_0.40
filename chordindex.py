# -*- coding: utf-8 -*-
"""
Created on Tue Jul 25 10:59:33 2023

@author: rolfe
"""


class ChordIndex_simpler:
    
    def printAllChords(theObject):
        i=0
        for property, value in (vars(theObject).items()):
            if property.startswith('C'): 
                i=i+1
                print("{}\t {}  {}".format(i, property.ljust(15), value))
            
    C_major =           [0,4,7]
    C_minor =           [0,3,7]
    C_7_major    =      [0,4,7,10]
    C_7_minor =         [0,3,7,10]
    
    C_sus2=             [0,2,7]         #does C_sus2 add7 exist?
   
    C_maj_minor   =     [0,3,7,11]
    C_maj_major=        [0,4,7,11]      #Cmaj = C7 with sharpen7 (dominant7)
    
    C_major_add2=       [0,2,4,7]
    
    C_6_major=          [0,4,7,9]       
    C_6_minor   =       [0,3,7,9]
    
    C_aug=              [0,4,8]          #C+
    C_aug_add7=         [0,4,8,10]
    
    C_9_major=          [0,4,7,10,14]    #C7 add9   - the 9th imply 7th
    C_9_minor=          [0,3,7,10,14]    #sharpen the 7 to get an variation?
        
    C_dim=              [0,3,6]
    C_dim_add7=         [0,3,6,10]  #is really Cm7(b5)  
    C_dim_add6=         [0,3,6,11] # real name is Cdim7  (I think: flat7)

class ChordIndex_simple:
    
    def printAllChords(theObject):
        i=0
        for property, value in (vars(theObject).items()):
            if property.startswith('C'): 
                i=i+1
                print("{}\t {}  {}".format(i, property.ljust(15), value)) 
            
    C_major =           [0,4,7]
    C_minor =           [0,3,7]
    C_7_major    =      [0,4,7,10]
    C_7_minor =         [0,3,7,10]
    
    C_sus2=             [0,2,7]         #does C_sus2 add7 exist?
   
    C_maj_minor   =     [0,3,7,11]
    C_maj_major=        [0,4,7,11]      #C7 with sharpen7
    
    C_major_add2=       [0,2,4,7]
    C_major_add9=       [0,4,7,13]      #not  a real 9th chord , missing 7th

    
    C_6_major=          [0,4,7,9]        #same as C6
    C_6_minor   =       [0,3,7,9]
    
    C_aug=              [0,4,8]          #C+
    C_aug_add7=         [0,4,8,10]
    
    C_9_major=          [0,4,7,10,14]    #C7 add9   - the 9th imply 7th
    C_9_minor=          [0,3,7,10,14]
    C_9_maj_major=      [0,4,7,11,14]    #C9 sharpen7
    C_9_flat7_major=    [0,4,7,9,14]     #C6/9 , flat7 = 6
    C_9_flat7_minor=    [0,3,7,9,14]   
        
    C_dim=              [0,3,6]
    C_dim_add6=         [0,3,6,10] #is really Cdim7
    C_dim_add7=         [0,3,6,11] #is really Cm7(b5) 
    
    
class ChordIndex:
    """
    A collection of all chords possible that could be made use of ...
    """
    def printAllChords(theObject):
        i=0
        for property, value in (vars(theObject).items()):
            if property.startswith('C'): 
                i=i+1
                print("{}\t {}  {}".format(i, property.ljust(15), value))
            
    # 7th = index 10
    # maj = index 11     maj = sharpen7
    # 9th = index 13
    # 11th = index 16
    # 13th = index 20
    #https://www.pianochord.org/

    ### why not self.C_major ... in a in __init___?

    C_major =           [0,4,7]
    C_7_major    =      [0,4,7,10]
    C_7_minor =         [0,3,7,10]
    C_7_flat5   =       [0,4,6,10]   #does Cminor_flat5 exist? = yes: Cdim ,, Cmajor flat5?
    C_7_addsharp9 =     [0,4,7,10,15]
    
    C_maj_minor   =     [0,3,7,11]
    C_maj_major=        [0,4,7,11]   #C7 with sharpen7
    
    C_major_add2=       [0,2,4,7]
    C_major_add9=       [0,4,7,13]  #not  a real 9th chord , missing 7th
    
    C_6_major=          [0,4,7,9]    #same as C6
    C_6_minor   =       [0,3,7,9]
    C_6_add9_major=     [0,4,7,9,14]     #C6/9 , flat7 = 6
    C_6_add9_minor=     [0,3,7,9,14] 
    
    C_minor =           [0,3,7]

    C_aug=              [0,4,8]           #C+
    C_aug_add7=         [0,4,8,10] #Caug_minor exist?
        
    #The note for 9th chord is always the same , not sharpen nor flatten
    C_9_major=          [0,4,7,10,14]    #C7 add9   - the 9th imply 7th
    C_9_minor=          [0,3,7,10,14]
    C_9_maj_major=      [0,4,7,11,14]    #C9 sharpen7
   
    C_9_flat7_minor=    [0,3,7,9,14]   

    C_sus2=             [0,2,7]          #does C_sus2 add7 exist?
    C_sus4=             [0,5,7]
    C_sus2_add9=        [0,2,7,10,14]
    C_sus2_add7=        [0,2,7,10] 
    C_sus4_add9=        [0,5,7,10,14]
    C_sus4_add7=        [0,5,7,10] 
    
    #sus chords can be added with 7 and 9 or only7?
    
    C_dim=              [0,3,6]
    C_dim_add6=         [0,3,6,10] #is really Cdim7
    C_dim_add7=         [0,3,6,11] #is really Cm7(b5) 
    
    C_11_major=         [0,4,7,10,14,17]  
    C_11_minor=         [0,3,7,10,14,17]  
    
    C_13_major=         [0,4,7,10,14,17,21]  #same as: C7 in addition to D_minor
    C_13_minor=         [0,3,7,10,14,17,21]
    C_13_maj=           [0,4,7,11,14,17,21]  # sharp7 
    
    #C13 with a 7th = dominant 13 
    # ---


#1.control: convert minor
#2.control: add7
#3.control: sharpen the 7th
#4.control: add 2