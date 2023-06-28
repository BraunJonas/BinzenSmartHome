from devices.device import Device

class Room:
    

    def __init__(self, name: str):
        self.name = name
        print("Room " + name + " has been created")
        self.devices = []

    def getDevices(self):
        print(f"{self.name} {len(self.devices)}")
        return self.devices

    def getName(self):
        return self.name

    def addDevice(self, device: Device):
        print(f"Device added to Room {self.name}")
        self.devices.append(device)

