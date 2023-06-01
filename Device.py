from abc import ABC, abstractmethod

class Device(ABC):
    def __init__(self, name:str):
        self.name = name
    @abstractmethod
    def getName(self) -> str:
        pass
    @abstractmethod
    def setName(self, name:str):
        pass