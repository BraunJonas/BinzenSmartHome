from rooms.gardenhouse_zone import GardenhouseZone
from actors.percentage_adjustable import PercentageAdjustable
from actors.temperature_adjustable import TemperatureAdjustable
from actors.amount_adjustable import AmountAdjustable
from actors.open_closeable import OpenCloseable
from actors.switch_on_offable import SwitchOnOffable

from devices.standard_devices.window import Window
from devices.standard_devices.lights import Light, IntensityLight
from devices.standard_devices.fertilize_device import FertilizeDevice
from devices.sensor_devices.humidity_device import HumidityDevice
from devices.sensor_devices.shadowing_device import ShadowingDevice
from devices.standard_devices.door import Door
from devices.standard_devices.multimedia_devices import AudioDevice, Tv
from rooms.zone_prototype_register import ZonePrototypeRegister
from devices.sensor_devices.rain_barrel_device import RainBarrel
from devices.sensor_devices.temperature_device import TemperatureDevice
from devices.standard_devices.frost_heating import FrostHeating
from devices.standard_devices.watering_device import WateringDeviceGround, WateringDeviceDrops
from rooms.zone import Zone

class Controller():
    __zones = []
    __rainbarrel = RainBarrel.getInstance()
    __frostheating = FrostHeating.getInstance()
    #Alle Devices außer RainBarrel und Frostheating hinzufügen (RainBarrel und Frostheating sind zonenübergreifend)
    __deviceOptions = ["TemperatureDevice", "HumidityDevice", "ShadowingDevice", "Tv", "Door","FertilizeDevice", "AudioDevice", "Light", "IntensityLight", "WateringDeviceDrops", "WateringDeviceGround", "Window"]
    
    #Aufsetzen der Prototypes
    @staticmethod
    def setUpPrototypeZones():

        z = GardenhouseZone("CompleteGardenPrototype")
        z.addDevice(WateringDeviceDrops("Name"))
        z.addDevice(WateringDeviceGround("Name"))
        z.addDevice(TemperatureDevice("Name"))
        z.addDevice(HumidityDevice("Name"))
        z.addDevice(ShadowingDevice("Name"))
        z.addDevice(FertilizeDevice("Name"))
        z.addDevice(Window("Name"))
        z.addDevice(Light("Name"))
        z.addDevice(IntensityLight("Name"))
        z.addDevice(Door("Name"))
        ZonePrototypeRegister.addPrototype(z, z.getName())

        z = GardenhouseZone("TropicalGardenPrototype")
        z.addDevice(WateringDeviceDrops("Name"))
        z.addDevice(TemperatureDevice("Name"))
        z.addDevice(HumidityDevice("Name"))
        z.addDevice(Light("Name"))
        z.addDevice(Door("Name"))
        z.addDevice(Window("Name"))
        ZonePrototypeRegister.addPrototype(z, z.getName())

        z = GardenhouseZone("MusicGardenPrototype")
        z.addDevice(WateringDeviceGround("Name"))
        z.addDevice(TemperatureDevice("Name"))
        z.addDevice(IntensityLight("Name"))
        z.addDevice(AudioDevice("Name"))
        z.addDevice(Door("Name"))
        z.addDevice(Window("Name"))
        ZonePrototypeRegister.addPrototype(z, z.getName())

        z = Zone("CompleteHomePrototype")
        z.addDevice(Tv("Name"))
        z.addDevice(AudioDevice("Name"))
        z.addDevice(Window("Name"))
        z.addDevice(Light("Name"))
        z.addDevice(IntensityLight("Name"))
        z.addDevice(Door("Name"))
        ZonePrototypeRegister.addPrototype(z, z.getName())

        z = Zone("BasicHomePrototype")
        z.addDevice(Door("Name"))
        z.addDevice(Window("Name"))
        z.addDevice(Light("Name"))
        ZonePrototypeRegister.addPrototype(z, z.getName())

        z = Zone("GamingHomePrototype")
        z.addDevice(Door("Name"))
        z.addDevice(Tv("Name"))
        z.addDevice(AudioDevice("Name"))
        z.addDevice(IntensityLight("Name"))
        ZonePrototypeRegister.addPrototype(z, z.getName())


    #setup des Controllers
    @staticmethod
    def setUp():
        Controller.setUpPrototypeZones()

    @staticmethod
    def simuliereEinenThreadDurchlauf():
        Controller.__frostheating.simuliereEinenThreadDurchlauf()
        Controller.__rainbarrel.simuliereEinenThreadDurchlauf()
        for z in Controller.__zones:
            z.simuliereEinenThreadDurchlauf()

    #Rückgabe der Zonen
    @staticmethod
    def getZones():
        return Controller.__zones

    #Rückgabe der Devices
    @staticmethod
    def getDevices(zone: int):
        return Controller.__zones[zone].getDevices()

    #Hinzufügen von Zonen
    @staticmethod
    def addZone(zone: Zone):
        Controller.__zones.append(zone)

    #Rückgabe der Device Options Array
    @staticmethod
    def getDeviceOptions():
        return Controller.__deviceOptions

    @staticmethod
    def addDevice(zone: int, device: str, name: str):
        ##Alle devices aufnehmen
        match device:
            case "TemperatureDevice":
                Controller.__zones[zone].addDevice(TemperatureDevice(name))
            case "HumidityDevice":
                Controller.__zones[zone].addDevice(HumidityDevice(name))
            case "ShadowingDevice":
                Controller.__zones[zone].addDevice(ShadowingDevice(name))
            case "Tv":
                Controller.__zones[zone].addDevice(Tv(name))
            case "Door":
                Controller.__zones[zone].addDevice(Door(name))
            case "FertilizeDevice":
                Controller.__zones[zone].addDevice(FertilizeDevice(name))
            case "AudioDevice":
                Controller.__zones[zone].addDevice(AudioDevice(name))
            case "Light":
                Controller.__zones[zone].addDevice(Light(name))
            case "IntensityLight":
                Controller.__zones[zone].addDevice(IntensityLight(name))
            case "WateringDeviceDrops":
                Controller.__zones[zone].addDevice(WateringDeviceDrops(name))
            case "WateringDeviceGround":
                Controller.__zones[zone].addDevice(WateringDeviceGround(name))
            case "Window":
                Controller.__zones[zone].addDevice(Window(name))

    #Abänderung der Werte der jeweiligen Device und Typevaluierung
    @staticmethod
    def getChangeOptions(zone: int, device: int):
        device = Controller.__zones[zone].getDevices()[device]
        options = []
        if isinstance(device, PercentageAdjustable):
            options.append((0,"Ändere Prozentualer Wert: aktueller Wert: "+str(device.getPercentage())))
        if isinstance(device, TemperatureAdjustable):
            options.append((1,"Ändere Temperatur Wert: aktueller Wert: "+str(device.getTemperature())))
        if isinstance(device, AmountAdjustable):
            options.append((2,"Ändere Mengen Wert: aktueller Wert: "+str(device.getAmount())))
        if isinstance(device, OpenCloseable):
            options.append((3,"Ändere Open Wert: aktueller Wert: "+str(device.isOpen())))
        if isinstance(device, SwitchOnOffable):
            options.append((4,"Ändere Running Wert: aktueller Wert: "+str(device.isRunning())))
        if isinstance(device, Door):
            options.append((5,"Ändere Locked Wert: aktueller Wert: "+str(device.isLocked())))
        if isinstance(device, AudioDevice):
            options.append((6, "Ändere ReactToAlarms Wert: aktueller Wert: "+str(device.getReactToAlarms())))
            options.append((7,"Spiele AudioDatei"))
        if isinstance(device, Tv):
            options.append((8,"Spiele VideoDatei"))
        options.append((9, "Ändere den Namen"))
        options.append((10, "Lösche Device"))
        return options

    #Attributsumkehrfunktion true->flase false->true
    @staticmethod
    def invertOpen(zone, device):
        d = Controller.__zones[zone].getDevices()[device]
        d.setOpen(not d.isOpen())
    
    #Attributsumkehrfunktion true->flase false->true
    @staticmethod
    def invertRunning(zone, device):
        d = Controller.__zones[zone].getDevices()[device]
        d.setRunning(not d.isRunning())

    #Attributsumkehrfunktion true->flase false->true
    @staticmethod
    def invertLocked(zone, device):
        d = Controller.__zones[zone].getDevices()[device]
        d.setLocked(not d.isLocked())

    @staticmethod
    def changePercentage(zone, device, number):
        d = Controller.__zones[zone].getDevices()[device]
        d.setPercentage(number)

    @staticmethod
    def changeTemp(zone, device, number):
        d = Controller.__zones[zone].getDevices()[device]
        d.setTemperature(number)

    @staticmethod
    def changeAmount(zone, device, number):
        d = Controller.__zones[zone].getDevices()[device]
        d.setAmount(number)

    @staticmethod
    def changeAudio(zone, device, eingabe):
        d = Controller.__zones[zone].getDevices()[device]
        d.playAudio(eingabe)

    @staticmethod
    def changeVideo(zone, device, eingabe):
        d = Controller.__zones[zone].getDevices()[device]
        d.playVideo(eingabe)

    @staticmethod
    def invertReactToAlarms(zone, device):
        d = Controller.__zones[zone].getDevices()[device]
        d.setReactToAlarms(not d.getReactToAlarms())

    #Löschen der Device aus der Zone
    @staticmethod
    def deleteDevice(zone, device):
        d = Controller.__zones[zone].getDevices()[device]
        Controller.__zones[zone].removeDevice(d)
    
    @staticmethod
    def changeName(zone, device, eingabe):
        d = Controller.__zones[zone].getDevices()[device]
        d.setName(eingabe)

