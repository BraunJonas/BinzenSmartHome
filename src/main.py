import datetime
import logging
import time

from src.communication_to_external_systems import ki_adapter
from src.devices.standard_devices.frost_heating import FrostHeating
from src.devices.sensor_devices.rain_barrel_device import RainBarrel
from rooms.gardenhouse_zone import GardenhouseZone
from rooms.zone_prototype_register import ZonePrototypeRegister
from src.devices.standard_devices.watering_device import WateringDeviceDrops
from src.rooms.zone import Zone


# ADP - Es gibt keine Zyklen in der Abhängigkeitsstruktur des gesamten Codes

def setupRooms():
    pass
    #Datei auslesen -> Räume erstellen

   

def setUpLogger():
    logging.basicConfig(filename="SmartHomeLog.log", encoding="utf-8", level=logging.DEBUG)
    logger = logging.getLogger()
    logger.info(10*"-" + str(datetime.datetime.now()) + 75*"-")

#eventuell in zweiter datei laden?
def setUpPrototypeZones():
    z = GardenhouseZone("Zone 1")
    z.addDevice(WateringDeviceDrops())
    ZonePrototypeRegister.addPrototype(z, "normal")


def checkInstance(a, str):
    return isinstance(a,str);


if __name__ == "__main__":

    #setUpLogger()
    #setUpPrototypeZones()
    #z = ZonePrototypeRegister.getPrototype("normal")
    setUpLogger()
    z = GardenhouseZone("Zone 1")
    z.addDevice(WateringDeviceDrops("z"))
    for i in range(0,20):
        z.askKI()
    #while(True):
        #logger.info(10*"-" + "NEW SIMULATION" + 75*"-")
        
   


