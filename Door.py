from Device import Device
from OpenCloseAble import OpenCloseAble


class Door(Device, OpenCloseAble):
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
