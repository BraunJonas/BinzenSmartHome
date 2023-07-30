import logging
from actors.open_closeable import OpenCloseable
from devices.device import Device


class Window(Device, OpenCloseable):

    def __init__(self, name: str):
        super().__init__("Window: " + name)
        self.logger = logging.getLogger(__name__)
        self.logger.info("Window " + name + " has been created")
        self.open = False

    #Festleugung ob fenster geöffnet oder geschlossen
    def setOpen(self, open: bool):
        self.logger.info("Window " + str(self.name) + " changed open to " + str(open))
        self.open = open

    #Abfrage ob fenster geöffnet ist
    def isOpen(self) -> bool:
        return self.open

    #Simulation eines Durchlaufs -> Main Klasse
    def simuliereEinenThreadDurchlauf(self):
        self.logger.info(f"Window {self.name} is {'open' if self.open else 'closed'}" )

    #klonieren gemäß Prototype
    def clone(self, name: str):
        clone = Window(name)
        clone.setOpen(self.open)
        return clone
