from random import randint
from .sensor import Sensor

class TemperatureSensor(Sensor):

    def getData(self) -> int:
        return self.data
    
    def checkEverythingNormal(self) -> bool:
        if ( self.getData() > -5 and self.getData() < 40 ):
            return True
        else:
            return False
    
    def setData(self, data):
        if(data >= -10 and data <= 55):
            self.data = data
        else:
            self.data = 0
    
    def setRandomData(self):
        self.data = randint(-10,55)

