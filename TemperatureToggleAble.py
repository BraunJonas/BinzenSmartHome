from Aktor import Aktor

class TemperatureToggleAble(Aktor):
    temp = 0

    def getTemperature(self) -> int:
        return self.temp    
    
    def setTemperature(self, temp:int):
        if ( temp > 40 or temp < 0):
            raise Exception("not possible")
        self.temp = temp

    