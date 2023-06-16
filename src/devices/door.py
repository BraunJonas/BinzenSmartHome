from .device import Device
from actors.open_closeable import OpenCloseable

class Door(Device, OpenCloseable):
    
    def __init__(self, name: str):
        print("Door " + name + " has been created")
        super().__init__(name)
        self.open = False
        self.locked = False

    def setOpen(self, open: bool):
        self.open = open
        print("Door " + str(self.name) + " changed open to " + str(open))

    def isOpen(self) -> bool:
        return self.isOpen   

    def setLocked(self, locked: bool):
        if(self.open and locked):
            print(f"Door {self.name} couldn't be locked because it is open")
            return
        self.locked = True
        print("Door " + str(self.name) + "changed locked to" + str(locked))

    def simuliereEinenThreadDurchlauf(self):
        print(f"Door {self.name} is {'open' if self.open else 'closed'} and {'locked' if self.locked else 'unlocked'}" )

