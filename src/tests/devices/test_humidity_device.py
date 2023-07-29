import unittest
from devices.sensor_devices.humidity_device import HumidityDevice
from sensors.humidity_sensor import HumiditySensor


class TestHumidityDevice(unittest.TestCase):

    def setUp(self):
        self.humiditySensor = HumiditySensor()
        self.humidityDevice = HumidityDevice("Heißmacher")

    def test_getPercentage(self):
        self.humidityDevice.setPercentage(30)
        self.assertEqual(self.humidityDevice.getPercentage(), 30)
    
    def test_setPercentage(self):
        self.humidityDevice.setPercentage(60)
        self.assertEqual(self.humidityDevice.getPercentage(), 60)
    
    def test_clone(self):
        self.humidityDevice.setPercentage(59)
        cloneDevice = self.humidityDevice.clone("Heißmacher")
        self.assertEqual(cloneDevice.getPercentage(), self.humidityDevice.getPercentage())
        self.assertEqual(cloneDevice.name, self.humidityDevice.name)