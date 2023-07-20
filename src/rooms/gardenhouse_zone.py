from src.devices.standard_devices.fertilize_device import FertilizeDevice
from src.devices.sensor_devices.humidity_device import HumidityDevice
from src.devices.standard_devices.lights import IntensityLight
from src.devices.sensor_devices.shadowing_device import ShadowingDevice
from src.devices.sensor_devices.temperature_device import TemperatureDevice
from src.devices.standard_devices.watering_device import WateringDeviceDrops, WateringDeviceGround, WateringDevice
from src.communication_to_external_systems.ki_adapter import getPflegeHinweis, KIError
from src.rooms.zone import Zone


class GardenhouseZone (Zone):
    
    def __init__(self, name: str):
        self.name = name
        super().__init__(name)
        self.logger.info("Gardenhousezone " + name + " has been created")
        #Devices Adden

    def askKI(self):
        try:
            code = getPflegeHinweis("Bild")
            self.logger.info("Gardenhousezone " + self.name + " got code "+ code +" from KI")
            match code:
                case "001":
                    self.changeAmount(0.5, WateringDevice)
                case "002":
                    self.changeAmount(-0.5, WateringDevice)
                case "010":
                    self.changeAmount(-0.5, FertilizeDevice)
                case "020":
                    self.changePercentage(10, HumidityDevice)
                case "021":
                    self.changePercentage(-10, HumidityDevice)
                case "030":
                    self.changePercentage(10, ShadowingDevice)
                    self.changePercentage(10, IntensityLight)

                case "031":
                    self.changePercentage(-10, ShadowingDevice)
                    self.changePercentage(-10, IntensityLight)

                case _:
                    self.logger.warning("Gardenhousezone " + self.name + " got an unknown code")
        except KIError:
            self.logger.warning("Gardenhousezone " + self.name + " wasn't able to communicate with KI")



