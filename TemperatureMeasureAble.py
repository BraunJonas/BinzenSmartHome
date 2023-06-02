import Sensor

class TemperatureMeasureable(Sensor):
    #Abstrct Method Sensor
    def checkEverythingNormal(self):
        print("TemperatureBenceable: everything is normal")
    def measureTemperature(self) -> int:
        pass #int muss zurück logik