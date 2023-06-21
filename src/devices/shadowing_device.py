from devices.event_manager import EventManager
from .device import Device
from sensors.light_sensor import LightSensor
from actors.percentage_adjustable import PercentageAdjustable

class ShadowingDevice(Device, LightSensor):
    
    def __init__(self, name: str, sensor: LightSensor):
        print("ShadowingDevice " + name + " has been created")
        super().__init__(name)
        self.sensor = sensor
        self.target = 50


    def setPercentage(self, lightintensity: int):
        self.target = lightintensity
        print("ShadowingDevice " + str(self.name) + " set Target to " + str(lightintensity))


    def getPercentage(self ):
        return self.target 

    def checkDifferenceToTarget(self) -> int:
        return self.target - self.sensor.getData()
    
    def simuliereEinenThreadDurchlauf(self):
        self.sensor.setRandomData()
        if not self.sensor.checkEverythingNormal():
            EventManager.notify("alarm", f"ShadowingDevice {self.name} is measuring unusual LightIntensity- check if the sensor is broken or an unusual Targt is set.")
        diff = self.checkDifferenceToTarget()
        print(f"ShadowingDevice {self.name} is trying to {'decrease ' if diff<0 else 'increase'} lightintensity. Difference to Target: {diff}" )