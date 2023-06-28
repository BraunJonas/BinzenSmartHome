from devices.event_listener import EventListerner
from devices.event_manager import EventManager
from devices.watering_strategy import WateringStrategy, WateringStrategyNormal, WateringStrategySaveUp
from .device import Device 
from actors.amount_adjustable import AmountAdjustable
import logging

class WateringDevice(Device, AmountAdjustable, EventListerner):
    def __init__(self, name: str):
        super().__init__(name)
        self.logger = logging.getLogger(__name__)
        self.logger.info("WateringDevice " + name + " has been created")
        self.amount = 2
        self.strategy = WateringStrategyNormal()
        EventManager.subscribe(self, "water")

    def setAmount(self, amount: float):
        self.amount = amount
        self.logger.info("WateringDevice " + str(self.name) + "changed amount to " + str(amount))

    def getAmount(self) -> float:
        return self.amount
    
    def setWateringStrategy(self,strategy: WateringStrategy):
        self.strategy=strategy

    #Design Pattern Observer Listening auf Water Event
    #Design Pattern Strategy -> Wässerungsverhalten wird nach der Strategie bestimmt
    def notify(self, event: str, additionalInformation: str):
        if event == "water":
            if additionalInformation == "Enough Water":
                self.setWateringStrategy(WateringStrategyNormal())
            elif additionalInformation == "Not enough Water":
                self.setWateringStrategy(WateringStrategySaveUp())
    
class WateringDeviceGround(WateringDevice, AmountAdjustable):
    def __init__(self, name: str):
        super().__init__(name)
        self.logger.info("WateringDeviceGround " + name + " has been created")

    def simuliereEinenThreadDurchlauf(self):
        amountUsed = self.strategy.execute(self.amount)
        self.logger.info(f"WateringDeviceGround {self.name} is watering {amountUsed}l per day" )

class WateringDeviceDrops(WateringDevice, AmountAdjustable):
    def __init__(self, name: str):
        super().__init__(name)
        self.logger.info("WateringDeviceDrops " + name + " has been created")

    def simuliereEinenThreadDurchlauf(self):
        amountUsed = self.strategy.execute(self.amount)
        self.logger.info(f"WateringDeviceDrops {self.name} is watering {amountUsed}l per day" )
    