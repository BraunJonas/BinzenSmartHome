import unittest
from devices.sensor_devices.shadowing_device import ShadowingDevice

class TestShadowingDevice(unittest.TestCase):

    def setUp(self):
        self.shadowingDevice = ShadowingDevice("Schattenmacher")

    def test_getpercentage(self):
        self.shadowingDevice.target = 40
        self.assertEqual(self.shadowingDevice.getPercentage(), 40)
    
    def test_setpercentage(self):
        self.logMessage = f"ShadowingDevice {self.shadowingDevice.name} set Target to 80"
        with self.assertLogs() as log:
            self.shadowingDevice.setPercentage(80)
        #checks if only one message gets logged
        self.assertEqual(len(log.records), 1)
        self.assertEqual(log.records[0].getMessage(), self.logMessage)
        self.assertEqual(self.shadowingDevice.getPercentage(), 80)
   
    def test_clone(self):
        self.shadowingDevice.setPercentage(70)
        cloneDevice = self.shadowingDevice.clone("Schattenmacher")
        self.assertEqual(cloneDevice.getPercentage(), self.shadowingDevice.getPercentage())
        self.assertEqual(cloneDevice.name, self.shadowingDevice.name)
