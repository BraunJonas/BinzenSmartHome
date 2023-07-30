import logging
from devices.device_communication.event_manager import EventManager
from devices.sensor_devices.sensor_device import SensorDevice
from sensors.humidity_sensor import HumiditySensor

class HumidityDevice(SensorDevice):
    
    def __init__(self, name: str):
        super().__init__("HumidityDevice: " + name)
        self.logger = logging.getLogger(__name__)
        self.logger.info("HumidityDevice " + name + " has been created")
        self.sensor = HumiditySensor()
        self.target = 40

    #Einstellen des Prozentwertes mit Gültigkeitseingabe
    def setPercentage(self, percentage: int):
        if(0 < percentage < 100):
            self.target = percentage
            self.logger.info("HumidityDevice " + str(self.name) + " set Target to " + str(percentage))

    #Rückgabe des Prozentwertes für die Dvice
    def getPercentage(self ):
        return self.target 

    #Unterschiedberechnung zwischen target und sensor Messung
    def checkDifferenceToTarget(self) -> int:
        return self.target - self.sensor.getData()
    
    #dimulieren eines Durchlaufs siehe Main Klasse
    def simuliereEinenThreadDurchlauf(self):
        self.sensor.setRandomData()
        if not self.sensor.checkEverythingNormal():
            self.logger.warning(f"HumidityDevice {self.name} is measuring unusual Humidity- check if the sensor is broken or an unusual Targt is set.")
            EventManager.notify("alarm", f"HumidityDevice {self.name} is measuring unusual Humidity- check if the sensor is broken or an unusual Targt is set.")
        diff = self.checkDifferenceToTarget()
        self.logger.info(f"HumidityDevice {self.name} is trying to {'increase ' if diff<0 else 'decrease'} huidity. Difference to Target: {diff}" )

    #klonieren einer device gemäß Prototype
    def clone(self, name: str):
        clone = HumidityDevice(name)
        clone.setPercentage(self.getPercentage())
        return clone