from abc import ABC, abstractmethod

# REP - alle Klassen des sensors Packages sind wiederverwendbar

# CRP - die Klassen des sensors Packages werden zusammen wiederverwendet

# SDP - die Abhängigkeit verläuft in die selbe Richtung wie die Stabilität, sodass Sensor eine stabilere Klasse ist, als die Subklassen von Sensor

# SAP - Stabilität wächst in Richtung der Abstraktheit, Sensor ist stabil und abstrakt

# OCP - offen für Erweiterungen, geschlossen für Modifikationen: 
# Subklassen von Sensor erben von Sensor und erweitern die Funktionalität ohne den bestehenden Code zu ändern

# ISP - Aufteilung von Funktionen und Zuordnung zu spezifischen Klassen: 
# Sensor hat 2 Subklassen die jeweils spezifische Funktionen implementieren,
# damit Klassen nur Methoden implementieren die sie tatsächlich benötigen und übermäßige Abhängigkeit verhindern

# DIP - Abhängigkeiten auf Abstraktionen: direkte Subklassen von Sensor nur von abstrakter Klasse Sensor abhängig

class Sensor(ABC):
    @abstractmethod       
    def checkEverythingNormal(self) -> bool:
        pass

    