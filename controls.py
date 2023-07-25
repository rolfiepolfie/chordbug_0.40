# -*- coding: utf-8 -*-
"""
Created on Tue Jul 25 11:12:01 2023

@author: rolfe
"""


from utilities import MidimsgType, Actiontype


import globalvars as glob

class Control:
    """
    Base class for all user defined controls
    """
    # def printall(Object): #move to the Control class ?
    #     i=0
    #     for property, value in (vars(Object).items()):
    #         #if not property.startswith('_'): 
    #         i=i+1
    #         print("{}\t {}  {}".format(i, property.ljust(15), value))
                
    
        
class Controls:
    __doc__="""
    If you want to print all Controls that is in the Classes
    A collection of controls with their function
    """
    #def printall(Object): super(Control, obj) 
    def printall(Object): 
        print("all possible controls that can be handled if  assigned to a midi message: ") 

        i=0
        for property, value in (vars(Object).items()):
            if not property.startswith('__'): 
                if not property.startswith('printall'): 
                    i=i+1
                    #print("{}\t {}  {}".format(i, property.ljust(15), value))
                    print("{}\t {}  ".format(i, property.ljust(15)))


    class freezeRoot(Control):
        def __init__(self, note_cc): #make constructor on all classes?
            if type(note_cc) != list: raise TypeError('__init__ parameter value must be a list []')

            """
            Freeze, means that the bass input do not change the root 
            of the cord
            These Controls classes got a optional constructor, but also have the 
            note_cc=value as a default value 
            """
            self.name = "FreezeRoot_control"
            self.msgtype=[MidimsgType.note_on, MidimsgType.note_off]
            self.note_cc=note_cc
            self.action=Actiontype.momentary
        
        def function(self, arg=None):

            global global_Control_disable_chord_root
            print("evoked: ", self.name)
                       
            Globals, msgtype, note_cc, mess, midi = arg
            
            if msgtype == MidimsgType.note_on:
                Globals.global_Control_disable_chord_root = True
                print("freeze-root  and note-on detected")
            
            if msgtype == MidimsgType.note_off:
                Globals.global_Control_disable_chord_root = False
                print("freeze-root  and note-off detected")
    
    class add_6th(Control):
        '''
        '''
        pass
    
            
    class add_seventh(Control):
        def __init__(self, note_cc): 
            if type(note_cc) != list: raise TypeError('__init__ parameter value must be a list []')
            
            self.name = "Add_7th_control"
            self.msgtype=[MidimsgType.note_on]
            self.note_cc=note_cc
            self.action=Actiontype.momentary
        
        def function(self, arg=None):
            """
            take current chord , return converted chord  
            """
            global Globals
            Globals, msgtype, note_cc, mess, midi=arg 
            print("add_seventh function evoked ...")
            #print(Globals.global_chord)

            # now add the 7th and put the chord back 
            
            
            # retrig the chord
            Globals.retrigChord() #not Globals().retrigChord()
            
            
    class convert_to_minor(Control):
        def __init__(self, note_cc): 
            if type(note_cc) != list: raise TypeError('__init__ parameter value must be a list []')
            self.note_cc=note_cc
            
            self.name = "Convert chord to minor"
            self.msgtype=[MidimsgType.note_on]
            self.note_cc=note_cc
            self.action=Actiontype.momentary
        
        def function(self, arg=None):
            """
            take current chord, return converted minor chord, re-play 
            """
            Globals, msgtype,note_cc,mess, midi=arg # "mess" got it "all" 
           
            print("evoked: ", self.name)
            #Globals.retrigChord(midi) # or do like in sendChord 
            #midi.playChord(glob.Globals.global_chord, glob.Globals.global_chord_root)
    
    
    class convertToMinorCC(Control): #for testing, we got an extra parameter for messagetype
        
        def __init__(self, note_cc): 
            if type(note_cc) != list: raise TypeError('__init__ parameter value must be a list []')
            self.note_cc=note_cc
            
            self.name = "Convert chord to minor - CC"
            self.msgtype=[MidimsgType.controlchange]
            self.note_cc=note_cc
            self.action=Actiontype.momentary
        
        def function(self, arg=None):
            """
            take current chord, return converted minor chord, re-play 
            """
            Globals, msgtype, note_cc, mess, midi=arg # "mess" got it "all" 
           
            print("evoked: ", self.name)
            #Globals.retrigChord(midi) # or do like in sendChord 
            #midi.playChord(glob.Globals.global_chord, glob.Globals.global_chord_root)
            # Here is how to use it:    Controls.sendChord(Chords.major([12]))
    
    
    
    class sendChord(Control): # <- fix this, a Chord class is to be used as param 
        '''
        This is an ordinary chord maskering as a function
        REMARK: this is takes Chord class object as param
        
        '''
        def __init__(self, note_cc, Chord): #make constructor on all classes?
            if type(note_cc) != list: raise TypeError('__init__ parameter value must be a list []')

 
            self.name = "Send Chord Control " + Chord.name
            self.msgtype=[MidimsgType.note_on, MidimsgType.note_off]
            self.note_cc=note_cc
            self.action=Actiontype.momentary   
            self.Chord=Chord        

            
        def function(self, arg=None):
            '''
            here we can use retrig in the global class
            '''
            Globals, msgtype,note_cc,mess, midi=arg  #midi is the midi layer and used for playing chords , m.m
            
            #global global_Control_disable_chord_root   #needed?
            
            print("evoked: ", self.name)
            
            glob.Globals.global_chord = self.Chord.index

            if msgtype == 'note_on':
                midi.playChord(glob.Globals.global_chord, glob.Globals.global_chord_root)

            
                
    class chordPage(Control):
        '''
        alternate between chordpages , one for each style , 
        '''
        pass               
                
                
                
#    class sequence(Chord):
#        '''
#        put some chords in an array, then loop trough them
#        sending chords out
#        '''
#        def loadChords(chordarray):
#            
#            '''
#            loadChords([c,f,g])
#            
#            also define a way to denote the delay between them  
#            '''
#            pass
#        
#        # needs to be syncromized with extrnal MIDI-clock
#        def runChordLoop():
#            pass
    
    
    
    
    #....
    #....
    #see earlier versions for ideas of functions that can be added 
            
