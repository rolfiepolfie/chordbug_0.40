# -*- coding: utf-8 -*- 


# when one class in each file ....
# example: from configparser import ConfigParser


import logging as logg
import config ##globals config variables for this app 


from chords import Chords
from midicom import MidiComm
from ports import Ports
from controls import Controls, Control
from midiMessage import Midimess

from filterMidi import Filter 

from setup import SetupBlacstarController
from sessionclass import SessionMain
from utilities import MidimsgType, Misc

from utilities import UserInteraction as ui # set this in a proper system

import rtmidi as rt
import sys
import mido

import globalvars as glob
import gmsounds as gm
#################################################################################################


def scan(msgtype, note_cc, Globals, msg, callback, extraparams=None): # -> Control:
    '''
    A helper function called by callbackChord_Control_Buttons(...)
    
    Scanning to se if a midi message match anything in the global lists: 
        chords = [] 
        controls = []
    If so, the _callback_scan() is invoked.
    msgtype: the type midi message cousing the triggering is a list [.....]
    note_cc: the midi note or CC (control change) causing the triggering
    callback: the function to be evoked if all parameters match 
    
    the returnvalue from this function is actually the return from _callback_scan(...)
    '''
    for control in Globals.controls:
        if msgtype in control.msgtype: 
            if note_cc in control.note_cc:
                return callback(control, msgtype, note_cc, msg) #returns class instance
 


def _callback_scan(classinstance, msgtype, note_cc, mess): #class instance , messagetype that triggered 
    '''    
    A helper function for the callback function
    The mess parameter contains all parameters
    This callback scans for Controls
    '''
        
    def iscontrol(instance): return isinstance(instance, Control)
    #def isAnothercontrol(instance): return isinstance(instance, AnotherControl)
        
    def activate_control(args, instance):
        instance.function(args) #every control got a function named 'function'
        
                
    if iscontrol(classinstance): 
        # I pack all sorts of parameters in here 
        # arguments to functions are decided here
        args=glob.Globals, msgtype, note_cc, mess, midi #is all needed? common parameters for all control.function(...)
        activate_control(args, classinstance)
        return classinstance # needed?
       
    #future versions
    #if isAnotertypeofControl(classinstance):
    #    pass
    
     
def callback_Control_Buttons(msg):
    '''
    check type of incoming midi-message
    scan for chords and controls giving the scan function the corect midi-messages
    
    the scan() function returns classinstance of the chord/control if needed
    the return of scan() is determined by the return value of _callback_scan()
    with other words: classinstance object
    '''
    mess=Midimess(msg)
    print(mess.totext())
    
    s="Nothing found ! - "
    
    if mess.isnoteOn():       
        r=scan(MidimsgType.note_on, msg.note , glob.Globals, mess, _callback_scan) #fill he globals       
        if r is None: print(s+mess.totext()) 
        return        
        
    if mess.isnoteOff():
        r=scan(MidimsgType.note_off, msg.note , glob.Globals, mess, _callback_scan) #fill he globals 
        if r is None: print(s+mess.totext())
        return
    
    if mess.isControlChange():
        r=scan(MidimsgType.controlchange, msg.control ,glob.Globals, mess, _callback_scan)
        if r is None: print(s+mess.totext())
        return
    
    #include more messages in later editions
    #if mess.isProgramChange(): pass

    
        
def callbackBass(msg):  #rename msg to midiOriginal    
    ''' 
    msg = original MIDI message, recall only original messages for the engine 
        set flag global_bassdown
    set root-note in global_chord_root
    send bass-note as midi-trough if requested 
    '''
    midimsg=Midimess(msg)
    
    logg.info("callbackBass")
    print('callbackBass2 - ', msg)
    
    
    def alterOutMidiChannel(newchannel):
        '''
        if you want alter the output midichannel only
        while retaining the other parameters  '''
        midi.sendMessageOut(msg.copy(channel=newchannel))
        
    if session._midiTrough:       
        midi.sendMessageOut(msg) #mimics the same as midi-through 
        #using midimsg did not work ..need original midi message!
        #alterOutMidiChannel(10)
    
    
    if midimsg.isnoteOn():    
        glob.Globals.global_bassdown=True
        
        if glob.Globals.global_Control_disable_chord_root == False: #control = freeze-root
           glob.Globals.global_chord_root=msg.note #we know it is a note at this stage
            
        print("global_chord_root note: ", glob.Globals.global_chord_root)
        return
        
    if midimsg.isnoteOff():
        glob.Globals.global_bassdown=False
        #print("Globals.global_bassdown=False")
        return
    

    
# -- global objects, later to be compiled into a session object     
session     = SessionMain()
midi        = MidiComm(mido, offset=config.__offset__, chordTimeLength=config.__chordTimeLength__) #offset = transpose 
ports       = Ports(mido)
filterMidi  = Filter(callbackBass, callback_Control_Buttons) 


class SetupHardware1:
    '''
    This is a PRESET setting up a collection of boxes 
    one blacstar + two pedals
    
    '''    
    def __init__(self):
        # here we decide what arrays tocadd to the Globals.controls array 
        # these arrays are controls that can also be a chord_send_control
        # we use the append command to add several controllers
        
        control1=SetupBlacstarController().getControlArray1(Controls, Chords)
        # for testing as we had another blackstar controller
        control2=SetupBlacstarController().getControlArray2(Controls, Chords) 
        #nb! do not use the same notes/cc if using the sme midi-channel    
        # here we put the control-array in series   
        self._controls = control1 + control2
        
        
    def connectToGlobals(self):
        glob.Globals.controls.extend(self._controls)
        #glob.Globals.controls.extend(control2) 'second control'
        
        #using extend or append? 
        # or control1 + control2 ?
    

def Configure():
    
    SetupHardware1().connectToGlobals()
    
    #midichannels [0...15] 
    session.midichannelBass=12
    session.MidiChannelControls=14
    session.MidiChannelOut=15    
    session._midiTrough=True
    
    #remark Misc = class object not instance
    Misc.functionalityreport(glob.Globals.controls) #report connection between controls - midi.numbers for this session
    
    ports.report_devices()   
    rv=ui.readportnumbers()  # reads port indexes from user
        
    ports.openOutPort(rv.out_index) #usually there is always an outport on a computer
    
    ui.askuseropenports(rv, midi, filterMidi, ports)
    
    
    # bass must +1 displayed to the user
    # 2,1,16 (in-bass, in-chords, in-controls, out-chords)
    # chords and controls will be merged to in-controls

    def setupFilter(session, filterMidi) -> None:
        
        filterMidi.midichannelBass = session.midichannelBass
        filterMidi.MidiChannelControls = session.MidiChannelControls
        filterMidi.MidiChannelOut = session.MidiChannelOut
        
        filterMidi.deactivate()  # <- remember to activate Filter 


    def setupMidi(midi, ports, session) -> None:
        
        midi.setOutPort(ports._outPort)       
        midi.setAllMidiChannels(session)  
        midi.sendProgamChange(gm.GmSounds.Celesta)
        midi.sendOutVolume(120)
        midi.testOut()
        midi.sendOutVolume(0)
        midi.testOut() 
       
            
    setupFilter(session, filterMidi)
    setupMidi(midi, ports, session)
    
    session.report()
    midi.report()
    filterMidi.report()
    ports.report()  
    
    
    
def _destruct():
    '''
    This will work as the destructor in the later Session Class 
    '''    
    if midi.InportsEmty()== False:
        print('* sending all notes off')
        midi.sendAllNotesOff()

        print('* closing all ports')
        ports.closeAllPorts() 
        
    ports.report()
    print('* program ended - bye')
    Misc.printTitle(mido, rt, sys, config.___version___, config.___title___)
    raise SystemExit(0) #clean way to exit , no traceback


# new idea: make a function: change chord function codepage
# exp: a device get a new selection of chords 2 -3 of them should be enough

# use logging instead of print 

# make each class have their own file 
# small classes collected in utility file 


def main()-> None:
    #logg.basicConfig(level=logg.INFO)
    
    #https://www.pylenin.com/blogs/python-logging-guide/
    logg.basicConfig(stream=sys.stdout, level=logg.INFO)
    # logg.debug('debug')
    logg.info("info message 123")
    # logg.warning('warning')
    # logg.error('error')
    
    
    Misc.printTitle(mido, rt, sys, config.___version___, config.___title___)
    Configure() 
    print(" \n NB! if using same midi-channel on both chord+controls")
    print("do not use the same MIDI-notes or CC messages \n")
    
    print("q-quits")
    print("p-panic")
    print("t-test")
    print("i-session info")
    print('n - new page with chordsx|')
    
    midi.startLoop_keyboardlistener(_destruct, midi, Misc) # polling the keyboard 
    

##################################################################################   
if __name__ == "__main__": main()    
    
    