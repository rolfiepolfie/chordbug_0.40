# -*- coding: utf-8 -*-
"""
Created on Tue Jul 25 10:55:44 2023

@author: rolfe
"""
# rename chordindex -> chordindexes
from chordindex import ChordIndex 
from utilities import MidimsgType, Actiontype


class Chord:  # all chords are instance of this class , isinstance....() 
    """
    Base class for all user defined chords
    
    IN USE 
    
    """
    def classname(): return "Chord"
    
class Chords:
    """
    If you want to print all CHORDS that is in the Classes

       msgtype and note..cc are all lists
       Class structure of chord indexes and its names 
       ChordId.dim.index = [0, 3, 6, 9] \n
       ChordId.dim.name = 'Dim'
       
    """
    def printall(Object):
        print("\n -- chords class structure, chords that can be invoked if  assigned to a midi message: ") 
        i=0
        for property, value in (vars(Object).items()):
            if not property.startswith('__'): 
                if not property.startswith('printall'): 
                    i=i+1
                    print("{}\t {} ".format(i, property.ljust(15)))
                    
        print('\n')
    

    #we need some self.... in the members             
    class major(Chord):
        """
        Comments goes here
        """
        def __init__(self, note_cc): 
            if type(note_cc) != list: raise TypeError('__init__ parameter value must be a list []')
            self.note_cc=note_cc
        index = ChordIndex.C_major
        name= Chord.classname() + " - Major"
        msgtype=[MidimsgType.note_on]
        note_cc=[60] #default value if constructor not used
        action=Actiontype.momentary
           
    class sus4(Chord):
        def __init__(self, note_cc): 
            if type(note_cc) != list: raise TypeError('__init__ parameter value must be a list []')
            self.note_cc=note_cc
        index= ChordIndex.C_sus4
        name= Chord.classname() + " - Sus2" 
        msgtype=[MidimsgType.note_on]
        note_cc=[61]   #<-delete these default values for all chords ...
        action=Actiontype.momentary
        alternations =["sus4", "add7", "add9"] # new idea to help algorithm def function(self, arg=None): pass

        
        def function(self, arg=None): pass
    
    class minor(Chord):
        def __init__(self, note_cc): 
            if type(note_cc) != list: raise TypeError('__init__ parameter value must be a list []')
            self.note_cc=note_cc
        index = ChordIndex.C_minor
        name = Chord.classname() + " - Minor"
        msgtype=[MidimsgType.note_on]
        note_cc=[62]
        action=Actiontype.momentary
        def function(self, arg=None): pass
        
    class normal_7th(Chord):  #not the maj7 or sharped 7
        def __init__(self, note_cc): #make constructor on all classes?
            if type(note_cc) != list: raise TypeError('__init__ parameter value must be a list []')
            self.note_cc=note_cc
        index = ChordIndex.C_7_major
        name= Chord.classname() + " - 7th-septim"
        msgtype=[MidimsgType.note_on]
        note_cc=[63]
        action=Actiontype.momentary
        def function(self, arg=None): pass
    
    
    class normal_6th(Chord):  #not the maj7 or sharped 7
        def __init__(self, note_cc): #make constructor on all classes?
            if type(note_cc) != list: raise TypeError('__init__ parameter value must be a list []')
            self.note_cc=note_cc
        index = ChordIndex.C_6_major
        name= Chord.classname() + " - 6th"
        msgtype=[MidimsgType.note_on]
        note_cc=[70]
        action=Actiontype.momentary
        def function(self, arg=None): pass
    
    
    class maj7(Chord): #sharpen 7th
        def __init__(self, note_cc): #make constructor on all classes?
            if type(note_cc) != list: raise TypeError('__init__ parameter value must be a list []')
            self.note_cc=note_cc
        index=ChordIndex.C_maj_major
        name=Chord.classname() + " - maj7-sharpen7th"
        msgtype=[MidimsgType.note_on]
        note_cc=[64]
        action=Actiontype.momentary
        def function(self, arg=None): pass
        
    class minor7(Chord):
        def __init__(self, note_cc): #make constructor on all classes?
            if type(note_cc) != list: raise TypeError('__init__ parameter value must be a list []')
            self.note_cc=note_cc
        index=ChordIndex.C_7_minor
        name=Chord.classname() + " - Minor7"
        msgtype=[MidimsgType.note_on]
        note_cc=[65]
        action=Actiontype.momentary
        def function(self, arg=None): pass
        
        
    class dim(Chord):  
        def __init__(self, note_cc): #make constructor on all classes?
            if type(note_cc) != list: raise TypeError('__init__ parameter value must be a list []')
            self.note_cc=note_cc
            
        index = ChordIndex.C_dim #lacking a 9 at the end , self.index
        name= Chord.classname() + " - Dim"   #self.name ? 
        msgtype=[MidimsgType.note_on]       #self.msgtype ? ....etc ...
        note_cc=[66]
        action=Actiontype.momentary
        def function(self, arg=None): pass
        
        
    class aug(Chord):
        def __init__(self, note_cc): #make constructor on all classes?
            if type(note_cc) != list: raise TypeError('__init__ parameter value must be a list []')
            self.note_cc=note_cc
        index= ChordIndex.C_aug
        name = Chord.classname() + " - augmented"
        msgtype=[MidimsgType.note_on]
        note_cc=[67]
        action=Actiontype.momentary
        def function(self, arg=None): pass
        
        
    class nine9(Chord):
        def __init__(self, note_cc): #make constructor on all classes?
            if type(note_cc) != list: raise TypeError('__init__ parameter value must be a list []')
            self.note_cc=note_cc
        index = ChordIndex.C_9_major
        name= Chord.classname() + " - 9th"
        msgtype=[MidimsgType.note_on]
        note_cc=[69]
        action=Actiontype.momentary
        def function(self, arg=None): pass
        
    class major11(Chord):
        def __init__(self, note_cc): #make constructor on all classes?
            if type(note_cc) != list: raise TypeError('__init__ parameter value must be a list []')
            self.note_cc=note_cc
        index= ChordIndex.C_11_major
        name = Chord.classname() + " - 11th"
        msgtype=[MidimsgType.note_on]
        note_cc=[70]
        action=Actiontype.momentary
        def function(self, arg=None): pass
        
    ## sus 2 + 7 = 9th chord
    
    # def invertChordLeft(self, chordId):
    #     it=deque(self, chordId)
    #     it.rotate(1)    
    #     return(list(it)) 
      
    # def invertChordRight(chordId):
    #     it=deque(chordId)
    #     it.rotate(-1)    
    #     return(list(it))         