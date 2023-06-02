from Device import Device
from TemperatureMeasureAble import TemperatureMeasureAble
from TemperatureToggleAble import TemperatureToggleAble

class CoolingDevice(Device, TemperatureMeasureAble, TemperatureToggleAble):
    def __init__(self, name:str):
        print("CoolingDevice "+ name +" has been created")
        super().__init__(name)

    def setTemperature(self, temp:int):
        super().setTemperature(temp)
        print("CoolingDevice "+ str(self.name) + "set Temperature to" + str(temp))
        if(self.checkAboveTarget):
            print("start cooling")

    
    def activateNightMode(self):
        self.setTemperature(16)
        print("CoolingDevice "+str(self.name) + "activated Night Mode")

    def checkAboveTarget(self, temp) -> bool:
        if(self.getTemperature < self.measureTemperature):
            return True
        return False
    