from abc import ABC, abstractmethod
from random import randint

from numpy import number
from Sensor import Sensor


class LightIntensityMeasureAble(Sensor):
    def measureLightIntensity(self) -> number:
        return randint(0, 100)

    def checkEverythingNormal(self) -> bool:
        if self.measureLightIntensity() > 10 and self.measureLightIntensity() < 90:
            return True
        else:
            return False
