from AktorDevice import IntencityToggleAble
from Light import Light

class IntensityLight(IntencityToggleAble,Light):
    def __init__(self, name:str):
        print("IntensityLight "+ name +" has been created")
        super().__init__(name)

    def activateNightMode(self):
        super().activateNightMode()
        self.setIntencity(5)
        print("IntesnsityLight "+str(self.name) + " activated Night Mode")

    def setIntencity(self, intencity):
        super().setIntencity(intencity)
        print("IntensityLight "+ self.name +" set to intensity: "+ str(intencity))
