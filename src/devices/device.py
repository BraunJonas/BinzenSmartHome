# SDP # SDP - die Abhängigkeit verläuft in die selbe Richtung wie die Stabilität, sodass Device eine stabilere Klasse ist, als die Subklassen von Device

# SRP - alle Subklassen von Device haben eine klare Verantwortung und eine Aufgabe: z.B. ist CoolingDevice nur für die Steuerung von Kühlgeräten zuständig

# OCP - offen für Erweiterungen, geschlossen für Modifikationen: 
# Subklassen von Device erben von Device und erweitern die Funktionalität ohne den bestehenden Code zu ändern

class Device(): 
    name = ""
    def __init__(self, name:str):
        self.name = name

    def getName(self) -> str:
        return self.name
    
    def setName(self, name:str):
        self.name = name