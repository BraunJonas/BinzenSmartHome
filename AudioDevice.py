from Device import Device
from IntencityToggleAble import IntencityToggleAble
from SwitchOnOffAble import SwitchOnOffAble


class AudioDevice(Device, IntencityToggleAble, SwitchOnOffAble):
    def __init__(self, name: str):
        print("Audiodevice " + name + " has been created")
        super().__init__(name)

    def setRunning(self, running: bool):
        super().setRunning(running)
        print("AudioDevice " + str(self.name) + " changed running to " + str(running))

    def setIntencity(self, intencity):
        super().setIntencity(intencity)
        print("Audiodevice " + self.name + " set to intensity: " + str(intencity))

    def activateNightMode(self):
        self.setRunning(False)
        self.setIntencity(5)
        print("AudioDevice " + str(self.name) + " activated Night Mode")

    def playAudio(self):
        if self.isRunning():
            print("AudioDevice " + str(self.name) + " is playing audio")
