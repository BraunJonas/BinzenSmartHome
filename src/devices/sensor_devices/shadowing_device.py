import logging
from actors.percentage_adjustable import PercentageAdjustable
from devices.device_communication.event_manager import EventManager
from devices.sensor_devices.sensor_device import SensorDevice
from sensors.light_sensor import LightSensor

class ShadowingDevice(SensorDevice, PercentageAdjustable):
    
    def __init__(self, name: str):
        super().__init__("ShadowingDevice: " + name)
        self.logger = logging.getLogger(__name__)
        self.logger.info("ShadowingDevice " + name + " has been created")
        self.sensor = LightSensor()
        self.target = 50

    #Festlegen des Prozentwertes für die Device
    def setPercentage(self, lightintensity: int):
        if(0 < lightintensity < 100):
            self.target = lightintensity
            self.logger.info("ShadowingDevice " + str(self.name) + " set Target to " + str(lightintensity))

    #Rückgabe des Prozentwertes für die Device
    def getPercentage(self ):
        return self.target 

    #Unterschiedberechnung zwishen target wert und gemessenem wert des sensors
    def checkDifferenceToTarget(self) -> int:
        return self.target - self.sensor.getData()
    
    #Simulation eines Durchlaufs -> Siehe Main Klasse
    def simuliereEinenThreadDurchlauf(self):
        self.sensor.setRandomData()
        if not self.sensor.checkEverythingNormal():
            self.logger.warning(f"ShadowingDevice {self.name} is measuring unusual LightIntensity- check if the sensor is broken or an unusual Targt is set." )
            EventManager.notify("alarm", f"ShadowingDevice {self.name} is measuring unusual LightIntensity- check if the sensor is broken or an unusual Targt is set.")
        diff = self.checkDifferenceToTarget()
        self.logger.info(f"ShadowingDevice {self.name} is trying to {'decrease ' if diff<0 else 'increase'} lightintensity. Difference to Target: {diff}" )

    #Klonieren der Device gemäß Prototype Konzept
    def clone(self, name: str):
        clone = ShadowingDevice(name)
        clone.setPercentage(self.getPercentage())
        return clone