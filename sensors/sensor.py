from abc import ABC, abstractmethod

class Sensor(ABC):
    @abstractmethod       
    def checkEverythingNormal(self) -> bool:
        pass

    