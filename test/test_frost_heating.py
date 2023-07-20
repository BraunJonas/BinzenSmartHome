import unittest
from devices.frost_heating import FrostHeating


class TestFrostHeating():

    # because of singleton building object is impossible
    def setUp(self):
        self.frostHeating = FrostHeating()

    def test_setRunning(self):
        self.frostHeating.setRunning(True) 
        self.assertEqual(self.frostHeating.isRunning(), True)
    
    def test_isRunning(self):
        self.frostHeating.setRunning(False)
        self.assertEqual(self.frostHeating.isRunning(), False)