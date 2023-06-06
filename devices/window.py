from .device import Device
from sensors.light_intensity_measurable import LightIntensityMeasurable
from actors.open_closeable import OpenCloseable

class Window(Device, LightIntensityMeasurable, OpenCloseable):
    def __init__(self, name: str):
        print("Window " + name + " has been created")
        super().__init__(name)

    def setOpen(self, open: bool):
        super().setOpen(open)
        print("window " + str(self.name) + " changed open to " + str(open))

    def activateNightMode(self):
        self.setOpen(False)
        self.closeBlades()
        print("Window " + str(self.name) + " activated Night Mode ")

    def closeBlinds(self):
        print("Window: Close blinds")

    def openBlinds(self):
        print("Window: Close blinds")

