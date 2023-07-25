# -*- coding: utf-8 -*-
"""
Created on Sun Jan 15 17:51:35 2023

@author: rolfe
"""
  
#from dataclasses import dataclass

#from chord_classes2 import UserInteraction as ui


#from setup import SetupBlacstarController


class SessionMain():
    
    def __init__(self):
        self._midichannel_bass =0
        self._midiTrough = True
        self._midichannel_out=0
        self._midichannel_controls=0
        
        self._controlArraySession = None
    
    
    
    # @dataclass
    # class data:
    #     '''
    #     data struct used during a typical session
    #     '''
    #     out_port_index: int
    #     in_port_index_bass: int
    #     in_port_index_control: int
      
    #     midi_channel_in_bass: int
    #     midi_channel_in_control: int
       
    #     midi_channel_out: int
       
    #     filepath: str
    #     controlSchemes: int
    
    def listControlsCurrentSession():
        pass
    
    def addChordScheme(controlArr):
        '''
        '''
        
        #controlarray.extend(.....)
        
        pass
    
    def nextChordScheme():
        pass
    
    
    def _attachControlstoGlobal():
        '''
        
        '''
        #Global.controls = self._controlArraySession
        pass
    
    
    @property
    def midichannelBass(self):
        return self._midichannel_bass
    
    @midichannelBass.setter
    def midichannelBass(self, ch):
        self._midichannel_bass = ch
            
    @property
    def midiChannelControls(self):
        return self._midichannel_controls
    
    @midiChannelControls.setter
    def midiChannelControls(self, ch):
        self._midichannel_controls = ch      
        
    @property
    def midiChannelOut(self):
        return self._midichannel_out
    
    @midiChannelOut.setter
    def midiChannelOut(self, ch):
        self._midichannel_out = ch   
    
    def report(self):
        print('\n')
        print(" --- Session Report --- ")
        print("Midi channel out: \t\t", self._midichannel_out)
        print("Midi channel control: \t", self._midichannel_controls)
        print("Midi channel bass: \t\t", self._midichannel_bass)
        
        print('Midi trough: ', self._midiTrough)
        

        
     
     

    