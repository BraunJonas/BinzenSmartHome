import unittest
from devices.standard_devices.fertilize_device import FertilizeDevice


class TestFertilizeDevice(unittest.TestCase):

    def setUp(self):
        self.fertilizeDevice = FertilizeDevice("Dünger")

    def test_setAmount(self):
        self.fertilizeDevice.setAmount(20.22)
        self.assertEqual(self.fertilizeDevice.getAmount(), 20.22)

    def test_getAmount(self):
        self.fertilizeDevice.setAmount(40.22)
        self.assertEqual(self.fertilizeDevice.getAmount(), 40.22)

    def test_simuliereEinenThreadDurchlauf(self):
        self.fertilizeDevice.setAmount(10.05)
        self.logMessage = f"FertilizeDevice {self.fertilizeDevice.name} is fertilizing " + str(10.05) + "g per day"
        with self.assertLogs() as log:
            self.fertilizeDevice.simuliereEinenThreadDurchlauf()
        self.assertEqual(len(log.records), 1)
        self.assertEqual(log.records[0].getMessage(), self.logMessage)

