from device import Device
from actors.intensity_toggleable import IntensityToggleable
from actors.switch_on_offable import SwitchOnOffable



class AudioDevice(Device, IntensityToggleable, SwitchOnOffable):
    def __init__(self, name: str):
        print("Audiodevice " + name + " has been created")
        super().__init__(name)

    def setRunning(self, running: bool):
        super().setRunning(running)
        print("AudioDevice " + str(self.name) + " changed running to " + str(running))

    def setIntensity(self, intensity):
        super().setIntensity(intensity)
        print("Audiodevice " + self.name + " set to intensity: " + str(intensity))

    def activateNightMode(self):
        self.setRunning(False)
        self.setIntensity(5)
        print("AudioDevice " + str(self.name) + " activated Night Mode")

    def playAudio(self):
        if self.isRunning():
            print("AudioDevice " + str(self.name) + " is playing audio")


class Tv(AudioDevice):
    def __init__(self, name: str):
        print("TV " + name + " has been created")
        super().__init__(name)

    def playVideo(self):
        if self.isRunning():
            print("AudioDevice " + str(self.name) + " is playing video")

