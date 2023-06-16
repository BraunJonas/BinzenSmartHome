from random import randint
from numpy import number
from .sensor import Sensor

class LightSensor(Sensor):

    def getData(self) -> number:
        return randint(0,100)
    
    def checkEverythingNormal(self) -> bool:
        if ( self.getData() > 10 and self.getData() < 90 ):
            return True
        else:
            return False

