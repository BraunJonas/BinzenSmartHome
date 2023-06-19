from .device import Device
from sensors.temperature_sensor import TemperatureSensor
from actors.temperature_adjustable import TemperatureAdjustable

class TemeratureDevice(Device, TemperatureAdjustable):
    
    def __init__(self, name: str, sensor: TemperatureSensor):
        print("TemeratureDevice " + name + " has been created")
        super().__init__(name)
        self.sensor = sensor
        self.target = 16


    def setTemperature(self, temp: int):
        self.target = temp
        print("TemperatureDevice " + str(self.name) + " set Target to " + str(temp))

    def getTemperature(self) -> int:
        return self.temperature

    def checkDifferenceToTarget(self) -> int:
        return self.target - self.sensor.getData()
    
    def simuliereEinenThreadDurchlauf(self):
        self.sensor.setRandomData()
        diff = self.checkDifferenceToTarget()
        print(f"TemperatureDevice {self.name} is {'cooling' if diff<0 else 'heating'} Difference to Target: {diff}" )
