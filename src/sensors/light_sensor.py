from random import randint
from numpy import number
from .sensor import Sensor

class LightSensor(Sensor):

    def getData(self) -> number:
        return self.data
    
    def checkEverythingNormal(self) -> bool:
        if ( self.getData() > 10 and self.getData() < 90 ):
            return True
        else:
            return False
    
    def setData(self, data):
        if(data <= 100 & data >= 0):
            self.data = data
        else:
            self.data = 0
    
    def setRandomData(self):
        self.data = randint(0,100)

