from devices.WaterEventListener import WaterEventListerner
from devices.water_event_manager import WaterEventManager
from devices.watering_strategy import WateringStrategy, WateringStrategyNormal, WateringStrategySaveUp
from .device import Device 
from actors.amount_adjustable import AmountAdjustable

class WateringDevice(Device, AmountAdjustable, WaterEventListerner):
    def __init__(self, name: str):
        print("WateringDevice " + name + " has been created")
        super().__init__(name)
        self.amount = 2
        self.strategy = WateringStrategyNormal()
        WaterEventManager.subscribe(self)

    def setAmount(self, amount: float):
        self.amount = amount
        print("WateringDevice " + str(self.name) + "changed amount to " + str(amount))

    def getAmount(self) -> float:
        return self.amount
    
    def setWateringStrategy(self,strategy: WateringStrategy):
        self.strategy=strategy

    #Design Pattern Observer Listening auf Water Event
    #Design Pattern Strategy -> Wässerungsverhalten wird nach der Strategie bestimmt
    def notify(self, enoughWater: bool):
        if enoughWater:
            self.setWateringStrategy(WateringStrategyNormal())
        else:
            self.setWateringStrategy(WateringStrategySaveUp())
    
class WateringDeviceGround(WateringDevice, AmountAdjustable):
    def __init__(self, name: str):
        print("WateringDeviceGround " + name + " has been created")
        super().__init__(name)

    def simuliereEinenThreadDurchlauf(self):
        amountUsed = self.strategy.execute(self.amount)
        print(f"WateringDeviceGround {self.name} is watering {amountUsed}l per day" )

class WateringDeviceDrops(WateringDevice, AmountAdjustable):
    def __init__(self, name: str):
        print("WateringDeviceDrops " + name + " has been created")
        super().__init__(name)

    def simuliereEinenThreadDurchlauf(self):
        amountUsed = self.strategy.execute(self.amount)
        print(f"WateringDeviceDrops {self.name} is watering {amountUsed}l per day" )
    