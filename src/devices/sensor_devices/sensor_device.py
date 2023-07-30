from devices.device import Device
#Abstrakte Klasse zum hinzufügen eines sensors in eine Device
class SensorDevice(Device):
    def checkDifferenceToTarget(self):
        raise NotImplementedError