import LightIntencityMeasurable, Device 

class Window(LightIntencityMeasurable, Device):
    def __init__(self, name):
        self.name = name

    def closeBlades(self):
        print("Window: Close blades")
        