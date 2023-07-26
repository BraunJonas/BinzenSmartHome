import logging
import src.communication_to_external_systems.weatherstation_adapter
from src.devices.device import Device
from src.devices.device_communication.event_manager import EventManager
from src.sensors.water_level_sensor import WaterLevelSensor


class RainBarrel(Device):
    __instance = None
     #Singleton

    def __init__(self ):
        if RainBarrel.__instance != None:
            raise Exception("This is a Singleton class")
        super().__init__("RainBarrel")
        self.logger = logging.getLogger(__name__)
        self.enoughWater = True
        self.maxAmount = 75
        self.sensor = WaterLevelSensor()
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
        #Ask Sensor if enough water is 
        #if(self.sensor.checkEverythingNormal()):
            #return True
        #else:
        amount = self.sensor.getData() * self.maxAmount /100
        expected = src.communication_to_external_systems.weatherstation_adapter.getExpectedRainAmount()
        self.logger.info(f"RainBarrel {self.name}= {amount}l"  )

        self.logger.info(f"RainBarrel {self.name} got Info: Expected RainAmount = {expected}l"  )
        if(amount + expected > 45):
            return True
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

    


        