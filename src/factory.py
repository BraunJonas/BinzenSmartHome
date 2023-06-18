from src.devices.fertilize_device import FertilizeDevice
from src.devices.lights import IntensityLight
from src.devices.shadowing_device import ShadowingDevice
from src.devices.temperature_device import TemeratureDevice
from src.devices.watering_device import WateringDeviceDrops, WateringDeviceGround
from src.rooms.room import Room
from src.sensors.light_sensor import LightSensor
from src.sensors.temperature_sensor import TemperatureSensor


class factory:
    def create_device(self, device_type: str, name: str):
        if (device_type == "Gartenhauszone"):
            gartenzone = Room("Gartenhauszone" + name)
            
            tempreatureSensor = TemperatureSensor()
            lightSensor = LightSensor()
            
            tempDevice = TemeratureDevice("temperatursensor Zone: " + name, tempreatureSensor)
            fertilizeDevice = FertilizeDevice("fertilize Device Zone: " + name)
            shadowingDevice = ShadowingDevice("shadow Device Zone: "+name, lightSensor)
            wateringDeviceGround =  WateringDeviceGround("Watering Device Ground Zone: "+name)
            wateringDeviceDrop =  WateringDeviceDrops("Watering Device Drop Zone: "+name)
            intensityLight = IntensityLight("Intensity Light Zone: "+name)
            
            gartenzone.addDevice(tempreatureSensor)
            gartenzone.addDevice(lightSensor)
            
            gartenzone.addDevice(tempDevice)
            gartenzone.addDevice(fertilizeDevice)
            gartenzone.addDevice(shadowingDevice)
            gartenzone.addDevice(wateringDeviceGround)
            gartenzone.addDevice(wateringDeviceDrop)
            gartenzone.addDevice(intensityLight)
            
            return gartenzone
