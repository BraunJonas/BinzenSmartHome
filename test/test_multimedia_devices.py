import unittest
from devices.multimedia_devices import AudioDevice
from devices.multimedia_devices import Tv


class TestAudioDevice(unittest.TestCase):

    def setUp(self):
        self.audioDevice = AudioDevice("Radio") 

    def test_getPercentage(self):
        self.audioDevice.setPercentage(30)
        self.assertEqual(self.audioDevice.getPercentage(), 30)
    
    def test_setPercentage(self):
        self.audioDevice.setPercentage(60)
        self.assertEqual(self.audioDevice.getPercentage(), 60)

    def test_setRunning(self):
        self.audioDevice.setRunning(True)
        self.assertEqual(self.audioDevice.isRunning(), True)

    def test_isRunning(self):
        self.audioDevice.setRunning(False)
        self.assertEqual(self.audioDevice.isRunning(), False)

    def test_playAudio_success(self):
        self.audioDevice.setRunning(True) 
        media = "Beispielsong"
        self.audioDevice.playAudio("Beispielsong")
        self.assertEqual(self.audioDevice.media, media)
    
    def test_playAudio_exception(self):
        self.audioDevice.setRunning(False)
        self.logMessage = f"AudioDevice {self.audioDevice.name} is turned off"
        with self.assertLogs() as log:
            self.audioDevice.playAudio("Song")
        #checks if only one message gets logged
        self.assertEqual(len(log.records), 1)
        self.assertEqual(log.records[0].getMessage(), self.logMessage)

    def test_simuliereEinenThreadDurchlauf_running(self):
        self.audioDevice.setRunning(True)
        self.audioDevice.setPercentage(80)
        self.audioDevice.media = "Song"
        self.logMessage = f"MultimediaDevice {self.audioDevice.name} is running with volume {self.audioDevice.volume} and playing {self.audioDevice.media}"
        with self.assertLogs() as log:
            self.audioDevice.simuliereEinenThreadDurchlauf()
        #checks if only one message gets logged
        self.assertEqual(len(log.records), 1)
        self.assertEqual(log.records[0].getMessage(), self.logMessage)
    
    def test_simuliereEinenThreadDurchlauf_notRunning(self):
        self.audioDevice.setRunning(False)
        self.logMessage = f"MultimediaDevice {self.audioDevice.name} is not running"
        with self.assertLogs() as log:
            self.audioDevice.simuliereEinenThreadDurchlauf()
        #checks if only one message gets logged
        self.assertEqual(len(log.records), 1)
        self.assertEqual(log.records[0].getMessage(), self.logMessage)
    
    def test_setReactToAlarms(self):
        ### TO-Do:   - test set-method
        #            - test if-else condition
        ""
    
    def test_getReactToAlarms(self):
        self.audioDevice.setReactToAlarms(True)
        self.assertEqual(self.audioDevice.getReactToAlarms(), True)
    
    def test_notify(self):
        ""

class TestTv(unittest.TestCase):

    def setUp(self):
        self.tv = Tv("Fernseher")
    

    ### Methode vollständig?

   #def test_playVideo_success(self):
   #    self.tv.setRunning(True) 
   #    media = "Beispielvideo"
   #    self.tv.playAudio("Beispielvideo")
   #    self.assertEqual(self.tv.media, media)


    