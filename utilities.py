# -*- coding: utf-8 -*-
"""
Created on Tue Jul 25 11:04:21 2023

@author: rolfe
"""
from dataclasses import dataclass
import time

### small classes and datatypes 


class MidimsgType():  
    note_on = 'note_on'
    note_off = 'note_off' 
    controlchange = 'control_change'
    programchange = 'program_change'
    sysex_data = 'sysex_data'
    pitchwheel = 'pitchwheel'
    aftertouch = 'aftertouch'
    
class Actiontype:
    momentary = 'momentary' # or temporary, remove effect when pedal is up
    toggle = 'toggle'
    other = 'other'



class CCvalues:
    """
    defines values that follows a CC (Control Change) message (CC, value)
    """
    ALL_SOUND_OFF = 120 #check midi spec for this one 
    RESET_ALL_CONTROLLERS = 121
    ALL_NOTES_OFF = 123
   
    # 122 Local Control On/Off  -  interrupt the internal control path between the keyboard and the sound-generating circuitry
    # 123 All Notes Off
    # 124 Omni Mode Off
    # 125 Omni Mode On
    # 126 Poly Mode On/Off
    # 127 Poly Mode Mono Off

    #https://www.lim.di.unimi.it/IEEE/MIDI/SOT0.HTM#Local

class utils:
    def availableCC():
        s="""
        These is free to use Control Change Messages ...
        """
        print(s)
        print("CC 3")
        print("CC 9")
        print("CC 14-15")
        print("CC 20-31")
        print("CC 85-87")
        print("CC 89-90")
        print("CC 102-119")
    
    # def showkeyb():
    #     img = mpimg.imread('keyb.png')
    #     plt.imshow(img)
    #     plt.show()




class Misc():
    
    #change to live session report ...
    def functionalityreport(controls):
        """
        Prints all the chords and controls loaded in this session 
        
        """

        print("\n")
        print("--- CONTROLS registered for controller messages this session ---")
        for c in controls:     
        
            print("control name: \t", c.name)   
            print("\t\t triggered by: \t", c.msgtype)
            print("\t\t note_cc: \t\t", c.note_cc)
            print("\t\t action: \t\t", c.action)
            #print("\n")
        
        print("\n")
  
    
    def classname(self): return __class__.__name__
    
    #def isControlChange(msg):
    #    return msg.type == 'control_change'
    
    #def isNote(msg):
    #    return msg.type == 'note_on' or msg.type == 'note_off'
    #    #return msg.type in ('note_on', 'note_off') # alternative
    
    def undefined_CC():
        t1=" Undefined MIDI CC List"

        t2="CC 3 "
        t3="CC 9 "
        t4="CC 14-15 "
        t5="CC 20-31 "
        t6="CC 85-87 "
        t7="CC 89-90 "
        t8="CC 102-119 "
        return t1+t2+t3+t4+t5+t6+t7+t8
        
        
    def listClassMembers(theObject):
        
        for property, value in vars(theObject).items():
            print(property, ":", value)
    
    def printUserprotertiesClass(clas):
        print([ m for m in dir(clas) if not m.startswith('__')])
    
    def clearSpyderTerminal():
        print("\033[H\033[J")  
    

    def printTitle(mido, rt, sys, ver, title): # the app's name .... 
        print("")
        print("*********************************")
        
        #print(' ▄████▄   ██░ ██  ▒█████   ██▀███  ▓█████▄  ██▓ ▄▄▄       ██▓    ')
        #print('▒██▀ ▀█  ▓██░ ██▒▒██▒  ██▒▓██ ▒ ██▒▒██▀ ██▌▓██▒▒████▄    ▓██▒    ')
        #print('▒▓█    ▄ ▒██▀▀██░▒██░  ██▒▓██ ░▄█ ▒░██   █▌▒██▒▒██  ▀█▄  ▒██░    ')
        #print('▒▓▓▄ ▄██▒░▓█ ░██ ▒██   ██░▒██▀▀█▄  ░▓█▄   ▌░██░░██▄▄▄▄██ ▒██░    ')
        #print('▒ ▓███▀ ░░▓█▒░██▓░ ████▓▒░░██▓ ▒██▒░▒████▓ ░██░ ▓█   ▓██▒░██████▒')
        #print('░ ░▒ ▒  ░ ▒ ░░▒░▒░ ▒░▒░▒░ ░ ▒▓ ░▒▓░ ▒▒▓  ▒ ░▓   ▒▒   ▓▒█░░ ▒░▓  ░')
        #print('  ░  ▒    ▒ ░▒░ ░  ░ ▒ ▒░   ░▒ ░ ▒░ ░ ▒  ▒  ▒ ░  ▒   ▒▒ ░░ ░ ▒  ░')

     ### a testing function ... shall be removed and replaced with Chord-Service  
        print("Title: \t\t\t\t" , title)
        print("Python installed: \t", sys.version_info[0],',', sys.version_info[1])
        print("Mido version:   \t", mido.__version__)
        print("Backend version RT:\t", rt.__version__)
        print("Chordial version: \t", ver)
     
     
    def overviewChords():
        return """
                    https://www.pianochord.org/c5.html
            
            C - C major (C△)
            Cm - C minor
            C7 - C dominant seventh
            Cm7 - C minor seventh
            
            Cmaj7 - C major seventh (C△7)
            CmM7 - C minor major seventh
            
            C6 - C major sixth
            Cm6 - C minor sixth
            C6/9 - C sixth/ninth (sixth added ninth)
            
            C5 - C fifth   (interval - 2 notes)
            
            C9 - C dominant ninth
            Cm9 - C minor ninth
            Cmaj9 - C major ninth
            
            C11 - C eleventh
            Cm11 - C minor eleventh
            
            C13 - C thirteenth
            Cm13 - C minor thirteenth
            Cmaj13 - C major thirteenth
            
            Cadd - C add
            C7-5 - C seven minus five
            C7+5 - C seven plus five
            Csus - C suspended
            
            Cdim - C diminished (C°)
            Cdim7 - C diminished seventh (C°7)
            Cm7b5 - C minor seventh flat five (Cø)
            
            Caug - C augmented (C+)
            Caug7 - C augmented seventh
        """


#from sessionclass import SessionMain


class UserInteraction:
    
    def askuseropenports(rv, midi, filt, ports):
        
        
        print("open inport for bass: ")
        #if ans == 'y':
        ports.openInport_bass(rv.in_index_bass) 
        midi.setinPort_bass(ports._inPort_bass, ports._inPort_bass_name, filt.trigBass) 
        time.sleep(1)
        
                 
        ports.openInport_control(rv.in_index_control1) 
        midi.setinPort_controlButtons(ports._inPort_control, ports._inPort_control_name, filt.trigControlChord) 
        time.sleep(1)
        
        print("open inport for control2: ")
        
        if rv.in_index_control2 != -1: 
        
            ports.openInport_control(rv.in_index_control2) 
            midi.setinPort_controlButtons(ports._inPort_control, ports._inPort_control_name, filt.trigControlChord) 
        
        else:
            print("NB ** port not opened **")
                    
        
        time.sleep(1)


    def readportnumbers():
        
        @dataclass
        class Returnvalue:
            out_index:          int
            in_index_bass:      int
            in_index_control1:  int
            in_index_control2:  int
            
        while True: # read in a midi port device 
            try:
                print(" *********** -1 if this service is not wanted. ************* ")
                print(" - ")
                out_index = int(input("For chord output, enter a number (default 0): ") or "0")
                print('\n')
                
                in_index_bass = int(input("For bass input, enter a number(default 1): ") or "1") #1
                      
                in_index_control1 = int(input("For control input1, enter a number(default 0): ") or "0") #3
                in_index_control2 = int(input("For control input2, enter a number(default -1): ") or "-1") #0
                
                break
            
            except Exception as e:
                print("er, ror: " + str(e))
                
        return Returnvalue(out_index, in_index_bass, in_index_control1, in_index_control2)
          

  