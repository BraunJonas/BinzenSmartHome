from devices.event_manager import EventManager
from .device import Device
from sensors.temperature_sensor import TemperatureSensor
from actors.temperature_adjustable import TemperatureAdjustable
import logging

class TemeratureDevice(Device, TemperatureAdjustable):
    
    def __init__(self, name: str, sensor: TemperatureSensor):
        super().__init__(name)
        self.logger = logging.getLogger(__name__)
        self.logger.info("TemeratureDevice " + name + " has been created")
        self.sensor = sensor
        self.target = 16

    def setTemperature(self, temp: int):
        self.target = temp
        self.logger.info("TemperatureDevice " + str(self.name) + " set Target to " + str(temp))

    def getTemperature(self) -> int:
        return self.target

    def checkDifferenceToTarget(self) -> int:
        return self.target - self.sensor.getData()
    
    def simuliereEinenThreadDurchlauf(self):
        self.sensor.setRandomData()
        if not self.sensor.checkEverythingNormal():
            #Verbesserungspotential -> Anpassung normalen Bereich an Target
            #Idee Alarme sollen nur unrealistische Temperaturen überprüfen -> "Funktionsweise des Geräts"
            EventManager.notify("alarm", f"TemperatureDevice {self.name} is measuring unusual Temperature- check if the sensor is broken or an unusual Targt is set.")
            self.logger.warning(f"TemperatureDevice {self.name} is measuring unusual Temperature- check if the sensor is broken or an unusual Targt is set.")

        diff = self.checkDifferenceToTarget()
        self.logger.info(f"TemperatureDevice {self.name} is {'cooling' if diff<0 else 'heating'} Difference to Target: {diff}" )
