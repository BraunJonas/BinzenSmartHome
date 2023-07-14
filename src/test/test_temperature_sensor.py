from sensors.temperature_sensor import TemperatureSensor
import unittest

class TestTemperatureSensor(unittest.TestCase):

    def setUp(self):
        self.temperatureSensor = TemperatureSensor()

    def test_getData(self):
        self.temperatureSensor.setData(30)
        self.assertEqual(self.temperatureSensor.getData(), 30)

    def test_checkEverythingNormal_success(self):
        self.temperatureSensor.setData(27)
        self.assertEqual(self.temperatureSensor.checkEverythingNormal(), True)

    def test_checkEverythingNormal_below_or_equal_minus_5(self):
        self.temperatureSensor.setData(-5)
        self.assertEqual(self.temperatureSensor.checkEverythingNormal(), False)

    def test_checkEverythingNormal_greater_or_equal_40(self):
        self.temperatureSensor.setData(40)
        self.assertEqual(self.temperatureSensor.checkEverythingNormal(), False)

    def test_setdata_success(self):
        self.temperatureSensor.setData(20)
        self.assertEqual(self.temperatureSensor.getData(), 20)

    def test_setdata_greater_55(self):
        self.temperatureSensor.setData(120)
        self.assertEqual(self.temperatureSensor.getData(), 0)

    def test_setdata_below_minus_10(self):
        self.temperatureSensor.setData(-15)
        self.assertEqual(self.temperatureSensor.getData(), 0)

        