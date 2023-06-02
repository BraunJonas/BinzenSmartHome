from random import randint

from Sensor import Sensor

class TemperatureMeasureAble(Sensor):

    def measureTemperature(self) -> int:
        return randint(-10,55)
    
    def checkEverythingNormal(self) -> bool:
        if ( self.measureTemperature() > -5 and self.measureTemperature() < 40 ):
            return True
        else:
            return False