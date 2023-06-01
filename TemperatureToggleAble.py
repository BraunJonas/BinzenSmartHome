from abc import ABC, abstractmethod
import Aktor

class TemperatureToggleAble(ABC, Aktor):
    def __init__(self, targetTemperature: int):
        self.targetTemperature = targetTemperature
    @abstractmethod
    def getTargetTemperature(self) -> int:
        pass
    @abstractmethod
    def setTargetTemperature(self, intensity): #Exception fehlt noch
        pass

    