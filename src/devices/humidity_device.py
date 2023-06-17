from .device import Device
from sensors.humidity_sensor import HumiditySensor
from actors.percentage_adjustable import PercentageAdjustable

class HumidityDevice(Device, HumiditySensor):
    
    def __init__(self, name: str, sensor: HumiditySensor):
        print("HumidityDevice " + name + " has been created")
        super().__init__(name)
        self.sensor = sensor
        self.target = 40


    def setPercentage(self, percentage: int):
        self.target = percentage
        print("HumidityDevice " + str(self.name) + " set Target to " + str(percentage))

    def getPercentage(self ):
        return self.target 

    def checkDifferenceToTarget(self) -> int:
        return self.target - self.sensor.getData()
    
    def simuliereEinenThreadDurchlauf(self):
        diff = self.checkDifferenceToTarget()
        print(f"HumidityDevice {self.name} is trying to {'increase ' if diff<0 else 'decrease'} huidity. Difference to Target: {diff}" )