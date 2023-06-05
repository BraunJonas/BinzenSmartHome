from AktorDevice import Device
from AktorDevice import LightIntensityMeasureAble
from AktorDevice import OpenCloseAble

class Window(Device, LightIntensityMeasureAble, OpenCloseAble):
    def __init__(self, name:str):
        print("Window "+ name +" has been created")
        super().__init__(name)

    def setOpen(self, open:bool):
        super().setOpen(open)
        print("window "+ str(self.name) + "changed open to" + str(open))
    
    def activateNightMode(self):
        self.setOpen(False)
        self.closeBlades()
        print("Window "+str(self.name) + "activated Night Mode")

    def closeBlades(self):
        print("Window: Close blades")

    def openBlades(self):
        print("Window: Close blades")
        