from abc import ABC, abstractmethod
import Aktor

class IntencityToggleAble(ABC, Aktor):

    def __init__(self, intencity:int):
        self.intencity = intencity

    @abstractmethod
    def getIntencity(self) -> int:
        pass    
    @abstractmethod
    def setIntencity(self, intencity):
        pass
