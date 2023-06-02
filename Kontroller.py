from Light import Light
from Room import Room
from IntensityLight import IntensityLight

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