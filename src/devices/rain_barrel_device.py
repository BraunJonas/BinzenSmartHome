from devices.device import Device
from devices.event_manager import EventManager
from sensors.water_level_sensor import WaterLevelSensor
import logging
class RainBarrel(Device):
    __instance = None
     #Singleton

    def __init__(self ):
        if RainBarrel.__instance != None:
            raise Exception("This is a Singleton class")
        super().__init__("RainBarrel")
        self.logger = logging.getLogger(__name__)
        self.enoughWater = True
        RainBarrel.__instance = self

    @staticmethod
    def getInstance():
        logger = logging.getLogger(__name__)
        if RainBarrel.__instance == None:
            logger.info("Creating new RainBarrel instance")
            RainBarrel()
        else:
            logger.info("Instance already existed: returning instance")
        return RainBarrel.__instance
    
    
    def setSensor(self, sensor: WaterLevelSensor):
        self.sensor = sensor

    def decideEnoughWater(self):
        if(self.sensor.checkEverythingNormal()):
            return True
        #ask weather station for rain update
        #if ... berechnen
        # return true
        return False
    
    def simuliereEinenThreadDurchlauf(self):
        self.sensor.setRandomData()
        enoughWaterNew = self.decideEnoughWater()
        if enoughWaterNew:
            self.logger.info("RainBarrel is full - no Water Saving necessary" )
            if (not self.enoughWater == enoughWaterNew):
                EventManager.notify("water", "Enough Water")
        else:
            self.logger.warning("RainBarrel is almost empty - Water Saving necessary" )
            EventManager.notify("alarm", "RainBarrel is almost empty - Water Saving necessary")
            if (not self.enoughWater == enoughWaterNew):
                EventManager.notify("water", "Not enough Water")
        
        self.enoughWater = enoughWaterNew

    


        