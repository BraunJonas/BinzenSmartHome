from Device import Device 
from LightIntencityMeasurable import LightIntensityMeasureAble
from SwitchOnOffAble import SwitchOnOffAble

class Light(Device, SwitchOnOffAble, LightIntensityMeasureAble):
    def __init__(self, name:str):
        print("Light "+ name +" has been created")
        super().__init__(name)

    def setRunning(self, running:bool):
        super().setRunning(running)
        print("Light "+ str(self.name) + "changed running to" + str(running))
    
    def activateNightMode(self):
        self.setRunning(False)
        print("Light "+str(self.name) + "activated Night Mode")
