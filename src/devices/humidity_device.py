from devices.event_manager import EventManager
from .device import Device
from sensors.humidity_sensor import HumiditySensor
import logging

class HumidityDevice(Device, HumiditySensor):
    
    def __init__(self, name: str, sensor: HumiditySensor):
        super().__init__(name)
        self.logger = logging.getLogger(__name__)
        self.logger.info("HumidityDevice " + name + " has been created")
        self.sensor = sensor
        self.target = 40


    def setPercentage(self, percentage: int):
        self.target = percentage
        self.logger.info("HumidityDevice " + str(self.name) + " set Target to " + str(percentage))

    def getPercentage(self ):
        return self.target 

    def checkDifferenceToTarget(self) -> int:
        return self.target - self.sensor.getData()
    
    def simuliereEinenThreadDurchlauf(self):
        self.sensor.setRandomData()
        if not self.sensor.checkEverythingNormal():
            self.logger.warning(f"HumidityDevice {self.name} is measuring unusual Humidity- check if the sensor is broken or an unusual Targt is set.")
            EventManager.notify("alarm", f"HumidityDevice {self.name} is measuring unusual Humidity- check if the sensor is broken or an unusual Targt is set.")
        diff = self.checkDifferenceToTarget()
        self.logger.info(f"HumidityDevice {self.name} is trying to {'increase ' if diff<0 else 'decrease'} huidity. Difference to Target: {diff}" )