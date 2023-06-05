from devices.cooling_device import CoolingDevice
from devices.lights import Light
from rooms.room import Room
from devices.lights import IntensityLight
from devices.multimedia_devices import Tv
from devices.window import Window
from devices.door import Door

if __name__ == "__main__":
    room = Room("Raum1")
    room.addDevice(Light("Licht"))
    light=room.getDevices()[0]
    print(light.getName())
    light.setRunning(True)
    print(light.isRunning())
    if (light.checkEverythingNormal == False):
        print(light.measureLightInensity)
    light.activateNightMode()

    room.addDevice(IntensityLight("IntensityLight"))
    light=room.getDevices()[1]
    print(light.getName())
    light.setRunning(True)
    print(light.isRunning())
    if (light.checkEverythingNormal == False):
        print(light.measureLightInensity)
    light.activateNightMode()
    try:
        light.setIntencity(10)
    except:
        print("Not possible")
    try:
        light.setIntencity(110)
    except:
        print("Not possible")

    
    room.addDevice(Tv("Tv"))
    tv=room.getDevices()[2]
    print(tv.getName())
    tv.setRunning(True)
    print(tv.isRunning())
    tv.playVideo()
    tv.playAudio()
    tv.activateNightMode()
    try:
        light.setIntencity(10)
    except:
        print("Not possible")
    try:
        light.setIntencity(110)
    except:
        print("Not possible")
    tv.playVideo()
    tv.playAudio()


    room.addDevice(Window("Tv"))
    window=room.getDevices()[3]
    print(window.getName())
    window.setOpen(True)
    print(window.isOpen())
    window.activateNightMode()
    if (window.checkEverythingNormal == False):
        print(window.measureTemperature())

    room.addDevice(Door("Tv"))
    door=room.getDevices()[4]
    print(door.getName())
    door.setOpen(True)
    print(door.isOpen())
    door.activateNightMode()

    room.addDevice(CoolingDevice("Cool"))
    cool=room.getDevices()[5]
    print(cool.getName())
    
    try:
        cool.setTemperature(10)
    except:
        print("Not possible")

    try:
        cool.setTemperature(111)
    except:
        print("Not possible")
    
    cool.activateNightMode()
