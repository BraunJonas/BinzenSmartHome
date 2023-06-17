from random import randint
from .sensor import Sensor

class WaterLevelSensor(Sensor):

    def getData(self) -> int:
        return randint(0,100)
    
    def checkEverythingNormal(self) -> bool:
        if ( self.getData() > 40 ):
            return True
        else:
            return False
