from device import Device
from sensors.temperature_measurable import TemperatureMeasureable
from actors.temperature_toggleable import TemperatureToggleable



class HeatingDevice(Device, TemperatureMeasureable, TemperatureToggleable):
    def __init__(self, name: str):
        print("HeatingDevice " + name + " has been created")
        super().__init__(name)

    def setTemperature(self, temp: int):
        super().setTemperature(temp)
        print("HeatingDevice " + str(self.name) + " set Temperature to " + str(temp))
        if self.checkBeneathTarget:
            print("start haeting")

    def activateNightMode(self):
        self.setTemperature(16)
        print("HeatingDevice " + str(self.name) + " activated Night Mode ")

    def checkBeneathTarget(self, temp) -> bool:
        if self.getTemperature > self.measureTemperature:
            return True
        return False

