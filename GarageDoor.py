from Device import Device
from OpenCloseAble import OpenCloseAble


class GarageDoor(Device, OpenCloseAble):
    def __init__(self, name: str):
        print("GarageDoor " + name + " has been created")
        super().__init__(name)

    def setOpen(self, open: bool):
        super().setOpen(open)
        print("GarageDoor " + str(self.name) + " changed open to " + str(open))

    def activateNightMode(self):
        self.setOpen(False)
        print("GarageDoor " + str(self.name) + " activated Night Mode")
