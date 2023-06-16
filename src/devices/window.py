from .device import Device
from actors.open_closeable import OpenCloseable

class Window(Device, OpenCloseable):
    def __init__(self, name: str):
        print("Window " + name + " has been created")
        super().__init__(name)
        self.open = False


    def setOpen(self, open: bool):
        print("Window " + str(self.name) + " changed open to " + str(open))
        self.open = open

    def isOpen(self) -> bool:
        return self.isOpen   

def simuliereEinenThreadDurchlauf(self):
        print(f"Window {self.name} is {'open' if self.open else 'closed'}" )
