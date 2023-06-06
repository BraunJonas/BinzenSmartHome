from actor import Actor


class IntensityToggleAble(Actor):
    intensity = 0

    def getIntensity(self) -> int:
        return self.intensity

    def setIntensity(self, intensity: int):
        if intensity > 100 or intensity < 0:
            raise Exception("not possible")
        self.intensity = intensity

