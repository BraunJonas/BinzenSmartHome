from .device import Device 
from actors.amount_adjustable import AmountAdjustable

class FertilizeDevice(Device, AmountAdjustable):
    def __init__(self, name: str):
        print("FertilizeDevice " + name + " has been created")
        super().__init__(name)
        self.amount = 50

    def setAmount(self, amount: float):
        self.amount = amount
        print("FertilizeDevice " + str(self.name) + "changed amount to " + str(amount))

    def getAmount(self) -> float:
        return self.amount
    
    def simuliereEinenThreadDurchlauf(self):
        print(f"FertilizeDevice {self.name} is fertilizing {self.amount}g per day" )