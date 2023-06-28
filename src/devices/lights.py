from .device import Device 
from actors.switch_on_offable import SwitchOnOffable
from actors.percentage_adjustable import PercentageAdjustable
import logging
# CCP - Light und IntensityLight sind geschlossen gegenüber der selben Art von Veränderungen und sind deshalb in einem Modul zusammengefasst

class Light(Device, SwitchOnOffable):
    def __init__(self, name: str):
        super().__init__(name)
        self.logger = logging.getLogger(__name__)
        self.logger.info("Light " + name + " has been created")
        self.running = False


    def setRunning(self, running: bool):
        self.running = running
        self.logger.info("Light " + str(self.name) + "changed running to " + str(running))

    def isRunning(self) -> bool:
        return self.running
    
    def simuliereEinenThreadDurchlauf(self):
        self.logger.info(f"Light {self.name} is {'running' if self.running else 'not running'}" )

    

#LSP - Austauschbarkeit der Klassen: IntensityLight kann anstelle von Light verwendet werden, ohne die Funktionalität zu beeinträchtigen

class IntensityLight(PercentageAdjustable, Light):
    
    def __init__(self, name: str):
        super().__init__(name)
        self.logger.info("IntensityLight " + name + " has been created")
        self.insensity = 50

    def setPercentage(self, percentage: int):
        self.insensity = percentage
        self.logger.info("IntensityLight " + self.name + " set to intensity: " + str(percentage))

    def getPercentage(self) -> bool:
        return self.insensity
    
    def simuliereEinenThreadDurchlauf(self):
        self.logger.info(f"IntensityLight {self.name} is {'running' if self.running else 'not running'} with intensity {self.intesity}" )



