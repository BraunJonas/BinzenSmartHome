from devices.device import Device


class Room:
    name = ""
    devices = []

    def __init__(self, name: str):
        self.name = name
        print("Room " + name + " has been created")

    def getDevices(self):
        return self.devices

    def getName(self):
        return self.name

    def addDevice(self, device: Device):
        print("Device added to Room")
        self.devices.append(device)
