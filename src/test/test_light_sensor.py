from sensors.light_sensor import LightSensor
import unittest

class TestLightSensor(unittest.TestCase):

    def setUp(self):
        self.lightSensor = LightSensor()

    def test_getData(self):
        self.lightSensor.setData(30)
        self.assertEqual(self.lightSensor.getData(), 30)

    def test_checkEverythingNormal_success(self):
        self.lightSensor.setData(50)
        self.assertEqual(self.lightSensor.checkEverythingNormal(), True)

    def test_checkEverythingNormal_below_or_equal_10(self):
        self.lightSensor.setData(10)
        self.assertEqual(self.lightSensor.checkEverythingNormal(), False)

    def test_checkEverythingNormal_greater_or_equal_90(self):
        self.lightSensor.setData(90)
        self.assertEqual(self.lightSensor.checkEverythingNormal(), False)

    def test_setdata_success(self):
        self.lightSensor.setData(20)
        self.assertEqual(self.lightSensor.getData(), 20)

    def test_setdata_greater_100(self):
        self.lightSensor.setData(120)
        self.assertEqual(self.lightSensor.getData(), 0)

    def test_setdata_below_0(self):
        self.lightSensor.setData(-5)
        self.assertEqual(self.lightSensor.getData(), 0)

        