from Heating import CoolingDevice
from Light import Light
from Room import Room
from Light import IntensityLight
from Entertainment import Tv
from Door import Window
from Door import Door

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
