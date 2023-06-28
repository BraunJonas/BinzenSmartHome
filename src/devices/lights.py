from .device import Device 
from actors.switch_on_offable import SwitchOnOffable
from actors.percentage_adjustable import PercentageAdjustable

# CCP - Light und IntensityLight sind geschlossen gegenüber der selben Art von Veränderungen und sind deshalb in einem Modul zusammengefasst

class Light(Device, SwitchOnOffable):
    def __init__(self, name: str):
        print("Light " + name + " has been created")
        super().__init__(name)
        self.running = False


    def setRunning(self, running: bool):
        self.running = running
        print("Light " + str(self.name) + "changed running to " + str(running))

    def isRunning(self) -> bool:
        return self.running
    
    def simuliereEinenThreadDurchlauf(self):
        print(f"Light {self.name} is {'running' if self.running else 'not running'}" )

    

#LSP - Austauschbarkeit der Klassen: IntensityLight kann anstelle von Light verwendet werden, ohne die Funktionalität zu beeinträchtigen

class IntensityLight(PercentageAdjustable, Light):
    
    def __init__(self, name: str):
        print("IntensityLight " + name + " has been created")
        super().__init__(name)
        self.insensity = 50

    def setPercentage(self, percentage: int):
        self.insensity = percentage
        print("IntensityLight " + self.name + " set to intensity: " + str(percentage))

    def getPercentage(self) -> bool:
        return self.insensity
    
    def simuliereEinenThreadDurchlauf(self):
        print(f"IntensityLight {self.name} is {'running' if self.running else 'not running'} with intensity {self.intesity}" )



