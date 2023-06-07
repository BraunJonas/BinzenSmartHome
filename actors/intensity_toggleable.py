from .actor import Actor

# ISP - Aufteilung von Funktionen und Zuordnung zu spezifischen Klassen: 
# Actor hat 4 Subklassen die jeweils spezifische Funktionen implementieren,
# damit Klassen nur Methoden implementieren, die sie tatsächlich benötigen und übermäßige Abhängigkeit verhindert
class IntensityToggleable(Actor):
    intensity = 0

    def getIntensity(self) -> int:
        return self.intensity

    def setIntensity(self, intensity: int):
        if intensity > 100 or intensity < 0:
            raise Exception("not possible")
        self.intensity = intensity

