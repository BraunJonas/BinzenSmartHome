from .device import Device 
from sensors.light_intensity_measurable import LightIntensityMeasurable
from actors.switch_on_offable import SwitchOnOffable
from actors.intensity_toggleable import IntensityToggleable

# CCP - Light und IntensityLight sind geschlossen gegenüber der selben Art von Veränderungen und sind deshalb in einem Modul zusammengefasst

class Light(Device, SwitchOnOffable, LightIntensityMeasurable):
    def __init__(self, name: str):
        print("Light " + name + " has been created")
        super().__init__(name)

    def setRunning(self, running: bool):
        super().setRunning(running)
        print("Light " + str(self.name) + "changed running to " + str(running))

    def activateNightMode(self):
        self.setRunning(False)
        print("Light " + str(self.name) + "activated Night Mode")

#LSP - Austauschbarkeit der Klassen: IntensityLight kann anstelle von Light verwendet werden, ohne die Funktionalität zu beeinträchtigen

class IntensityLight(IntensityToggleable, Light):
    def __init__(self, name: str):
        print("IntensityLight " + name + " has been created")
        super().__init__(name)

    def activateNightMode(self):
        super().activateNightMode()
        self.setIntensity(5)
        print("IntensityLight " + str(self.name) + " activated Night Mode")

    def setIntensity(self, intensity):
        super().setIntensity(intensity)
        print("IntensityLight " + self.name + " set to intensity: " + str(intensity))

