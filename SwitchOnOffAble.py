from abc import ABC, abstractmethod

import Aktor
class SwitchOnOffAble(ABC,Aktor):
    def __init__(self, running:bool):
        self.running = running
        
    @abstractmethod
    def setRunning(self, running:bool):
        pass
     
    @abstractmethod
    def isRunning(self) -> bool:
        pass