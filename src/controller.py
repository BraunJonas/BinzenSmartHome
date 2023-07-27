from rooms.gardenhouse_zone import GardenhouseZone
from src.actors.percentage_adjustable import PercentageAdjustable
from src.actors.temperature_adjustable import TemperatureAdjustable
from src.actors.amount_adjustable import AmountAdjustable
from src.actors.open_closeable import OpenCloseable
from src.actors.switch_on_offable import SwitchOnOffable

from src.devices.sensor_devices.humidity_device import HumidityDevice
from src.devices.sensor_devices.shadowing_device import ShadowingDevice
from src.devices.standard_devices.door import Door
from src.devices.standard_devices.multimedia_devices import AudioDevice, Tv
from src.rooms.zone_prototype_register import ZonePrototypeRegister
from src.devices.sensor_devices.rain_barrel_device import RainBarrel
from src.devices.sensor_devices.temperature_device import TemperatureDevice
from src.devices.standard_devices.frost_heating import FrostHeating
from src.devices.standard_devices.watering_device import WateringDeviceDrops
from src.rooms.zone import Zone

class Controller():
    __zones = []
    __rainbarrel = RainBarrel.getInstance()
    __frostheating = FrostHeating.getInstance()
    #Alle Devices außer RainBarrel und Frostheating hinzufügen (aufpassen in Lights/ Audio File sind mehrere Devices) -> SensorDevice und Device sind abstrakt!
    __deviceOptions = ["TemperatureDevice", "HumidityDevice", "ShadowingDevice", "Tv", "Door"]
    @staticmethod
    def setUpPrototypeZones():
        z = GardenhouseZone("TropicalPrototype")
        z.addDevice(WateringDeviceDrops("Name"))
        z.addDevice(TemperatureDevice("Name"))
        ZonePrototypeRegister.addPrototype(z, z.getName())

    @staticmethod
    def setUp():
        Controller.setUpPrototypeZones()

    @staticmethod
    def simuliereEinenThreadDurchlauf():
        Controller.__frostheating.simuliereEinenThreadDurchlauf()
        Controller.__rainbarrel.simuliereEinenThreadDurchlauf()
        for z in Controller.__zones:
            z.simuliereEinenThreadDurchlauf()

    @staticmethod
    def getZones():
        return Controller.__zones

    @staticmethod
    def getDevices(zone: int):
        return Controller.__zones[zone].getDevices()

    @staticmethod
    def addZone(zone: Zone):
        Controller.__zones.append(zone)

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

    @staticmethod
    def invertOpen(zone, device):
        d = Controller.__zones[zone].getDevices()[device]
        d.setOpen(not d.isOpen())
    @staticmethod
    def invertRunning(zone, device):
        d = Controller.__zones[zone].getDevices()[device]
        d.setRunning(not d.isRunning())

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

    @staticmethod
    def deleteDevice(zone, device):
        d = Controller.__zones[zone].getDevices()[device]
        Controller.__zones[zone].removeDevice(d)
    @staticmethod
    def changeName(zone, device, eingabe):
        d = Controller.__zones[zone].getDevices()[device]
        d.setName(eingabe)

