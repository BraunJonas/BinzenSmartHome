from device import Device
from sensors.temperature_measurable import TemperatureMeasureable
from actors.temperature_toggleable import TemperatureToggleable



class CoolingDevice(Device, TemperatureMeasureable, TemperatureToggleable):
    def __init__(self, name: str):
        print("CoolingDevice " + name + " has been created")
        super().__init__(name)

    def setTemperature(self, temp: int):
        super().setTemperature(temp)
        print("CoolingDevice " + str(self.name) + " set Temperature to " + str(temp))
        if self.checkAboveTarget:
            print("start cooling")

    def activateNightMode(self):
        self.setTemperature(16)
        print("CoolingDevice " + str(self.name) + " activated Night Mode")

    def checkAboveTarget(self, temp) -> bool:
        if self.getTemperature < self.measureTemperature:
            return True
        return False

