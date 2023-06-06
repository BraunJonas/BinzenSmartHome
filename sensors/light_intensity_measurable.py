from abc import ABC, abstractmethod
from random import randint

from numpy import number
from sensor import Sensor

class LightIntensityMeasurable(Sensor):

    def measureLightInensity(self) -> number:
        return randint(0,100)
    
    def checkEverythingNormal(self) -> bool:
        if ( self.measureLightInensity() > 10 and self.measureLightInensity() < 90 ):
            return True
        else:
            return False

