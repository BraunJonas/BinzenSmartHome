from .device import Device
from actors.open_closeable import OpenCloseable
import logging

class Door(Device, OpenCloseable):
    
    def __init__(self, name: str):
        super().__init__(name)
        self.logger = logging.getLogger(__name__)
        self.logger.info("Door " + name + " has been created")
        self.open = False
        self.locked = False

    def setOpen(self, open: bool):
        self.open = open
        self.logger.info(f"Door {self.name} is {'open' if self.open else 'closed'}")

    def isOpen(self) -> bool:
        return self.open   

    def isLocked(self) -> bool:
        return self.locked  
    
    def setLocked(self, locked: bool):
        if(self.open and locked):
            self.logger.info(f"Door {self.name} couldn't be locked because it is open")
            return
        self.locked = locked
        self.logger.info(f"Door {self.name} was {'locked' if self.locked else 'unlocked'}")

    def simuliereEinenThreadDurchlauf(self):
        self.logger.info(f"Door {self.name} is {'open' if self.open else 'closed'} and {'locked' if self.locked else 'unlocked'}" )
        

