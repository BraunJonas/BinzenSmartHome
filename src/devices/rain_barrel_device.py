from devices.device import Device
from devices.water_event_manager import WaterEventManager
from sensors.water_level_sensor import WaterLevelSensor

class RainBarrel(Device):
    __instance = None
     #Singleton

    def __init__(self ):
        if RainBarrel.__instance != None:
            raise Exception("This is a Singleton class")
        super().__init__("RainBarrel")
        self.enoughWater = True
        RainBarrel.__instance = self

    @staticmethod
    def getInstance():
        if RainBarrel.__instance == None:
            print("Creating new RainBarrel instance")
            RainBarrel()
        else:
            print("Instance already existed: returning instance")
        return RainBarrel.__instance
    
    @staticmethod
    def setSensor(sensor: WaterLevelSensor):
        RainBarrel.__instance.sensor = sensor

    def decideEnoughWater(self):
        if(self.sensor.checkEverythingNormal()):
            return True
        #ask weather station for rain update
        #if ... berechnen
        # return true
        return False
    
    def simuliereEinenThreadDurchlauf(self):
        print(self.enoughWater)
        enoughWaterNew = self.decideEnoughWater()
        if enoughWaterNew:
            print(f"RainBarrel is full - no Water Saving necessary" )
        else:
            print(f"RainBarrel is almost empty - Water Saving necessary" )
        if (not self.enoughWater == enoughWaterNew):
            WaterEventManager.notify(enoughWaterNew)
        self.enoughWater = enoughWaterNew

    


        