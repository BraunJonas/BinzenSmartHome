from .device import Device 
from actors.amount_adjustable import AmountAdjustable
import logging

class FertilizeDevice(Device, AmountAdjustable):
    def __init__(self, name: str):
        super().__init__(name)
        self.logger = logging.getLogger(__name__)
        self.logger.info("FertilizeDevice " + name + " has been created")
        self.amount = 50

    def setAmount(self, amount: float):
        self.amount = amount
        self.logger.info("FertilizeDevice " + str(self.name) + "changed amount to " + str(amount))

    def getAmount(self) -> float:
        return self.amount
    
    def simuliereEinenThreadDurchlauf(self):
        self.logger.info(f"FertilizeDevice {self.name} is fertilizing {self.amount}g per day" )