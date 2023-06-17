from random import randint
from .sensor import Sensor

class TemperatureSensor(Sensor):

    def getData(self) -> int:
        return randint(-10,55)
    
    def checkEverythingNormal(self) -> bool:
        if ( self.getData() > -5 and self.measureTemperature() < 40 ):
            return True
        else:
            return False

