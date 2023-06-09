from .device import Device
from actors.open_closeable import OpenCloseable
import logging
class Window(Device, OpenCloseable):
    def __init__(self, name: str):
        super().__init__(name)
        self.logger = logging.getLogger(__name__)
        self.logger.info("Window " + name + " has been created")
        self.open = False


    def setOpen(self, open: bool):
        self.logger.info("Window " + str(self.name) + " changed open to " + str(open))
        self.open = open

    def isOpen(self) -> bool:
        return self.isOpen   

def simuliereEinenThreadDurchlauf(self):
        self.logger.info(f"Window {self.name} is {'open' if self.open else 'closed'}" )
