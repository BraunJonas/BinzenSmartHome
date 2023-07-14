from sensors.water_level_sensor import WaterLevelSensor
import unittest

class TestWaterLevelSensor(unittest.TestCase):

    def setUp(self):
        self.waterLevelSensor = WaterLevelSensor()

    def test_getData(self):
        self.waterLevelSensor.setData(30)
        self.assertEqual(self.waterLevelSensor.getData(), 30)

    def test_checkEverythingNormal_success(self):
        self.waterLevelSensor.setData(60)
        self.assertEqual(self.waterLevelSensor.checkEverythingNormal(), True)

    def test_checkEverythingNormal_below_or_equal_40(self):
        self.waterLevelSensor.setData(40)
        self.assertEqual(self.waterLevelSensor.checkEverythingNormal(), False)

    def test_setdata_success(self):
        self.waterLevelSensor.setData(20)
        self.assertEqual(self.waterLevelSensor.getData(), 20)

    def test_setdata_greater_100(self):
        self.waterLevelSensor.setData(120)
        self.assertEqual(self.waterLevelSensor.getData(), 0)

    def test_setdata_below_0(self):
        self.waterLevelSensor.setData(-15)
        self.assertEqual(self.waterLevelSensor.getData(), 0)

        