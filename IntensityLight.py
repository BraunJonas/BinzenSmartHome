from IntensityToggleAble import IntensityToggleAble
from Light import Light


class IntensityLight(IntensityToggleAble, Light):
    def __init__(self, name: str):
        print("IntensityLight " + name + " has been created")
        super().__init__(name)

    def activateNightMode(self):
        super().activateNightMode()
        self.setIntensity(5)
        print("IntensityLight " + str(self.name) + " activated Night Mode")

    def setIntensity(self, intensity):
        super().setIntensity(intensity)
        print("IntensityLight " + self.name + " set to intensity: " + str(intensity))
