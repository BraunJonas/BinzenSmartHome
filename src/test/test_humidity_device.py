from devices.humidity_device import HumidityDevice
from sensors.humidity_sensor import HumiditySensor
import unittest

class TestHumidityDevice(unittest.TestCase):

    def setUp(self):
        self.humiditySensor = HumiditySensor()
        self.humidityDevice = HumidityDevice("Heißmacher", self.humiditySensor)

    def test_getPercentage(self):
        self.humidityDevice.setPercentage(30)
        self.assertEqual(self.humidityDevice.getPercentage(), 30)
    
    def test_setPercentage(self):
        self.humidityDevice.setPercentage(60)
        self.assertEqual(self.humidityDevice.getPercentage(), 60)