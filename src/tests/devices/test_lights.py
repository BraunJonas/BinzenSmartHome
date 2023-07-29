import unittest
from devices.standard_devices.lights import IntensityLight
from devices.standard_devices.lights import Light


class TestLight(unittest.TestCase):

    def setUp(self):
        self.light = Light("Glühbirne")

    def test_setRunning(self):
        self.light.setRunning(True)
        self.assertEqual(self.light.isRunning(), True)
    
    def test_isRunning(self):
        self.light.setRunning(False)
        self.assertEqual(self.light.isRunning(), False)

class TestIntensityLight(unittest.TestCase):

    def setUp(self):
        self.intensityLight = IntensityLight("Intense Glühbirne")

    def test_setRunning(self):
        self.intensityLight.setRunning(True)
        self.assertEqual(self.intensityLight.isRunning(), True)
    
    def test_isRunning(self):
        self.intensityLight.setRunning(False)
        self.assertEqual(self.intensityLight.isRunning(), False)