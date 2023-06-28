from devices.device import Device
import logging

class Room:
    

    def __init__(self, name: str):
        self.name = name
        self.logger = logging.getLogger(__name__)
        self.logger.info("Room " + name + " has been created")
        self.devices = []

    def getDevices(self):
        self.logger.info(f"{self.name} {len(self.devices)}")
        return self.devices

    def getName(self):
        return self.name

    def addDevice(self, device: Device):
        self.logger.info(f"Device added to Room {self.name}")
        self.devices.append(device)

