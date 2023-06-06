from Device import Device
from IntensityToggleAble import IntensityToggleAble
from SwitchOnOffAble import SwitchOnOffAble


class AudioDevice(Device, IntensityToggleAble, SwitchOnOffAble):
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
