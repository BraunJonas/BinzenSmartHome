import logging
from actors.percentage_adjustable import PercentageAdjustable
from actors.switch_on_offable import SwitchOnOffable
from devices.device import Device


# CCP - Light und IntensityLight sind geschlossen gegenüber der selben Art von Veränderungen und sind deshalb in einem Modul zusammengefasst

class Light(Device, SwitchOnOffable):
    def __init__(self, name: str):
        super().__init__("Light: " + name)
        self.logger = logging.getLogger(__name__)
        self.logger.info("Light " + name + " has been created")
        self.running = False

    #Festlegung des zustandes
    def setRunning(self, running: bool):
        self.running = running
        self.logger.info("Light " + str(self.name) + "changed running to " + str(running))

    #Prüfen obe ist das licht an ist
    def isRunning(self) -> bool:
        return self.running
    
    #Simulation eines Durchlaufs -> Main-Klasse
    def simuliereEinenThreadDurchlauf(self):
        self.logger.info(f"Light {self.name} is {'running' if self.running else 'not running'}" )

    #Klonierung des Objektes gemäß Prototype
    def clone(self, name: str):
        clone = Light(name)
        clone.setRunning(self.running)
        return clone


# LSP - Austauschbarkeit der Klassen: IntensityLight kann anstelle von Light verwendet werden, ohne die Funktionalität zu beeinträchtigen

class IntensityLight(PercentageAdjustable, Light):

    def __init__(self, name: str):
        super().__init__("(IntensityLight): " + name)
        self.logger.info("IntensityLight " + name + " has been created")
        self.intesity = 50

    #Festlegung der Lichtitensität
    def setPercentage(self, percentage: int):
        self.intesity = percentage
        self.logger.info("IntensityLight " + self.name + " set to intensity: " + str(percentage))

    #Rückgabe des itensität wertes
    def getPercentage(self) -> int:
        return self.intesity

    #Simulation eines Durchlaufs -> Main-Klasse
    def simuliereEinenThreadDurchlauf(self):
        self.logger.info(
            f"IntensityLight {self.name} is {'running' if self.running else 'not running'} with intensity {self.intesity}")

    #klonieren der device gemäß Prototype
    def clone(self, name: str):
        clone = IntensityLight(name)
        clone.setRunning(self.running)
        clone.setPercentage(self.intesity)
        return clone

