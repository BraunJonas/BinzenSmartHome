from .device import Device
from actors.open_closeable import OpenCloseable

# OCP - offen für Erweiterungen, geschlossen für Modifikationen: 
# Door erbt von Device und erweitert die Funktionalität ohne den bestehenden Code zu ändern
class Door(Device, OpenCloseable):
    def __init__(self, name: str):
        print("Door " + name + " has been created")
        super().__init__(name)

    def setOpen(self, open: bool):
        super().setOpen(open)
        print("Door " + str(self.name) + " changed open to " + str(open))

    def activateNightMode(self):
        self.setOpen(False)
        print("Door " + str(self.name) + " activated Night Mode")

    def lock(self):
        print("Door " + str(self.name) + " locked")

    def unlock(self):
        print("Door " + str(self.name) + " unlocked")

