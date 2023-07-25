# -*- coding: utf-8 -*-
"""
Created on Tue Jul 18 11:27:42 2023

@author: rolfe
"""

class SetupBlacstarController():
    '''
    This controller got 6 knobs ...
    last time used set to ch:16
    
    06.07.23 - the unit was programmed:
    All note_on/off +  sysex data=(0,0,116,1,0,77,67,1,0,70,1,0,6) 
    midi_trough = on , on channel 15 
    # notes are: 12, 14, 16, 17, 19, 21
    
    # 12-14-16-17-19-20(cc) -- 24/7
    
    # the two external inputs are only CC
    # values EXP2 = CC 20
    # EXP1 = CC 21
    
    Everything MIDI ch 16
        
    '''
    def __init__(self):
        
        pass
        
    
    def getControlArray1(self, Controls, Chords):
        #for control use
        
        chordMajor= Controls.sendChord([12], Chords.major)
        chordsus2= Controls.sendChord([99], Chords.sus4)
        chordMinor= Controls.sendChord([16], Chords.minor)
        chordMaj7= Controls.sendChord([17], Chords.maj7)
        
        #controlAdd7= Controls.add_seventh([14])
        controlConvMinor_CC=Controls.convertToMinorCC([20]) #listens to CC-messages 
        
        controlFreeze=Controls.freezeRoot([21]) #we're listening to note-messages by default       
        
        
        #chordDim = Controls.sendChord([19], Chords.dim) #new test chord as function
        
        c=[chordMajor, chordMinor, chordMaj7, controlFreeze, controlConvMinor_CC]
        
        return c
    
    
    #another way of setting up the device ....
    def getControlArray2(self, Controls, Chords):
        #for control use
        
        chordDim=Controls.sendChord([14], Chords.dim) #new test chord as function
        
        #c=[Controls.freezeRoot([12]), Controls.add_seventh([14]), Controls.convert_to_minor([16]), chordDim]
        c=[chordDim, Controls.freezeRoot([21])] #test
        return c
    
    
    # #def getControlArray_chordUse(self, Chords):
    #     '''
    #     Use this for setting up the device as a "chord input"
    #     we got 6+ chord qualities , can have another live logic 
    #     with the minor and add7 on the other 
    #     + make a function for importing several chord-templates 
        
    #     ### fcb chords - conclusion 17.01
    #     #### C_maj,   C_aug,  Cdim,   ,C6,      C9
    #     #### C_major, C_sus2, C_minor, C7_minor, C7    
    #     # in addition functions: root_freeze , add7,  convertMinor
        
    #     Chord template-1
    #     1-2-3-4-5-6
        
    #     1.major
    #     2.minor
    #     3.sus2
    #     4.septim_minor
    #     5.maj7
    #     6.dim
    #     ##### 7.6'th - not much used , make alternative template ?
        
        
    #     live-logic nr2
    #     -------------------------------------------------------------------
        
    #     Control
    #     1-2-3-4-5-6
    #     maybe sustain on nr1? 
    #     1. root_on/off
    #     2. minor_convert
    #     3. add7
    #     4. add7_sharp
    #     5. extra control 1
    #     6. extra control 2
        
    #     -------------------------------------------------------------------
        
    #     app name: Live Logic Midi control 
    #     notes are: 12, 14, 16, 17, 19, 21 - pr06.07.23
    #     '''
        
    #  "   chords=[Chords.major([12]), Chords.minor([14]),Chords.sus4([16]),
    #  "           Chords.minor7([17]), Chords.maj7([19]), Chords.dim([21])]
        
        
    #  "   return chords        
    

        
    
