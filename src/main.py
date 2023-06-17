import time
from devices.multimedia_devices import AudioDevice
from devices.rain_barrel_device import RainBarrel
from devices.watering_device import WateringDeviceGround
from devices.watering_strategy import WateringStrategySaveUp
from rooms.room import Room
from sensors.temperature_sensor import TemperatureSensor
from devices.temperature_device import TemeratureDevice
from devices.frost_heating import FrostHeating
from sensors.water_level_sensor import WaterLevelSensor


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

    groundWater = WateringDeviceGround("WATER")
    groundWater.setWateringStrategy((WateringStrategySaveUp()))
    
    sensor = WaterLevelSensor()
    rainbarrel = RainBarrel.getInstance()
    RainBarrel.setSensor(sensor)

    while(True):
        rainbarrel.simuliereEinenThreadDurchlauf()
        groundWater.simuliereEinenThreadDurchlauf()
        time.sleep(3)
    #for room in rooms:
        #for device in room.getDevices():
            #device.simuliereEinenThreadDurchlauf()

