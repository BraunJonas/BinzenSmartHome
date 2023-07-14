from  devices.device import Device
import unittest

class TestDevice(unittest.TestCase):

    def setUp(self):
        self.device = Device("Basisgerät")

    def test_getName(self):
        self.device.setName("Gerät")
        self.assertEqual(self.device.getName(), "Gerät")

    def test_setName(self):
        self.device.setName("Kühlschrank")
        self.assertEqual(self.device.getName(), "Kühlschrank")

   