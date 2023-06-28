import time
from devices.multimedia_devices import AudioDevice
from devices.rain_barrel_device import RainBarrel
from devices.watering_device import WateringDeviceGround
from devices.watering_strategy import WateringStrategySaveUp
from rooms.room import Room
from devices.multimedia_devices import Tv
from sensors.temperature_sensor import TemperatureSensor
from devices.temperature_device import TemeratureDevice
from sensors.water_level_sensor import WaterLevelSensor
from devices.door import Door
import logging
import datetime


# ADP - Es gibt keine Zyklen in der Abhängigkeitsstruktur des gesamten Codes

def setupRooms():
    #Factory und oder Prototyping einsetzen
    # add rooms
    rooms = []
    rooms.append(Room("Küche"))
    rooms.append(Room("Schlafzimmer"))
    rooms.append(Room("Wohnzimmer"))
    audio = AudioDevice("AudioDevice")
    rooms[0].addDevice(audio)
    tempsens = TemperatureSensor()
    tempdev = TemeratureDevice("TEMP",tempsens)
    rooms[0].addDevice(tempdev)

    return rooms


if __name__ == "__main__":

    #TODO
    #Räume und Zonen -> Klassen erstellen
    #Factory für Devices 
    #Adapter Schnittstelle für KI und Wetterstation
    #Observer für Alarme? / Mediator

    # frost = FrostHeating.getInstance()
    # frost.setRunning(True)

    # frost2 = FrostHeating.getInstance()
    # print(frost2.isRunning())
    # print(frost.isRunning())


    logging.basicConfig(filename="SmartHomeLog.log", encoding="utf-8", level=logging.DEBUG)
    logger = logging.getLogger()
    logger.info(10*"-" + str(datetime.datetime.now()) + 75*"-")
    door = Door("Tür")
    door.setOpen(True)
    tv = Tv("tv")
    groundWater = WateringDeviceGround("WATER")
    groundWater.setWateringStrategy((WateringStrategySaveUp()))
    
    sensor = WaterLevelSensor()
    rainbarrel = RainBarrel.getInstance()
    rainbarrel.setSensor(sensor)

    audio = AudioDevice("AUDIO")
    audio.setReactToAlarms(True)
    tempsens = TemperatureSensor()
    temp = TemeratureDevice("Temperaturdevice", tempsens)

    while(True):
        logger.info(10*"-" + "NEW SIMULATION" + 75*"-")
        rainbarrel.simuliereEinenThreadDurchlauf()
        groundWater.simuliereEinenThreadDurchlauf()
        temp.simuliereEinenThreadDurchlauf()
        time.sleep(3)
    #for room in rooms:
        #for device in room.getDevices():
            #device.simuliereEinenThreadDurchlauf()

