from random import randint
from numpy import number
from .sensor import Sensor

class HumiditySensor(Sensor):

    def getData(self) -> number:
        return randint(0,100)
    
    def checkEverythingNormal(self) -> bool:
        if ( self.getData() > 30 and self.getData() < 70 ):
            return True
        else:
            return False