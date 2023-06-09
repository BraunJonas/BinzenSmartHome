from abc import ABC, abstractmethod

# REP - alle Klassen des actors Packages sind wiederverwendbar

# CRP - die Klassen des actors Packages werden zusammen wiederverwendet

# SDP - die Abhängigkeit verläuft in die selbe Richtung wie die Stabilität, sodass Actor eine stabilere Klasse ist, als die Subklassen von Actor

# SAP - Stabilität wächst in Richtung der Abstraktheit, Actor ist stabil und abstrakt

# OCP - offen für Erweiterungen, geschlossen für Modifikationen: 
# Subklassen von Actor erben von Actor und erweitern die Funktionalität ohne den bestehenden Code zu ändern

# ISP - Aufteilung von Funktionen und Zuordnung zu spezifischen Klassen: 
# Actor hat 4 Subklassen die jeweils spezifische Funktionen implementieren,
# damit Klassen nur Methoden implementieren die sie tatsächlich benötigen und übermäßige Abhängigkeit verhindern

# DIP - Abhängigkeiten auf Abstraktionen: direkte Subklassen von Sensor nur von abstrakter Klasse Actor abhängig

class Actor(ABC):

    @abstractmethod
    def activateNightMode(self):
        pass

