import Device
import IntencityToggleAble
import SwitchOnOffAble

class AudioDevice(Device,IntencityToggleAble,SwitchOnOffAble):
    
    
    def __init__(self, name:str, intencity:int,running:bool):
        self.name = name
        self.intencity = intencity
        self.running = running

    #Abstract Methods
    #Device
    def getName(self) -> str:
         return self.name
        
        
    #IntensityToggleAble
    #SwitchOnOffAble