import logging
from src.actors.amount_adjustable import AmountAdjustable

from src.devices.device import Device


class FertilizeDevice(Device, AmountAdjustable):
    def __init__(self, name: str):
        super().__init__(name)
        self.logger = logging.getLogger(__name__)
        self.logger.info("FertilizeDevice " + name + " has been created")
        self.amount = 50

    def setAmount(self, amount: float):
        if(amount>0):
            self.amount = amount
            self.logger.info("FertilizeDevice " + str(self.name) + " changed amount to " + str(amount))
        else:
            self.logger.info("FertilizeDevice " + str(self.name) + " can't set amount below 0")


    def getAmount(self) -> float:
        return self.amount
    
    def simuliereEinenThreadDurchlauf(self):
        self.logger.info(f"FertilizeDevice {self.name} is fertilizing {self.amount}g per day" )

    def clone(self, name: str):
        clone = FertilizeDevice(name)
        clone.setAmount(self.amount)
        return clone
