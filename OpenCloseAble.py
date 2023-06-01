from abc import ABC, abstractmethod
import Aktor

class OpenCloseAble(Aktor):

    def __init__(self, open:bool):
        self.open = open

    @abstractmethod
    def getOpen(self) -> bool:
        pass

    @abstractmethod
    def setOpen(self, open):
        pass