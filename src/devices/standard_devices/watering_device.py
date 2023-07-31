import logging
from actors.amount_adjustable import AmountAdjustable
from devices.device_communication.event_listener import EventListener
from devices.device_communication.event_manager import EventManager
from devices.standard_devices.watering_strategy import WateringStrategy, WateringStrategyNormal, WateringStrategySaveUp
from devices.device import Device


class WateringDevice(Device, AmountAdjustable, EventListener):
    def __init__(self, name: str):
        super().__init__(name)
        self.logger = logging.getLogger(__name__)
        self.logger.info("WateringDevice " + name + " has been created")
        self.amount = 2
        self.strategy = WateringStrategyNormal()
        EventManager.subscribe(self, "water")

    #Festlegung eiens wertes für bewässerung
    def setAmount(self, amount: float):
        if amount>0:
            self.amount = amount
            self.logger.info("WateringDevice " + str(self.name) + "changed amount to " + str(amount))

    #Rückgabe des bewässerungwertes
    def getAmount(self) -> float:
        return self.amount
    
    #Festlegung der wateringstrategy strategy pattern
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
        super().__init__("WateringDeviceGround: " + name)
        self.logger.info("WateringDeviceGround " + name + " has been created")

    #Simulation eines Durchlaufs -> Main Klasse
    def simuliereEinenThreadDurchlauf(self):
        amountUsed = self.strategy.execute(self.amount)
        self.logger.info(f"WateringDeviceGround {self.name} is watering {amountUsed}l per day" )

    #klonieren gemäß Prototype
    def clone(self, name: str):
        clone = WateringDeviceGround(name)
        clone.setAmount(self.amount)
        clone.setWateringStrategy(self.strategy)
        return clone

class WateringDeviceDrops(WateringDevice, AmountAdjustable):
    def __init__(self, name: str):
        super().__init__("WateringDeviceDrops: " + name)
        self.logger.info("WateringDeviceDrops " + name + " has been created")

    #Simulation eines durchlaufs -> Main Klasse
    def simuliereEinenThreadDurchlauf(self):
        amountUsed = self.strategy.execute(self.amount)
        self.logger.info(f"WateringDeviceDrops {self.name} is watering {amountUsed}l per day" )

    #klonieren gemäß Prototyüe
    def clone(self, name: str):
        clone = WateringDeviceDrops(name)
        clone.setAmount(self.amount)
        clone.setWateringStrategy(self.strategy)
        return clone
    