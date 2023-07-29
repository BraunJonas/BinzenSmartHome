import unittest
from random import Random
from sensors.humidity_sensor import HumiditySensor

class TestHumiditySensor(unittest.TestCase):

    def setUp(self):
        self.humiditySensor = HumiditySensor()

    def test_getData(self):
        self.humiditySensor.setData(30)
        self.assertEqual(self.humiditySensor.getData(), 30)

    def test_checkEverythingNormal_success(self):
        self.humiditySensor.setData(50)
        self.assertEqual(self.humiditySensor.checkEverythingNormal(), True)

    # test if Methdod correctly when data is below or equal 30
    def test_checkEverythingNormal_below_or_equal_30(self):
        self.humiditySensor.setData(30)
        self.assertEqual(self.humiditySensor.checkEverythingNormal(), False)

    # test if Methdod correctly when data is greater or equal 70
    def test_checkEverythingNormal_greater_or_equal_70(self):
        self.humiditySensor.setData(70)
        self.assertEqual(self.humiditySensor.checkEverythingNormal(), False)

    def test_setdata_success(self):
        self.humiditySensor.setData(20)
        self.assertEqual(self.humiditySensor.getData(), 20)

    # test if Methdod sets data greater or equal 120
    def test_setdata_over_100(self):
        self.humiditySensor.setData(120)
        self.assertEqual(self.humiditySensor.getData(), 0)

    # test if Methdod sets data greater or equal 0
    def test_setdata_below_0(self):
        self.humiditySensor.setData(-5)
        self.assertEqual(self.humiditySensor.getData(), 0)


        