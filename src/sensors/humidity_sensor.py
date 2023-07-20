from random import randint

from .sensor import Sensor


class HumiditySensor(Sensor):

    def getData(self) -> int:
        return self.data
    
    def checkEverythingNormal(self) -> bool:
        if ( self.getData() > 30 and self.getData() < 70 ):
            return True
        else:
            return False
    
    def setData(self, data: int):
        if(data <= 100 and data >= 0):
            self.data = data
        else:
            self.data = 0
    
    def setRandomData(self):
        self.data = randint(0,100)