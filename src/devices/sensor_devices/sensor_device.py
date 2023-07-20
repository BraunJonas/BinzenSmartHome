from src.devices.device import Device

class SensorDevice(Device):
    def checkDifferenceToTarget(self):
        raise NotImplementedError