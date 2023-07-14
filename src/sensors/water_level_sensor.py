from random import randint
from .sensor import Sensor

class WaterLevelSensor(Sensor):

    def getData(self) -> int:
        return self.data
    
    def checkEverythingNormal(self) -> bool:
        if ( self.getData() > 40 ):
            return True
        else:
            return False
    
    def setData(self, data):
        if(data <= 100 and data >= 0):
            self.data = data
        else:
            self.data = 0
    
    def setRandomData(self):
        self.data = randint(0,100)
