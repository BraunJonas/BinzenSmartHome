from devices.event_manager import EventManager
from .device import Device
from sensors.light_sensor import LightSensor
from actors.percentage_adjustable import PercentageAdjustable
import logging

class ShadowingDevice(Device, LightSensor):
    
    def __init__(self, name: str, sensor: LightSensor):
        super().__init__(name)
        self.logger = logging.getLogger(__name__)
        self.logger.info("ShadowingDevice " + name + " has been created")
        self.sensor = sensor
        self.target = 50


    def setPercentage(self, lightintensity: int):
        self.target = lightintensity
        self.logger.info("ShadowingDevice " + str(self.name) + " set Target to " + str(lightintensity))


    def getPercentage(self ):
        return self.target 

    def checkDifferenceToTarget(self) -> int:
        return self.target - self.sensor.getData()
    
    def simuliereEinenThreadDurchlauf(self):
        self.sensor.setRandomData()
        if not self.sensor.checkEverythingNormal():
            self.logger.warning(f"ShadowingDevice {self.name} is measuring unusual LightIntensity- check if the sensor is broken or an unusual Targt is set." )
            EventManager.notify("alarm", f"ShadowingDevice {self.name} is measuring unusual LightIntensity- check if the sensor is broken or an unusual Targt is set.")
        diff = self.checkDifferenceToTarget()
        self.logger.info(f"ShadowingDevice {self.name} is trying to {'decrease ' if diff<0 else 'increase'} lightintensity. Difference to Target: {diff}" )