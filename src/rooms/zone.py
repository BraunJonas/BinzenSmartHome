import logging

from actors.amount_adjustable import AmountAdjustable
from actors.open_closeable import OpenCloseable
from actors.percentage_adjustable import PercentageAdjustable
from actors.switch_on_offable import SwitchOnOffable
from actors.temperature_adjustable import TemperatureAdjustable
from devices.device import Device


class Zone:
    #jeder Zone können Devices zugeordnet werden
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

    #Klonieren einer Zone mittels Aufruf gemäß Prototype , sowie klonierung der zugehörigen Geräte
    def clone(self, name: str):
        clone = Zone(name)
        for d in self.devices:
            clone.addDevice(d.clone("Device von Zone: " + name))
        return clone

    #Abändern des Wertes für eine Device
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

    #Abändern des Wertes für eine Device
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


