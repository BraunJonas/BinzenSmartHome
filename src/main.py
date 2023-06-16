from devices.multimedia_devices import AudioDevice
from rooms.room import Room
from sensors.temperature_sensor import TemperatureSensor
from devices.temperature_device import TemeratureDevice

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
    rooms = setupRooms()
    for room in rooms:
        for device in room.getDevices():
            device.simuliereEinenThreadDurchlauf()

