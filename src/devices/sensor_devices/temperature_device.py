import logging
from actors.temperature_adjustable import TemperatureAdjustable
from devices.device_communication.event_manager import EventManager
from devices.sensor_devices.sensor_device import SensorDevice
from sensors.temperature_sensor import TemperatureSensor

class TemperatureDevice(SensorDevice, TemperatureAdjustable):
    
    def __init__(self, name: str):
        super().__init__("TemperatureDevice: " + name)
        self.logger = logging.getLogger(__name__)
        self.logger.info("TemeratureDevice " + name + " has been created")
        self.sensor = TemperatureSensor()
        self.target = 16

    #Festelgen des Teperaturwertes
    def setTemperature(self, temp: int):
        if(0 < temp < 50):
            self.target = temp
            self.logger.info("TemperatureDevice " + str(self.name) + " set Target to " + str(temp))

    #Rückgabe des temperaturwretes
    def getTemperature(self) -> int:
        return self.target

    #Differendberechnung zwischen sensor Wert und target Wert
    def checkDifferenceToTarget(self) -> int:
        return self.target - self.sensor.getData()
    
    #Simulation eines Durchlaufs gemäß der Main-Klasse
    def simuliereEinenThreadDurchlauf(self):
        self.sensor.setRandomData()
        if not self.sensor.checkEverythingNormal():
            #Verbesserungspotential -> Anpassung normalen Bereich an Target
            #Idee Alarme sollen nur unrealistische Temperaturen überprüfen -> "Funktionsweise des Geräts"
            EventManager.notify("alarm", f"TemperatureDevice {self.name} is measuring unusual Temperature- check if the sensor is broken or an unusual Targt is set.")
            self.logger.warning(f"TemperatureDevice {self.name} is measuring unusual Temperature- check if the sensor is broken or an unusual Targt is set.")

        diff = self.checkDifferenceToTarget()
        self.logger.info(f"TemperatureDevice {self.name} is {'cooling' if diff<0 else 'heating'} Difference to Target: {diff}" )

    #Klonieren gemäß Prototype
    def clone(self, name: str):
        clone = TemperatureDevice(name)
        clone.setTemperature(self.getTemperature())
        return clone