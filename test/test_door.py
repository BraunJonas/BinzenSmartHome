import unittest
from devices.door import Door


class TestDevice(unittest.TestCase):

    def setUp(self):
        self.door = Door("Waschmachine")

    def test_setOpen(self):
        self.door.open = True
        self.assertEqual(self.door.open, True)
    
    def test_isOpen(self):
        self.door.open = True
        self.assertEqual(self.door.open, True)

    def test_isLocked(self):
        self.door.locked = False
        self.assertEqual(self.door.locked, False)

    def test_setLocked_locked(self):
        self.door.setOpen(False)
        self.logMessage = f"Door {self.door.name} was locked"
        with self.assertLogs() as log:
            self.door.setLocked(True)
        self.assertEqual(len(log.records), 1)
        self.assertEqual(log.records[0].getMessage(), self.logMessage)

    def test_setLocked_unlocked(self):
        self.door.setOpen(False)
        self.logMessage = f"Door {self.door.name} was unlocked"
        with self.assertLogs() as log:
            self.door.setLocked(False)
        self.assertEqual(len(log.records), 1)
        self.assertEqual(log.records[0].getMessage(), self.logMessage)

    def test_setLocked_doorOpen(self):
        self.door.setOpen(True)
        self.logMessage = f"Door {self.door.name} couldn't be locked because it is open"
        with self.assertLogs() as log:
            self.door.setLocked(True)
        self.assertEqual(len(log.records), 1)
        self.assertEqual(log.records[0].getMessage(), self.logMessage)

    def test_simuliereEinenThreadDurchlauf(self):
        self.door.setOpen(False)
        self.door.setLocked(True)
        self.logMessage = f"Door {self.door.name} is closed and locked"
        with self.assertLogs() as log:
            self.door.simuliereEinenThreadDurchlauf()
        self.assertEqual(len(log.records), 1)
        self.assertEqual(log.records[0].getMessage(), self.logMessage)
    