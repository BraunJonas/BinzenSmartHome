import logging

from src import devices
from src.actors.amount_adjustable import AmountAdjustable
from src.actors.open_closeable import OpenCloseable
from src.actors.percentage_adjustable import PercentageAdjustable
from src.actors.switch_on_offable import SwitchOnOffable
from src.actors.temperature_adjustable import TemperatureAdjustable
from src.devices.device import Device


class Zone:
    
    def __init__(self, name: str):
        self.name = name
        self.logger = logging.getLogger(__name__)
        self.logger.info("Zone " + name + " has been created")
        self.devices = []

    def getDevices(self):
        return self.devices

    def getName(self):
        return self.name

    def addDevice(self, device: Device):
        self.logger.info(f"Device added to Zone {self.name}")
        self.devices.append(device)

    def removeDevice(self, device: Device):
        self.devices.remove(device)

    def simuliereEinenThreadDurchlauf(self):
        for d in self.devices:
            d.simuliereEinenThreadDurchlauf()

    def clone(self, name: str):
        clone = Zone(name)
        for d in self.devices:

            clone.addDevice(d.clone("Device von Zone: " + name))
        return clone

    def changeAmount(self, amount: int, type):
        if not issubclass(type, AmountAdjustable):
            self.logger.warning("Change Amount was called for the wrong Type")
            return
        foundDevice = False
        for d in self.devices:
            if isinstance(d,type):
                d.setAmount(d.getAmount()+amount)
                foundDevice = True
        if not foundDevice:
            self.logger.warning("Zone "+ self.name + " has no Device with Type "+ str(type))

    def changePercentage(self, percentage: int, type):
        if not issubclass(type, PercentageAdjustable):
            self.logger.warning("Change Percentage was called for the wrong Type")
            return
        foundDevice = False
        for d in self.devices:
            if isinstance(d,type):
                d.setPercentage(d.setPercentage()+percentage)
                foundDevice = True
        if not foundDevice:
            self.logger.warning("Zone "+ self.name + " has no Device with Type "+ str(type))


